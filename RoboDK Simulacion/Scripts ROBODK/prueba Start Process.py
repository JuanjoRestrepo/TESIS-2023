import Graph
import Dashboard
import Run_Stations
from datetime import datetime

def Find_Index_Key(data,valor):
        return(data.index(valor))

def Start_Process():
    dash = Dashboard.dashboard()
    base = Graph.graph()

    # Bring all the nodes type order with status Created
    orders_keys,orders_values = base.get_data_especific('order','State','Created')
    # If we dont have orders to run, notified
    if len(orders_values) == 0:
        return([True,"Lo lamento, en este momento no hay ninguna orden para ejecutar"])
    
    # Run the steps of the order created
    for order in orders_values:
        Run = True

        locations = eval(order[Find_Index_Key(orders_keys[0],'Locations')]) # Bring Locations to ASRS                                
        ID = order[Find_Index_Key(orders_keys[0],'ID_Order')] 
        amount = order[Find_Index_Key(orders_keys[0],'Amount')]
        piece = order[Find_Index_Key(orders_keys[0],'Piece')]
        steps,files,stations = base.get_steps(piece)
  
        # Update data
        #base.update_data(ID,'order',['Running'],['State'])
        #dash.Modified_Row(ID,'Running','Ordenes',1,9)

        # Logic for Run
        create = 1
        progress = [0]*len(steps) 

    
        while Run:
            if progress[-1] != amount:  # correr todas las piezas hasta la última estacion
                if (create <= int(len(steps))) and (create <= int(amount)): 
                    finish = Run_Stations.Run_Stations(ID,files[:create],locations[create-1],create,piece)
                    print(finish)
                    if finish:
                        for n in range(create):
                            progress[n]=+1
                        print(progress)
                        create=+1
                    else:
                        #COMPLETAR LOGICA DE ERROR
                        return([True,"Se presento un ERROR en la ejecución"])
    """
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
        """
Start_Process()