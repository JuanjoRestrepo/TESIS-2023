import multiprocessing
# multipo-proce #scrip.py

def stations(loc,script,ID):
    if script == 'Station_Lathe':
        pass
        #Station_Lathe
    #elif script == 'Station_Melling':
    #    Station_Melling.Run(ID)
    #elif script == 'Station_Inspection':
    #    Station_Inspection.Run(ID)
    #elif script == 'Station_ASRS':
    #    Station_ASRS.Run(ID,loc)
    #else:
    #    Station_ASRS2.Run(ID,loc)

def run_process(ID,files,loc):
    # Crea procesos para ejecutar cada script
    procesos = []
    for script in files:
        proceso = multiprocessing.Process(target=script)
        procesos.append(proceso)
        proceso.start()

    # Espera a que todos los procesos terminen
    for proceso in procesos:
        proceso.join()

    return(True)

run_process(1,['Station_Lathe.py'],1)