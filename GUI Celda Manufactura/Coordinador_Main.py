import Graph
import Dashboard
import Run_Stations
from datetime import datetime

class coordinator():

    def __init__(self):
        self.base = Graph.graph()
        self.dash = Dashboard.dashboard()

    def Find_Index_Key(self,data,valor):
        return(data.index(valor))

    # Start Process (Run Manufacturing Cell)
    def Start_Process(self):
        dash = self.dash
        base = self.base

        # Bring all the nodes type order with status Created
        orders_keys,orders_values = base.get_data_especific('order','State','Running')
        # If we dont have orders to run, notified
        if len(orders_values) == 0:
            return([True,"Lo lamento, en este momento no hay ninguna orden para ejecutar"])

        # Run the steps of the order created
        for order in orders_values:
            Run = True

            locations = eval(order[self.Find_Index_Key(orders_keys[0],'Locations')]) # Bring Locations to ASRS                                
            ID = order[self.Find_Index_Key(orders_keys[0],'ID_Order')] 
            amount = order[self.Find_Index_Key(orders_keys[0],'Amount')]
            piece = order[self.Find_Index_Key(orders_keys[0],'Piece')]
            steps,files,stations = base.get_steps(piece)
            
            # Update data
            base.update_data(ID,'order',['Running'],['State'])
            dash.Modified_Row(ID,'Running','Ordenes',1,9)

            # Logic for Run
            create = 1
            progress = [0]*len(steps) 
     
            while Run:
                if progress[-1] != amount:  # correr todas las piezas en la última estacion
                    if (create <= int(len(steps))) and (create <= int(amount)): 
                        finish = Run_Stations.Run_Stations(ID,files[:create],locations[0],create)
                        print(finish)
                        if finish:
                            for n in range(create):
                                progress[n]=+1
                            print(progress)
                            create=+1
                            locations.pop(0)
                        else:
                            #COMPLETAR LOGICA DE ERROR
                            return([True,"Se presento un ERROR en la ejecución"])

                    else:
                        if progress[0] != amount:
                            finish = Run_Stations.Run_Stations(ID,files[:len(steps)],locations[0],create)
                            if finish:
                                for n in range(len(progress)):
                                    progress[n]=+1
                                if len(locations)==0:
                                    locations =""
                                else:
                                    locations.pop(0)
                            else:
                                #COMPLETAR LOGICA DE ERROR
                                return([True,"Se presento un ERROR en la ejecución"])
                        else:
                            progress.pop(0)
                            files.pop(0)
                            steps.pop(0)
                else:
                    Run = False

            # Update data
            base.update_data(ID,'order',['Finished'],['State'])
            dash.Modified_Row(ID,'Finished','Ordenes',1,9)
            return("run1")
            

            # INSERTA LOGICA DE BOTON APAGADO

    def get_orders(self): # Show all the orders
        base = self.base
        key,orders = base.get_data('order')
        f_orders =[]

        for i in orders:
            amount = i[self.Find_Index_Key(key[0],'Amount')]
            material = i[self.Find_Index_Key(key[0],'Material')]
            ID = i[self.Find_Index_Key(key[0],'ID_Order')]
            piece = i[self.Find_Index_Key(key[0],'Piece')]
            date = i[self.Find_Index_Key(key[0],'Create_Date')]
            state= i[self.Find_Index_Key(key[0],'State')]

            f_orders.append([ID,amount,material,piece,date,state])
        return(f_orders)
    
    def information_order(self,ID): # Get an especific order node
        base = self.base
        key,order = base.get_data_especific('order','Name',ID)

        return(key[0],order[0])

    def get_ID(self): # Get all the order IDs with state created
        base = self.base
        ID =[]
        key,values = base.get_data_especific('order','State','Created')
        if len(values) == 0:
            return(ID)
        else:
            index = self.Find_Index_Key(key[0],'ID_Order')
            for i in values:
                ID.append(i[index])
            return(ID)

    def get_storage(self): # Get Storage properties
        base = self.base
        key,value = base.get_data_especific('storage','Name','Storage')
        return(key[0],value[0])
    
    def create_order(self,material,piece,amount):
        dash = self.dash
        base = self.base
        keys,values= base.get_data_especific('material','Name',material)
        
        disponible = values[0]
        
        available = eval(disponible[self.Find_Index_Key(keys[0],'Available')]) # valor cantidad disponible material
        locations = eval(disponible[self.Find_Index_Key(keys[0],'Location')]) # Ubicaciones
        used = eval(disponible[self.Find_Index_Key(keys[0],'Used')]) # Usadas
        
        
        if (int(available == 0) or (int(available)< amount)):
            return(False,"")
        
        else:
            # Update locations
            location = locations[0:amount]
            del locations[0:amount]
            used.extend(location)
            available = int(available) - amount
            
            base.update_data(material,'material',[available,locations,used,str(datetime.now())],['Available','Location','Used','Update_Date'])
            
            # Create and Update Order
            data = base.create_order(material,amount,piece,location)
            dash.Add_End(data,'Ordenes')
            
            return(True,data)
        
        
    def delete_order(self,ID):
        dash = self.dash
        base = self.base

        # Bring order information
        order_k,order_v = self.information_order(ID)
        amount = eval(order_v[self.Find_Index_Key(order_k,'Amount')])
        material = order_v[self.Find_Index_Key(order_k,'Material')]
        location =  order_v[self.Find_Index_Key(order_k,'Locations')]

        # Bring materials information
        keys,values= base.get_data_especific('material','Name',material)
        
        disponible = values[0]
        available = eval(disponible[self.Find_Index_Key(keys[0],'Available')]) # valor cantidad disponible material
        locations = eval(disponible[self.Find_Index_Key(keys[0],'Location')]) # Ubicaciones
        used = eval(disponible[self.Find_Index_Key(keys[0],'Used')]) # Usadas

        available= int(available) + amount
        locations.extend(eval(location))
        new_used = [valor for valor in used if valor not in eval(location)]

        locations =sorted(locations, key=lambda x: (x[0], x[1]))
        
        # Update data information
        base.update_data(material,'material',[available,locations,new_used,str(datetime.now())],['Available','Location','Used','Update_Date'])
        
        # Delete order in data and dashboard
        base.delete_node('order',ID)
        dash.Delete_Row(ID,'Ordenes')

        return('La orden '+str(ID)+' fue eliminada con éxito')

    def modify_order(self,ID,piece,material,amount,cpiece,cmaterial,camount):
        # PREGUNTAR SI ES NECESARIO MODIFICAR EL ID
        dash = self.dash
        base = self.base
        
        # Bring order information
        order_k,order_v = self.information_order(ID)
        last_amount = int(order_v[self.Find_Index_Key(order_k,'Amount')])
        last_material = order_v[self.Find_Index_Key(order_k,'Material')]
        last_piece = order_v[self.Find_Index_Key(order_k,'Piece')]
        location =  order_v[self.Find_Index_Key(order_k,'Locations')]

        key_E,value_E= base.get_data_especific('material','Name','Empack')
        available_E = int(value_E[0][self.Find_Index_Key(key_E[0],'Available')]) # valor cantidad disponible material
        locations_E = eval(value_E[0][self.Find_Index_Key(key_E[0],'Location')]) # Ubicaciones
        used_E = eval(value_E[0][self.Find_Index_Key(key_E[0],'Used')]) # Usadas

        key_A,value_A= base.get_data_especific('material','Name','Aluminio')
        available_A = int(value_A[0][self.Find_Index_Key(key_A[0],'Available')]) # valor cantidad disponible material
        locations_A = eval(value_A[0][self.Find_Index_Key(key_A[0],'Location')]) # Ubicaciones
        used_A = eval(value_A[0][self.Find_Index_Key(key_A[0],'Used')]) # Usadas
        
        if cpiece:
            base.delete_relation('PIECE',ID,last_piece,'order',last_piece)
            base.relation('PIECE','order',piece,ID,piece)
            base.update_data(ID,'order',[piece,str(datetime.now())],['Piece','Update_Date'])
            dash.Modified_Row(ID,piece,'Ordenes',1,5) #piece

        if cmaterial & (not camount):  # If the material change but the amount not
            if last_material == 'Empack':
                if available_A==0 or available_A< amount :
                    return('Lo lamento no se puede modificar la orden por falta de material')
                else:
                    locations = locations_A[0:amount]

                    available_A = int(available_A) - amount   
                    available_E = int(available_E) + amount   

                    locations_E.extend(eval(location))
                    locations_E = sorted(locations_E, key=lambda x: (x[0], x[1]))
                    del locations_A[0:amount]

                    used_A.extend(locations)
                    used_A = sorted(used_A, key=lambda x: (x[0], x[1]))
                    used_E = [valor for valor in used_E if valor not in eval(location)]

                    base.update_data('Empack','material',[available_E,locations_E,used_E,str(datetime.now())],['Available','Location','Used','Update_Date'])
                    base.update_data('Aluminio','material',[available_A,locations_A,used_A,str(datetime.now())],['Available','Location','Used','Update_Date'])
                    base.update_data(ID,'order',[material,amount,locations,str(datetime.now())],['Material','Amount','Locations','Update_Date'])
                    dash.Modified_Row(ID,material,'Ordenes',1,4) #material
                    return('La orden '+str(ID)+' fue modificada con éxito')

            else:

                if available_E==0 or available_E< amount :
                    return('Lo lamento no se puede modificar la orden por falta de material')
                else:
                    locations = locations_E[0:amount]

                    available_A = int(available_A) + amount   
                    available_E = int(available_E) - amount   

                    locations_A.extend(eval(location))
                    locations_A = sorted(locations_A, key=lambda x: (x[0], x[1]))
                    del locations_E[0:amount]

                    used_E.extend(locations)
                    used_E = sorted(used_E, key=lambda x: (x[0], x[1]))
                    used_A = [valor for valor in used_A if valor not in eval(location)]

                    base.update_data('Empack','material',[available_E,locations_E,used_E,str(datetime.now())],['Available','Location','Used','Update_Date'])
                    base.update_data('Aluminio','material',[available_A,locations_A,used_A,str(datetime.now())],['Available','Location','Used','Update_Date'])
                    base.update_data(ID,'order',[material,amount,locations,str(datetime.now())],['Material','Amount','Locations','Update_Date'])
                    dash.Modified_Row(ID,material,'Ordenes',1,4) #material
                    return('La orden '+str(ID)+' fue modificada con éxito')
        
        if camount & (not cmaterial):  # If the amount change but the material not
            if last_material == 'Empack':
                if available_E==0 or (available_E+last_amount) < amount :
                    return('Lo lamento no se puede modificar la orden por falta de material')
                else:
                    locations_E.extend(eval(location))
                    locations_E = sorted(locations_E, key=lambda x: (x[0], x[1]))
                    locations = locations_E[0:amount]
                    del locations_E[0:amount]

                    available_E = int(available_E) + last_amount- amount   

                    
                    used_E = [valor for valor in used_E if valor not in eval(location)]
                    used_E.extend(locations)
                    used_E = sorted(used_E, key=lambda x: (x[0], x[1]))

                    base.update_data('Empack','material',[available_E,locations_E,used_E,str(datetime.now())],['Available','Location','Used','Update_Date'])
                    base.update_data(ID,'order',[material,amount,locations,str(datetime.now())],['Material','Amount','Locations','Update_Date'])
                    dash.Modified_Row(ID,amount,'Ordenes',1,6) #amount
                    dash.Modified_Row(ID,material,'Ordenes',1,4) #material
                    return('La orden '+str(ID)+' fue modificada con éxito')

            else:

                if available_A==0 or (available_A+last_amount) < amount :
                    return('Lo lamento no se puede modificar la orden por falta de material')
                else:
                    locations_A.extend(eval(location))
                    locations_A = sorted(locations_A, key=lambda x: (x[0], x[1]))
                    locations = locations_A[0:amount]
                    del locations_A[0:amount]

                    available_A = int(available_A) + last_amount- amount   

                    
                    used_A = [valor for valor in used_A if valor not in eval(location)]
                    used_A.extend(locations)
                    used_A = sorted(used_A, key=lambda x: (x[0], x[1]))

                    base.update_data('Aluminio','material',[available_A,locations_A,used_A,str(datetime.now())],['Available','Location','Used','Update_Date'])
                    base.update_data(ID,'order',[material,amount,locations,str(datetime.now())],['Material','Amount','Locations','Update_Date'])
                    dash.Modified_Row(ID,amount,'Ordenes',1,6) #amount
                    dash.Modified_Row(ID,material,'Ordenes',1,4) #material
                    return('La orden'+str(ID)+'fue modificada con éxito')
        
        if camount & cmaterial:  # If both changed
            if last_material == 'Empack':
                if available_A==0 or available_A< amount :
                    return('Lo lamento no se puede modificar la orden por falta de material')
                else:
                    locations_E.extend(eval(location))
                    locations_E = sorted(locations_E, key=lambda x: (x[0], x[1]))

                    locations = locations_A[0:amount]
                    del locations_A[0:amount]

                    available_A = int(available_A) - amount   
                    available_E = int(available_E) + last_amount  

                    
                    used_A.extend(locations)
                    used_A = sorted(used_E, key=lambda x: (x[0], x[1]))
                    used_E = [valor for valor in used_E if valor not in eval(location)]

                    base.update_data('Empack','material',[available_E,locations_E,used_E,str(datetime.now())],['Available','Location','Used','Update_Date'])
                    base.update_data('Aluminio','material',[available_A,locations_A,used_A,str(datetime.now())],['Available','Location','Used','Update_Date'])
                    base.update_data(ID,'order',[material,amount,locations,str(datetime.now())],['Material','Amount','Locations','Update_Date'])
                    dash.Modified_Row(ID,amount,'Ordenes',1,6) #amount
                    dash.Modified_Row(ID,material,'Ordenes',1,4) #material
                    return('La orden '+str(ID)+' fue modificada con éxito')

            else:
                pass
        
    def modify_storage(self,material,amount,ID): #modify storage properties
        base = self.base
        keys,values= base.get_data_especific('material','Name',material)
        
        disponible = values[0]
        
        available = eval(disponible[self.Find_Index_Key(keys[0],'Available')]) # valor cantidad disponible material
        locations = eval(disponible[self.Find_Index_Key(keys[0],'Location')]) # Ubicaciones
        used = eval(disponible[self.Find_Index_Key(keys[0],'Used')]) # Usadas
        
        if (int(available == 0) or (int(available)< amount)):
            return(False,"")
        
        else:
            # Update locations
            location = locations[0:amount]
            del locations[0:amount]
            used.extend(location)
            available = int(available) - amount
            
            base.update_data(material,'material',[available,locations,used,str(datetime.now())],['Available','Location','Used','Update_Date'])
            base.update_data(ID,'order',[location,str(datetime.now())],['Locations','Update_Date'])

            return(True)
        
    
#run = coordinator()

#print(run.Start_Process())
#print(run.get_ID())
#print(run.information_order('AP1_2023_30_8_C5_H11_T33'))
#print(run.get_storage())
#print(run.get_orders())
#print(run.create_order('Aluminio',"Piece1",3))
#print(run.create_order('Empack',"Piece2",5))
#print(run.delete_order('AP1_2023_10_8_C5_H18_T22',5,'Aluminio','[[1, 1], [1, 2], [2, 1], [2, 2], [3, 1]]'))
#print(run.get_orders())
#print(run.modify_order('EP2_2023_10_8_C5_H21_T0','piece2','Empack',2,'piece2','Empack',3,False,False,True,'[[1, 3], [1, 4], [1, 5], [2, 3], [2, 4]]'))