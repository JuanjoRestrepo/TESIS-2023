from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
import time
import Dashboard
import Graph
from datetime import datetime
RDK = Robolink()

#Set the travel of the conveyors for each iterations
PART_ROTATION_ANGLE = -30

#Declaration of the conveyor object
Conv_curved1 = RDK.Item('Curved_Conv_Mech',itemtype=ITEM_TYPE_ROBOT)
Conv_curved2 = RDK.Item('Curved_Conv_Mech2',itemtype=ITEM_TYPE_ROBOT)
Conv_curved3 = RDK.Item('Curved_Conv_Mech3',itemtype=ITEM_TYPE_ROBOT)
Conv_curved4 = RDK.Item('Curved_Conv_Mech4',itemtype=ITEM_TYPE_ROBOT)

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

    

#If the conveyor exist, move it to the declared value.
def moveCurve(curveConveyor, rotationAngle,banda,ID,station,machine):
    #setSpeed(speed_linear, speed_joints, accel_linear, accel_joints), 
    #Must adjust to match the linear conveyors speed
    curveConveyor.setSpeed(7,7,7,7)
    tiempo_total = 0
    tiempo = time.time()
    if curveConveyor.Valid():
        curveConveyor.MoveJ(curveConveyor.Joints() + rotationAngle)
        counter = 1
        while curveConveyor.Valid() and counter < 3:
            curveConveyor.MoveJ(curveConveyor.Joints() + rotationAngle)
            counter += 1
        tiempo2 = time.time()
        tiempo_total = (tiempo2 - tiempo) + tiempo_total
        tiempo_total = round(tiempo_total,2)
        update(banda,tiempo_total,ID,station,machine)

def resetCurve(curveConveyor, rotationAngle):
    curveConveyor.MoveJ(curveConveyor.Joints() - rotationAngle * 3)

#moveCurve(Conv_curved2, PART_ROTATION_ANGLE)