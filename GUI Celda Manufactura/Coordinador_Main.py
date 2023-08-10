import Graph
import Dashboard
import Robot_Simulation


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
            # How many steps are needed
            # Run the steps
            # Update data


            
    def Stop_Process(self):
        pass

    def create_order(self,material,amount,piece):
        dash = self.dash
        base = self.base
        keys,values= base.get_data('storage')

		# TRAER UBICACIONES
        if (material == 'Empack'):
            pos = 0
        else:
            pos = 1
        
        disponible = values[0]
        available = disponible[self.Find_Index_Key(keys[0],'Available')] # valor cantidad disponible material
        if (int(available[pos]) == 0) or (int(available[pos])< amount):
            return('Lo lamento no es posible crear la orden por falta de material')
        
        else:
            # CREA LA ORDEN Y ACTUALIZA
            data = base.create_order(material,amount,piece)
            dash.Add_End(data,'Ordenes')
            available[pos] = int(available[pos]) - amount
            base.update_data('Storage','storage',[available],['Available'])
            return('La orden fue creada con el ID',data[0])
        
    def delete_order(self,ID):
        dash = self.dash
        base = self.base

        base.delete_node('order',ID)
        dash.Delete_Row(ID,'Ordenes')
        return('La orden',ID,'fue eliminada con éxito')

    def modify_order(self):
        pass
    def modify_storage(self):
        pass
    def get_orders(self):
        pass
    def get_ID(self):
        pass
    def get_storage(self):
        pass



        




run = coordinator()

#run.Init_Process()

run.crear('Aluminio',5,'piece1')