import threading
import Station_ASRS
import Main_Stations
from robolink import *
from robodk import *


# Define una función que será ejecutada en cada hilo
def mi_funcion(station,ID,loc,piece,run):
    if station == 'Station_Lathe':
        Main_Stations.Lathe_Section(ID,loc,piece,run)
    if station == 'Station_Melling':
        Main_Stations.Melling_Section(ID,run)
    if station == 'Station_Inspection':
        Main_Stations.Inspection_Section(ID,run)
    if station == 'Station_ASRS':
        Station_ASRS.Run(ID,loc,'Get')
    if station == 'Station_ASRS2':
        Main_Stations.ASRS_Section(ID,loc,'Put',run)
        
def Run_Stations(ID,programs,loc,piece):
    # Crea una lista de hilos
    hilos = []
    
    #logica del salto estación
    # 0 para saltarla 1 para ejecutarla
    run = [1,0,0,0,1]

    # LATHE
    if "Station_Lathe" in programs:
        run[1] = 1
    #MELLING
    if "Station_Melling" in programs:
        run[2] = 1
    #UR3
    if "Station_Inspection" in programs:
        run[3] = 1

    celda = ['Station_ASRS','Station_Lathe','Station_Melling','Station_Inspection','Station_ASRS2']

    for i in range (len(celda)):
        hilo = threading.Thread(target=mi_funcion, args=(celda[i],ID,loc,piece))
        hilos.append(hilo)
        hilo.start()

        for hilo in hilos:
            hilo.join()



def Run_Stations2(ID,programs,loc,piece):
    import time
    # Crea una lista de hilos
    hilos = []
    
    locations= ['[1,3]','[1,4]','[1,5]']

    for i in range (len(celda)):
        hilo = threading.Thread(target=Run_Stations, args=(locations[i],ID,loc,piece,run[i]))
        hilos.append(hilo)
        hilo.start()

        for hilo in hilos:
            hilo.join()



Run_Stations('EP3_2024_24_1_C1_H15_T26',['Station_Lathe','Station_Inspection'],locations[0],'Piece3')

for i in range(len(locations)-1):
    # Definir el tiempo de espera en segundos
    tiempo_espera = 40  # Cambia esto al tiempo deseado en segundos
    # Obtener el tiempo actual
    tiempo_inicio = time.time()
    # Realizar la pausa
    time.sleep(tiempo_espera)
    # Obtener el tiempo actual después de la pausa
    tiempo_transcurrido = time.time() - tiempo_inicio

    if tiempo_transcurrido >= tiempo_espera:
        Run_Stations('EP3_2024_24_1_C1_H15_T26',['Station_Lathe','Station_Inspection'],locations[i],'Piece3')