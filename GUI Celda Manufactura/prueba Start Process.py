import Graph
import Dashboard
import Run_Stations
from datetime import datetime

def Start_Process(self):
    dash = self.dash
    base = self.base

    # Bring all the nodes type order with status Created
    orders_keys,orders_values = base.get_data_especific('order','State','Created')
    # If we dont have orders to run, notified
    if len(orders_values) == 0:
        return([True,"Lo lamento, en este momento no hay ninguna orden para ejecutar"])

    # Run the steps of the order created
    for order in orders_values:
        
        locations = eval(order[self.Find_Index_Key(orders_keys[0],'Locations')]) # Bring Locations to ASRS                                
        ID = order[self.Find_Index_Key(orders_keys[0],'ID_Order')] 
        amount = order[self.Find_Index_Key(orders_keys[0],'Amount')]
        piece = order[self.Find_Index_Key(orders_keys[0],'Piece')]
        steps,files,stations = base.get_steps(piece)
        
        # Update data
        base.update_data(ID,'order',['Running',str(datetime.now())],['State','Update_Date'])
        dash.Modified_Row(ID,'Running','Ordenes',1,9)
        
        
        
        Run_Stations.Run_Stations(ID,files,locations[0],piece)
        
        # Update data
        piece_keys,piece_values = base.get_data_especific('piece','Name',piece)
        produced = piece_values[0][self.Find_Index_Key(piece_keys[0],'Produced')]
        new_produced= int(produced) + 1
        base.update_data(piece,'piece',[str(new_produced),str(datetime.now())],['Produced','Update_Date'])
        
        base.update_data(ID,'order',['Finished',str(datetime.now())],['State','Update_Date'])
        dash.Modified_Row(ID,'Finished','Ordenes',1,9) # Status
        dash.Modified_Row(ID,str(datetime.now()),'Ordenes',1,3) # Fecha fin

        total_time = base.total_time(ID)
        dash.Modified_Row(ID,total_time,'Ordenes',1,8) # Tiempo total
        return([True,"Celda ejecutada exitosamente"])
