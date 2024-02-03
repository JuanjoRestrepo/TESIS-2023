from robolink import *
import time
import Dashboard
import Graph
from datetime import datetime

# DEFINE GRIPPERS FUNCTIONS
def gripper(action,RDK):
    Grip_Open = RDK.Item('Grip Open UR3')
    Grip_Close = RDK.Item('Grip Close UR3')

    # Close
    if action =='C':
        Grip_Open.setVisible(False)
        Grip_Close.setVisible(True)
        return(Grip_Close)
    # Open
    if action == 'O':
        Grip_Open.setVisible(True)
        Grip_Close.setVisible(False)
        return(Grip_Open)

def dropPiece(robotTool, drop_frame):
    robotTool.DetachClosest()
    # Obtiene el objeto que fue desconectado (el objeto previamente adjunto)
    detached_object = robotTool.Childs()[0]
    # Establece "Frame_Conv3" como el padre del objeto previamente adjunto
    detached_object.setParentStatic(drop_frame)

def Run (ID):
    # Conectar a RoboDK
    RDK = Robolink()
    dash = Dashboard.dashboard()
    base = Graph.graph()

    # VARIABLES A UTILIZAR
    robot = RDK.Item('Robot UR3')
    Home = RDK.Item('Home UR3')
    Piece = RDK.Item('Piece UR3')
    Up_Piece = RDK.Item('Up Piece UR3')
    Put_Piece = RDK.Item('Put Piece UR3')
    Step1 = RDK.Item('1')
    Step2 = RDK.Item('2')
    Step3 = RDK.Item('3')
    Step4 = RDK.Item('4')
    Step5 = RDK.Item('5')
    Start = RDK.Item('Start')
    SetPiece = RDK.Item('set Piece UR3')

    
    # Guardar el tiempo de inicio
    tiempo_inicio = time.time()

    # Verificar si el robot existe
    if robot.Valid():
        # Establecer la velocidad del robot en mm/s (ajusta según tus necesidades)
        velocidad = 100  # por ejemplo, 100 mm/s
        robot.setSpeed(velocidad)

        # Logica de inspección
        gripper('O',RDK)
        robot.setSpeed(velocidad)

        # Secuencia para recoger la pieza
        robot.MoveL(Home)
        robot.MoveL(Piece)
        tool = gripper('C',RDK)
        tool.AttachClosest()
        robot.setSpeed(velocidad)

        # Lleva la pieza a la mesa
        robot.MoveL(Home)
        robot.MoveL(Up_Piece)
        robot.MoveL(SetPiece)
        frame = RDK.Item('Table_Put UR3')
        dropPiece(tool, frame)

        # Empieza a hacer la inspección
        robot.MoveL(Start)
        robot.MoveL(Step1)
        robot.MoveL(Step2)
        robot.MoveL(Step3)
        robot.MoveL(Step4)
        robot.MoveL(Step5)
        robot.MoveL(Step4)
        robot.MoveL(Step3)
        robot.MoveL(Step2)
        robot.MoveL(Step1)
        robot.MoveJ(SetPiece)

        # Vuelve a dejar la pieza en la banda
        tool.AttachClosest()
        robot.MoveL(Start)
        robot.MoveL(Home)
        robot.MoveL(Piece)
        frame = RDK.Item('Frame_Conv1')
        dropPiece(tool, frame)
        gripper('O',RDK)
        robot.setSpeed(velocidad)
        robot.MoveL(Home)

    # Guardar el tiempo de finalización
    tiempo_fin = time.time()
    # Calcular el tiempo transcurrido
    tiempo_transcurrido = tiempo_fin - tiempo_inicio

    tiempo_transcurrido =  round(tiempo_transcurrido,2)

    # Actualización de la base y dashboard
    dash.Add_End(['Robot UR3',str(datetime.now()),tiempo_transcurrido,ID,'Exitoso'],'Ejecuciones Máquinas')
    station = base.exist_relation('station','TIME_STATION','Station_Inspection')
    machine = base.exist_relation('machine','TIME_MACHINE','Robot_UR3')

    if station == 0:
        base.create_relation_data('TIME_STATION',"time:"+str(tiempo_transcurrido),'order','station',ID,'Station_Inspection')
    else:
        tiempo = base.get_data_relation('order',ID,'station','Station_Inspection','TIME_STATION')
        tiempo = tiempo[1][0][0]
        nuevo_tiempo = float(tiempo) + tiempo_transcurrido
        base.update_data_relation(ID,'order','Station_Inspection','station',nuevo_tiempo,'TIME_STATION','time')

    if machine == 0:
        base.create_relation_data('TIME_MACHINE',"time:"+str(tiempo_transcurrido),'order','machine',ID,'Robot_UR3')
    else:
        tiempo = base.get_data_relation('order',ID,'machine','Robot_UR3','TIME_MACHINE')
        tiempo = tiempo[1][0][0]
        nuevo_tiempo = float(tiempo) + tiempo_transcurrido
        base.update_data_relation(ID,'order','Robot_UR3','machine',nuevo_tiempo,'TIME_MACHINE','time')
    return()

#Run('AP2_2023_23_9_C2_H17_T30',2)