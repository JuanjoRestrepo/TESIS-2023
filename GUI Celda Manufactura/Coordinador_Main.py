import Graph
import Dashboard
import Robot_Simulation
from datetime import datetime

class coordinator():

    def __init__(self):
        self.base = Graph.graph()
        #self.robot = Robot_Simulation.Simulation()
        self.dash = Dashboard.dashboard()

    def Find_Index_Key(self,data,valor):
        return(data.index(valor))


    # ACCIONES CELDA DE MANUFACTURA
    def Init_Process(self):
        dash = self.dash
        #robot = self.robot
        base = self.base

        # Bring all the nodes type order with status Created
        orders_keys,orders_values = base.get_data_especific('order','State','Created')
        
        # If we dont have orders to run, notified
        #if len(orders) == 0:
        #    return("Lo lamento, en este momento no hay ninguna orden para ejecutar")

        # Run the steps of the order created
        for order in orders_values:

            material = order[self.Find_Index_Key(orders_keys[0],'Material')]
            ID = order[self.Find_Index_Key(orders_keys[0],'ID_Order')]
            
            # Update data
            base.update_data(ID,'order',['Running'],['State'])
            dash.Modified_Row(ID,'Running','Ordenes',1,8)

            if (material == 'Empack'):
                loc = 'Location_E'
            else:
                loc = 'Location_A'
        

            #Bring the location to run the ASRS

            storage = base.get_data('storage')
            #locations = storage[self.Find_Index_Key(storage.keys(),loc)]
            print(storage.keys)
            # cantidades
            # How many steps are needed
            # Run the steps
            # Update data
            #TENER EN CUENTA LA CANTIDAD DE PIEZAS A HACER

    def Stop_Process(self):
        pass
    
    def get_orders(self): # Show all the orders
        base = self.base
        key,orders = base.get_data('order')

        amount = eval(orders[self.Find_Index_Key(key[0],'Amount')])
        material = eval(orders[self.Find_Index_Key(key[0],'Material')])
        ID = eval(orders[self.Find_Index_Key(key[0],'ID_Order')])
        piece = eval(orders[self.Find_Index_Key(key[0],'Piece')])
        date = eval(orders[self.Find_Index_Key(key[0],'Create_Date')])
        state= eval(orders[self.Find_Index_Key(key[0],'State')])

        return([ID,amount,material,piece,date,state])
    
    def information_order(self,ID): # Get an especific order node
        base = self.base
        key,order = base.get_data_especific('order','Name',ID)
        return(key[0],order[0])

    def get_ID(self): # Get all the order IDs with state created
        base = self.base
        ID =[]
        key,values = base.get_data_especific('order','State','Created')
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
        keys,values= base.get_data('storage')

		# TRAER UBICACIONES
        if (material == 'Empack'):
            pos = 0
            loc ='Location_E'
            use = 'Used_E'
        else:
            pos = 1
            loc ='Location_A'
            use = 'Used_A'
        
        disponible = values[0]
        available = eval(disponible[self.Find_Index_Key(keys[0],'Available')]) # valor cantidad disponible material
        locations = eval(disponible[self.Find_Index_Key(keys[0],loc)]) # Ubicaciones
        used = eval(disponible[self.Find_Index_Key(keys[0],use)]) # Usadas
        
        if (int(available[pos]) == 0) or (int(available[pos])< amount):
            return(False,"")
        
        else:
            # Update locations
            location = locations[0:amount]
            del locations[0:amount]
            used.extend(location)
            available[pos] = int(available[pos]) - amount
            
            base.update_data('Storage','storage',[available,locations,used,str(datetime.now())],['Available',loc,use,'Update_Date'])
            

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
        material = eval(order_v[self.Find_Index_Key(order_k,'Material')])
        location =  eval(order_v[self.Find_Index_Key(order_k,'Locations')])

        # Bring storage information
        keys,values= base.get_data('storage')

		# Validate material case
        if (material == 'Empack'):
            pos = 0
            loc ='Location_E'
            use = 'Used_E'
        else:
            pos = 1
            loc ='Location_A'
            use = 'Used_A'
        
        # Update the material available
        disponible = values[0]
        available = eval(disponible[self.Find_Index_Key(keys[0],'Available')]) # valor cantidad disponible material
        locations = eval(disponible[self.Find_Index_Key(keys[0],loc)]) # Ubicaciones
        used = eval(disponible[self.Find_Index_Key(keys[0],use)]) # Usadas

        available[pos] = int(available[pos]) + amount
        locations.extend(eval(location))
        new_used = [valor for valor in used if valor not in eval(location)]

        locations =sorted(locations, key=lambda x: (x[0], x[1]))
        
        # Update data information
        base.update_data('Storage','storage',[available,locations,new_used,str(datetime.now())],['Available',loc,use,'Update_Date'])
        
        # Delete order in data and dashboard
        base.delete_node('order',ID)
        dash.Delete_Row(ID,'Ordenes')

        return('La orden'+str(ID)+'fue eliminada con éxito')

    def modify_order(self,ID,piece,material,amount,cpiece,cmaterial,camount):
        # PREGUNTAR SI ES NECESARIO MODIFICAR EL ID
        dash = self.dash
        base = self.base

        # Bring order information
        order_k,order_v = self.information_order(ID)
        last_amount = eval(order_v[self.Find_Index_Key(order_k,'Amount')])
        last_material = eval(order_v[self.Find_Index_Key(order_k,'Material')])
        last_piece = eval(order_v[self.Find_Index_Key(order_k,'Piece')])
        location =  eval(order_v[self.Find_Index_Key(order_k,'Locations')])

        keys,values= base.get_data('storage')
        disponible = values[0]
        available = eval(disponible[self.Find_Index_Key(keys[0],'Available')]) # valor cantidad disponible material
        locations_E = eval(disponible[self.Find_Index_Key(keys[0],'Location_E')]) # Ubicaciones
        locations_A = eval(disponible[self.Find_Index_Key(keys[0],'Location_A')])
        used_E = eval(disponible[self.Find_Index_Key(keys[0],'Used_E')]) # Usadas
        used_A = eval(disponible[self.Find_Index_Key(keys[0],'Used_A')]) 

        if cmaterial & (not camount):  # If the material change but the amount not
            if last_material == 'Empack':
                if available[1]==0 or available[1]< amount :
                    return('Lo lamento no se puede modificar la orden por falta de material')
                else:
                    locations = locations_A[0:amount]

                    available[0] = int(available[0]) + amount   
                    available[1] = int(available[1]) - amount   

                    locations_E.extend(eval(location))
                    locations_E = sorted(locations_E, key=lambda x: (x[0], x[1]))
                    del locations_A[0:amount]

                    used_A.extend(locations)
                    used_A = sorted(used_A, key=lambda x: (x[0], x[1]))
                    used_E = [valor for valor in used_E if valor not in eval(location)]

                    base.update_data('Storage','storage',[available,locations_E,locations_A,used_E,used_A,str(datetime.now())],['Available','Location_E','Location_A','Used_E','Used_A','Update_Date'])
                    base.update_data(ID,'order',[piece,material,amount,locations,str(datetime.now())],['Piece','Material','Amount','Locations','Update_Date'])
                    dash.Modified_Row(ID,material,'Ordenes',1,4) #material
                    dash.Modified_Row(ID,piece,'Ordenes',1,5) #piece
                    return('La orden'+str(ID)+'fue modificada con éxito')

            else:

                if available[0]==0 or available[0]< amount :
                    return('Lo lamento no se puede modificar la orden por falta de material')
                else:
                    locations = locations_E[0:amount]

                    available[0] = int(available[0]) - amount   
                    available[1] = int(available[1]) + amount   

                    locations_A.extend(eval(location))
                    locations_A = sorted(locations_A, key=lambda x: (x[0], x[1]))
                    del locations_E[0:amount]

                    used_E.extend(locations)
                    used_E = sorted(used_E, key=lambda x: (x[0], x[1]))
                    used_A = [valor for valor in used_A if valor not in eval(location)]

                    base.update_data('Storage','storage',[available,locations_E,locations_A,used_E,used_A,str(datetime.now())],['Available','Location_E','Location_A','Used_E','Used_A','Update_Date'])
                    base.update_data(ID,'order',[piece,material,amount,locations,str(datetime.now())],['Piece','Material','Amount','Locations','Update_Date'])
                    dash.Modified_Row(ID,material,'Ordenes',1,4) #material
                    dash.Modified_Row(ID,piece,'Ordenes',1,5) #piece
                    return('La orden'+str(ID)+'fue modificada con éxito')
        
        if camount & (not cmaterial):  # If the amount change but the material not
            if last_material == 'Empack':
                if available[0]==0 or (available[0]+last_amount) < amount :
                    return('Lo lamento no se puede modificar la orden por falta de material')
                else:
                    locations_E.extend(eval(location))
                    locations_E = sorted(locations_E, key=lambda x: (x[0], x[1]))
                    locations = locations_E[0:amount]
                    del locations_E[0:amount]

                    available[0] = int(available[0]) + last_amount- amount   

                    
                    used_E = [valor for valor in used_E if valor not in eval(location)]
                    used_E.extend(locations)
                    used_E = sorted(used_E, key=lambda x: (x[0], x[1]))

                    base.update_data('Storage','storage',[available,locations_E,used_E,str(datetime.now())],['Available','Location_E','Used_E','Update_Date'])
                    base.update_data(ID,'order',[piece,material,amount,locations,str(datetime.now())],['Piece','Material','Amount','Locations','Update_Date'])
                    dash.Modified_Row(ID,amount,'Ordenes',1,6) #amount
                    dash.Modified_Row(ID,piece,'Ordenes',1,5) #piece
                    return('La orden'+str(ID)+'fue modificada con éxito')

            else:

                if available[1]==0 or (available[1]+last_amount) < amount :
                    return('Lo lamento no se puede modificar la orden por falta de material')
                else:
                    locations_A.extend(eval(location))
                    locations_A = sorted(locations_A, key=lambda x: (x[0], x[1]))
                    locations = locations_A[0:amount]
                    del locations_A[0:amount]

                    available[0] = int(available[0]) + last_amount- amount   

                    
                    used_A = [valor for valor in used_A if valor not in eval(location)]
                    used_A.extend(locations)
                    used_A = sorted(used_A, key=lambda x: (x[0], x[1]))

                    base.update_data('Storage','storage',[available,locations_A,used_A,str(datetime.now())],['Available','Location_A','Used_A','Update_Date'])
                    base.update_data(ID,'order',[piece,material,amount,locations,str(datetime.now())],['Piece','Material','Amount','Locations','Update_Date'])
                    dash.Modified_Row(ID,amount,'Ordenes',1,6) #amount
                    dash.Modified_Row(ID,piece,'Ordenes',1,5) #piece
                    return('La orden'+str(ID)+'fue modificada con éxito')
        
        if camount & cmaterial:  # If both changed
            if last_material == 'Empack':
                if available[0]==0 or (available[0]+last_amount) < amount :
                    return('Lo lamento no se puede modificar la orden por falta de material')
                else:
                    locations_E.extend(eval(location))
                    locations_E = sorted(locations_E, key=lambda x: (x[0], x[1]))
                    locations = locations_E[0:amount]
                    del locations_E[0:amount]

                    available[0] = int(available[0]) + last_amount- amount   

                    
                    used_E = [valor for valor in used_E if valor not in eval(location)]
                    used_E.extend(locations)
                    used_E = sorted(used_E, key=lambda x: (x[0], x[1]))

                    base.update_data('Storage','storage',[available,locations_E,used_E,str(datetime.now())],['Available','Location_E','Used_E','Update_Date'])
                    base.update_data(ID,'order',[piece,material,amount,locations,str(datetime.now())],['Piece','Material','Amount','Locations','Update_Date'])
                    dash.Modified_Row(ID,amount,'Ordenes',1,6) #amount
                    dash.Modified_Row(ID,piece,'Ordenes',1,5) #piece
                    return('La orden'+str(ID)+'fue modificada con éxito')

            else:
                pass
        
    def modify_storage(self,name,data,propiedades): #modify storage properties
        base = self.base
        base.update_data(name,'storage',data,propiedades)
        return('El storage fue actualizado con éxito')
        # TENER EN CUENTA QUE LA NUEVA INFORMACION DEBE CUMPLIR CON LOS CRITERIOS
        
    

run = coordinator()

#run.Init_Process()
#print(run.get_ID())
#print(run.information_order('AP1_2023_10_8_C5_H18_T22'))
#print(run.get_storage())
#print(run.get_orders())
#print(run.create_order('Aluminio',3,'piece1'))
#print(run.create_order('Empack',5,'piece2'))
#print(run.delete_order('AP1_2023_10_8_C5_H18_T22',5,'Aluminio','[[1, 1], [1, 2], [2, 1], [2, 2], [3, 1]]'))
#run.get_orders()
#print(run.modify_order('EP2_2023_10_8_C5_H21_T0','piece2','Empack',2,'piece2','Empack',3,False,False,True,'[[1, 3], [1, 4], [1, 5], [2, 3], [2, 4]]'))