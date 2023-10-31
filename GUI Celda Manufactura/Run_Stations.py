import threading
import Station_ASRS
import Stations_Main
from robolink import *
from robodk import *


# Define una función que será ejecutada en cada hilo
def mi_funcion(station,ID,loc,num,piece):
    if station == 'Station_Lathe':
        pass
        #Stations_Main.runLatheSection(ID,num,loc,piece)
    if station == 'Station_Melling':
        pass
        #Stations_Main.runMellingSection(ID,num)
    if station == 'Station_Inspection':
        pass
        #Stations_Main.runInspectionSection(ID,num)
    if station == 'Station_ASRS':
        Station_ASRS.Run(ID,loc,'Get',num)
    if station == 'Station_ASRS2':
        Station_ASRS.Run(ID,loc,'Put',num)
        
def Run_Stations(ID,programs,loc,num,piece):
    # Crea una lista de hilos
    hilos = []

    for i in range (len(programs)):
        hilo = threading.Thread(target=mi_funcion, args=(programs[i],ID,loc,num,piece))
        hilos.append(hilo)
        hilo.start()

        for hilo in hilos:
            hilo.join()


    """
    # Crea y comienza cada hilo
    for i in range (len(programs)):
        hilo = threading.Thread(target=mi_funcion, args=(programs[i],ID,loc,num,piece))
        hilos.append(hilo)
        hilo.start()

    # Espera a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()
    return(True)
    """

Run_Stations('EP1_2023_23_10_C2_H10_T7',['Station_ASRS'],'[1,3]',1,'Piece1')