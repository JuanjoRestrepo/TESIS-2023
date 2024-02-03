from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
import time
import Dashboard
import Graph
from datetime import datetime

RDK = Robolink()

#Set the travel of the conveyors for each iterations
PART_TRAVEL_MM1 = 50
PART_TRAVEL_MM2 = 60
PART_TRAVEL_MM3 = 50
PART_TRAVEL_MM4 = 100

#Declaration of the conveyor object
Conv_mechanism1 = RDK.Item('Conv_Mech1',itemtype=ITEM_TYPE_ROBOT)
Conv_mechanism2 = RDK.Item('Conv_Mech2',itemtype=ITEM_TYPE_ROBOT)
Conv_mechanism3 = RDK.Item('Conv_Mech3',itemtype=ITEM_TYPE_ROBOT)
Conv_mechanism4 = RDK.Item('Conv_Mech4',itemtype=ITEM_TYPE_ROBOT)

frameConv3 = RDK.Item('Frame_Conv3')
LatheFrame = RDK.Item('Lathe')

# === Pick Targets ===
tolerance = 15
pick_positionTorno = 1090.0
pick_positionFresado = 1015.0
pick_positionASRS = 960.0
pick_positionUR3 = 950.0

def update(banda,time,ID,station,machine):
    dash = Dashboard.dashboard()
    base = Graph.graph()

    # Actualización de la base y dashboard
    dash.Add_End([banda,str(datetime.now()),time,ID,'Exitoso'],'Ejecuciones Máquinas')
    station2 = base.exist_relation('station','TIME_STATION',station)
    machine2 = base.exist_relation('machine','TIME_MACHINE',machine)
    
    # Band Machine
    if machine2 == 0:
        base.create_relation_data('TIME_MACHINE',"time:"+str(time),'order','machine',ID,machine)
    else:
        tiempo = base.get_data_relation('order',ID,'machine',machine,'TIME_MACHINE')
        tiempo = tiempo[1][0][0]
        nuevo_tiempo = float(tiempo) + time
        base.update_data_relation(ID,'order',machine,'machine',nuevo_tiempo,'TIME_MACHINE','time')
    
    # Band Station
    if station2 == 0:
        base.create_relation_data('TIME_STATION',"time:"+str(time),'order','station',ID,station)
    else:
        tiempo = base.get_data_relation('order',ID,'station',station,'TIME_STATION')
        tiempo = tiempo[1][0][0]
        nuevo_tiempo = float(tiempo) + time
        base.update_data_relation(ID,'order',station,'station',nuevo_tiempo,'TIME_STATION','time')
    
def MoveConveyor1(conveyor, part_travel_mm,pieza,ID):
    OnPickTarget = None
    tiempo_total = 0
    tiempo = time.time()
    if conveyor.Valid():
        conveyor.MoveJ(conveyor.Joints() + part_travel_mm)
        while conveyor.Valid():
            current_position = conveyor.Pose()[0, 3]  # Obtiene la posición actual del marco
            piece_position = pieza.PoseAbs()[0, 3] 

            # Verifica si la próxima posición excederá el límite de 2000
            next_position = current_position + part_travel_mm
            if next_position > 2100:
                tiempo2 = time.time()
                tiempo_total = (tiempo2 - tiempo) + tiempo_total
                tiempo_total = round(tiempo_total,2)
                update('Banda UR3',tiempo_total,ID,'Station_Inspection','Conveyor_Inspection')
                return(True,False)
            elif abs(pick_positionUR3 - current_position) < tolerance:
                OnPickTarget = True
                tiempo2 = time.time()
                tiempo_total = (tiempo2 - tiempo) + tiempo_total
                tiempo_total = round(tiempo_total,2)
                update('Banda UR3',tiempo_total,ID,'Station_Inspection','Conveyor_Inspection')
                return(False,OnPickTarget)
            else:
                # Mueve la banda
                conveyor.MoveJ(conveyor.Joints() + part_travel_mm)

def MoveConveyor2(conveyor, part_travel_mm,pieza,state,ID):
    OnPickTarget = None
    base = Graph.graph()
    tiempo_total = 0
    tiempo = time.time()
    if conveyor.Valid():
        conveyor.MoveJ(conveyor.Joints() + part_travel_mm)
        while conveyor.Valid():
            current_position = conveyor.Pose()[0, 3]  # Obtiene la posición actual del marco
            piece_position = pieza.PoseAbs()[1, 3]
            #print("Pieza Position: ", piece_position)
            #print("Current Position: ", current_position)
            # Verifica si la próxima posición excederá el límite de 2000
            next_position = current_position + part_travel_mm
            #print(next_position)
            if next_position > 1070:
                tiempo2 = time.time()
                tiempo_total = (tiempo2 - tiempo) + tiempo_total
                tiempo_total = round(tiempo_total,2)
                update('Banda ASRS',tiempo_total,ID,'Station_ASRS','Conveyor_ASRS')
                return(True,False)
            
            elif abs(current_position - pick_positionASRS) < tolerance and state==2:
                #print("\n==== ESTACION ASRS ====")
                OnPickTarget = True
                tiempo2 = time.time()
                tiempo_total = (tiempo2 - tiempo) + tiempo_total
                tiempo_total = round(tiempo_total,2)
                update('Banda ASRS',tiempo_total,ID,'Station_ASRS','Conveyor_ASRS')
                return(False,OnPickTarget)
            else:
                # Mueve la banda
                conveyor.MoveJ(conveyor.Joints() + part_travel_mm)

def MoveConveyor3(conveyor, part_travel_mm,pieza,ID):
    OnPickTarget = None
    tiempo_total = 0
    tiempo = time.time()
    if conveyor.Valid():
        conveyor.MoveJ(conveyor.Joints() + part_travel_mm)
        while conveyor.Valid():
            current_position = conveyor.Pose()[0, 3]  # Obtiene la posición actual del marco
            piece_position = pieza.PoseAbs()[0, 3]
            #print("Current Position: ", current_position)
            #print("Pieza Position: ", piece_position)

            # Verifica si la próxima posición excederá el límite de 2000
            next_position = current_position + part_travel_mm
            #print(next_position)
            if next_position > 1070:
                tiempo2 = time.time()
                tiempo_total = (tiempo2 - tiempo) + tiempo_total
                tiempo_total = round(tiempo_total,2)
                update('Banda Torno',tiempo_total,ID,'Station_Lathe','Conveyor_Lathe')
                return(True,False)
            elif abs(current_position - pick_positionTorno) < tolerance:
                #print("\n==== ESTACION TORNO ====")
                OnPickTarget = True
                tiempo2 = time.time()
                tiempo_total = (tiempo2 - tiempo) + tiempo_total
                tiempo_total = round(tiempo_total,2)
                update('Banda Torno',tiempo_total,ID,'Station_Lathe','Conveyor_Lathe')
                return(False,OnPickTarget)
            else:
                # Mueve la banda
                conveyor.MoveJ(conveyor.Joints() + part_travel_mm)

def MoveConveyor4(conveyor, part_travel_mm,pieza,ID):
    OnPickTarget = None
    tiempo_total = 0
    tiempo = time.time()
    if conveyor.Valid():
        conveyor.MoveJ(conveyor.Joints() + part_travel_mm)
        while conveyor.Valid():
            current_position = conveyor.Pose()[0, 3]  # Obtiene la posición actual del marco
            piece_position = pieza.PoseAbs()[0, 3] 
            #print("Current Position: ", current_position)
            #print("Pieza Position: ", piece_position)

            # Verifica si la próxima posición excederá el límite de 2000
            next_position = current_position + part_travel_mm
            if next_position > 2100:
                tiempo2 = time.time()
                tiempo_total = (tiempo2 - tiempo) + tiempo_total
                tiempo_total = round(tiempo_total,2)
                update('Banda Melling',tiempo_total,ID,'Station_Melling','Conveyor_Melling')
                return(True,False)
            elif abs(pick_positionFresado - current_position) <= tolerance:
                #print("\n==== ESTACION FRESADO ====")
                OnPickTarget = True
                tiempo2 = time.time()
                tiempo_total = (tiempo2 - tiempo) + tiempo_total
                tiempo_total = round(tiempo_total,2)
                update('Banda Melling',tiempo_total,ID,'Station_Melling','Conveyor_Melling')
                return(False,OnPickTarget)
            else:
                # Mueve la banda
                conveyor.MoveJ(conveyor.Joints() + part_travel_mm)

def ResetConveyorPosition(conveyor, resetFramePoint):
    if conveyor.Valid():
        conveyor.setJoints([resetFramePoint])
