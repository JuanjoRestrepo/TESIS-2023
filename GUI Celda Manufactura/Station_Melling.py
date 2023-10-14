from robolink import *
import Graph
import Dashboard
import time
from datetime import datetime

# DEFINE GRIPPERS FUNCTIONS
def gripper(action,RDK):
    Grip_Open = RDK.Item('Grip Open Melling')
    Grip_Close = RDK.Item('Grip Close Melling')

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

def Run(ID,num):
    # Conectar a RoboDK
    RDK = Robolink()
    dash = Dashboard.dashboard()
    base = Graph.graph()
    
    # VARIABLES A UTILIZAR
    robot = RDK.Item('Mitsubishi Fresado')
    Home = RDK.Item('Home_Robot_Fresado')
    Pick = RDK.Item('Pick_Robot_Fresado')
    Place = RDK.Item('Place_Robot_Fresado')
    Step1 = RDK.Item('Fresado1')
    Step2 = RDK.Item('Fresado2')
    Door_Open = RDK.Item('Open Melling')
    Door_Close = RDK.Item('Close Melling')

    # Guardar el tiempo de inicio
    tiempo_inicio = time.time()
    tiempo_robot_total = 0
    tiempo_melling_total = 0

    # Verificar si el robot existe
    if robot.Valid():
        # Establecer la velocidad del robot en mm/s (ajusta según tus necesidades)
        velocidad = 100  # por ejemplo, 100 mm/s
        robot.setSpeed(velocidad)

        # Logica de Poner la pieza en Lathe
        # Robot Lathe
        tiempo_robot = time.time()
        gripper('O',RDK)
        robot.setSpeed(velocidad)
        robot.MoveJ(Home)
        robot.MoveJ(Pick)
        tool = gripper('C',RDK)
        tool.AttachClosest()
        robot.setSpeed(velocidad)
        robot.MoveJ(Home)
        robot.MoveJ(Step1)
        robot.MoveJ(Step2)
        tiempo_robot2 = time.time()
        tiempo_robot_total = (tiempo_robot2 - tiempo_robot) + tiempo_robot_total


        # Abre la puerta
        # Lathe
        tiempo_melling = time.time()
        Door_Open.RunProgram()
        time.sleep(5)
        tiempo_melling2 = time.time()
        tiempo_melling_total = (tiempo_melling2 - tiempo_melling) + tiempo_melling_total

        # Robot Lathe
        tiempo_robot = time.time()
        robot.MoveL(Place)
        frame = RDK.Item('Melling')
        gripper('O',RDK)
        robot.setSpeed(velocidad)
        dropPiece(tool, frame)
        robot.MoveL(Step2)
        tiempo_robot2 = time.time()
        tiempo_robot_total = (tiempo_robot2 - tiempo_robot) + tiempo_robot_total

        # Cierra la puerta
        # Lathe
        tiempo_melling = time.time()
        Door_Close.RunProgram()
        time.sleep(8)
        #LOGICA DE CAMBIO DE PIEZA

        # Abre la puerta
        Door_Open.RunProgram()
        time.sleep(5)
        tiempo_melling2 = time.time()
        tiempo_melling_total = (tiempo_melling2 - tiempo_melling) + tiempo_melling_total

        # Recoge la pieza y la pone en la banda
        # Robot Lathe
        tiempo_robot = time.time()
        robot.MoveL(Place)
        tool = gripper('C',RDK)
        tool.AttachClosest()
        robot.setSpeed(velocidad)
        robot.MoveL(Step2)
        Door_Close.RunProgram()
        robot.MoveJ(Step1)
        robot.MoveJ(Home)
        robot.MoveJ(Pick)
        frame = RDK.Item('Frame_Conv4')
        dropPiece(tool, frame)
        gripper('O',RDK)
        robot.setSpeed(velocidad)
        robot.MoveJ(Home)
        tiempo_robot2 = time.time()
        tiempo_robot_total = (tiempo_robot2 - tiempo_robot) + tiempo_robot_total
    
    # Guardar el tiempo de finalización
    tiempo_fin = time.time()
    # Calcular el tiempo transcurrido
    tiempo_transcurrido = tiempo_fin - tiempo_inicio

    tiempo_transcurrido =  round(tiempo_transcurrido,2)
    tiempo_robot_total = round(tiempo_robot_total,2)
    tiempo_melling_total = round(tiempo_melling_total,2)

    # Actualización de la base y dashboard
    dash.Add_End(['Robot Mitsubishi Melling',str(datetime.now()),tiempo_robot_total,ID,'Exitoso'],'Ejecuciones')
    dash.Add_End(['CNC Melling',str(datetime.now()),tiempo_melling_total,ID,'Exitoso'],'Ejecuciones')

    if num == 1:
        # Station
        base.create_relation_data('TIME_STATION',"time:"+str(tiempo_transcurrido),'order','station',ID,'Station_Melling')

        # Robot Lathe
        base.create_relation_data('TIME_MACHINE',"time:"+str(tiempo_robot_total),'order','machine',ID,'Robot_Melling')

        # CNC Lathe
        base.create_relation_data('TIME_MACHINE',"time:"+str(tiempo_melling_total),'order','machine',ID,'CNC_Melling')
    else:
        # Station
        tiempo = base.get_data_relation('order',ID,'station','Station_Melling','TIME_STATION')
        tiempo = tiempo[1][0][0]
        nuevo_tiempo = int(tiempo) + tiempo_transcurrido
        base.update_data_relation(ID,'order','Station_Melling','station',nuevo_tiempo,'TIME_STATION','time')

        # Robot Lathe
        tiempo = base.get_data_relation('order',ID,'machine','Robot_Melling','TIME_MACHINE')
        tiempo = tiempo[1][0][0]
        nuevo_tiempo = int(tiempo) + tiempo_robot_total
        base.update_data_relation(ID,'order','Robot_Melling','machine',nuevo_tiempo,'TIME_MACHINE','time')

        # CNC Lathe
        tiempo = base.get_data_relation('order',ID,'machine','CNC_Melling','TIME_MACHINE')
        tiempo = tiempo[1][0][0]
        nuevo_tiempo = int(tiempo) + tiempo_melling_total
        base.update_data_relation(ID,'order','CNC_Melling','machine',nuevo_tiempo,'TIME_MACHINE','time')
    
    return(tiempo_transcurrido,tiempo_melling_total,tiempo_robot_total)
    

#print(Run('AP2_2023_23_9_C2_H17_T30',1))
