import threading
import Station_Lathe
import Station_ASRS
import Station_Inspection
import Station_Melling
from robolink import *
from robodk import *

# Define una función que será ejecutada en cada hilo
def mi_funcion(station,ID,loc,num,piece):
    if station == 'Station_Lathe':
        Station_Lathe.Run(ID,num,loc,piece)
    if station == 'Station_Melling':
        Station_Melling.Run(ID,num)
    if station == 'Station_Inspection':
        Station_Inspection.Run(ID,num)
    if station == 'Station_ASRS':
        Station_ASRS.Run(ID,loc,'Get',num)
    if station == 'Station_ASRS2':
        Station_ASRS.Run(ID,loc,'Put',num)
        
def Run_Stations(ID,programs,loc,num,piece):
    # Crea una lista de hilos
    hilos = []
    
    # Crea y comienza cada hilo
    for i in range (len(programs)):
        hilo = threading.Thread(target=mi_funcion, args=(programs[i],ID,loc,num,piece))
        hilos.append(hilo)
        hilo.start()

    # Espera a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()
    return(True)

#Run_Stations('AP2_2023_10_10_C1_H17_T3',['Station_Lathe','Station_Melling','Station_Inspection'],'ffff',1,'Piece2')