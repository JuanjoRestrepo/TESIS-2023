from robolink import *
from robodk import *
#import Dashboard
import time
#import Graph
from datetime import datetime

# DEFINE GRIPPERS FUNCTIONS
def gripper(action,RDK):
    Grip_Open = RDK.Item('Grip Open Lathe')
    Grip_Close = RDK.Item('Grip Close Lathe')

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

def create_Piece(RDK,piece,new_piece):
    pieza_original = RDK.Item(new_piece)
    pieza_vieja = RDK.Item(piece)
    lathe= RDK.Item('Mazak Lathe Base torno')

    pieza_original.Copy()
    object_copy1 = RDK.Paste(paste_to=lathe)
    object_copy1.setName('piece')
    object_copy1.setPose(transl(-352.259,-145.960,-85.819))

    pieza_vieja.setVisible(False)
    # Actualizar la pantalla de RoboDK
    RDK.Render()
    return()


def Run(loc,piece):
    # Conectar a RoboDK
    RDK = Robolink()
    #dash = Dashboard.dashboard()
    #base = Graph.graph()
    
    # VARIABLES A UTILIZAR
    robot = RDK.Item('Mitsubishi Torno')
    Home = RDK.Item('Home_Robot_Torno')
    Pick = RDK.Item('Pick_lathe') # Target 4
    Step1 = RDK.Item('Lathe1') # Target 5
    Step2 = RDK.Item('Lathe2') # Target 6
    Step3 = RDK.Item('Lathe3') # Target 7
    Step3_Finish = RDK.Item('Lathe3_Finish')
    Pick_Finish = RDK.Item('Pick_lathe_Finish')
    Door_Open = RDK.Item('Open Door Lathe')
    Door_Close = RDK.Item('Close Door Lathe')

    # Guardar el tiempo de inicio
    tiempo_inicio = time.time()
    tiempo_robot_total = 0
    tiempo_lathe_total = 0

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
        tiempo_lathe = time.time()
        Door_Open.RunProgram()
        time.sleep(7)
        tiempo_lathe2 = time.time()
        tiempo_lathe_total = (tiempo_lathe2 - tiempo_lathe) + tiempo_lathe_total

        # Robot Lathe
        tiempo_robot = time.time()
        robot.MoveJ(Step3)
        frame = RDK.Item('Mazak Lathe Base torno')
        gripper('O',RDK)
        robot.setSpeed(velocidad)
        dropPiece(tool, frame)
        robot.MoveJ(Step2)
        tiempo_robot2 = time.time()
        tiempo_robot_total = (tiempo_robot2 - tiempo_robot) + tiempo_robot_total

        # Cierra la puerta
        # Lathe
        tiempo_lathe = time.time()
        Door_Close.RunProgram()
        time.sleep(18)
        create_Piece(RDK,loc,piece)
        time.sleep(5)
        

        # Abre la puerta
        Door_Open.RunProgram()
        time.sleep(7)
        tiempo_lathe2 = time.time()
        tiempo_lathe_total = (tiempo_lathe2 - tiempo_lathe) + tiempo_lathe_total

        # Recoge la pieza y la pone en la banda
        # Robot Lathe
        tiempo_robot = time.time()
        robot.MoveJ(Step3_Finish)
        tool = gripper('C',RDK)
        tool.AttachClosest()
        robot.setSpeed(velocidad)
        robot.MoveJ(Step2)
        Door_Close.RunProgram()
        robot.MoveJ(Step1)
        robot.MoveJ(Home)
        robot.MoveJ(Pick_Finish)
        frame = RDK.Item('Frame_Conv3')
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
    tiempo_lathe_total= round(tiempo_lathe_total,2)

    print(f"tiempo transcurrido: {tiempo_transcurrido} seg")
    print(f"tiempo Robot Total: {tiempo_robot_total} seg" )
    print(f"tiempo Lathe Total: {tiempo_lathe_total} seg" )

    # Actualización de la base y dashboard
    #dash.Add_End(['Robot Mitsubishi Torno',str(datetime.now()),tiempo_robot_total,ID,'Exitoso'],'Ejecuciones')
    #dash.Add_End(['CNC Torno',str(datetime.now()),tiempo_lathe_total,ID,'Exitoso'],'Ejecuciones')

    #if num == 1:
        # Station
    #    base.create_relation_data('TIME_STATION',"time:"+str(tiempo_transcurrido),'order','station',ID,'Station_Lathe')

        # Robot Lathe
    #    base.create_relation_data('TIME_MACHINE',"time:"+str(tiempo_robot_total),'order','machine',ID,'Robot_Lathe')

        # CNC Lathe
    #    base.create_relation_data('TIME_MACHINE',"time:"+str(tiempo_lathe_total),'order','machine',ID,'CNC_Lathe')
    #else:
        # Station
    #    tiempo = base.get_data_relation('order',ID,'station','Station_Lathe','TIME_STATION')
    #    tiempo = tiempo[1][0][0]
    #    nuevo_tiempo = int(tiempo) + tiempo_transcurrido
    #    base.update_data_relation(ID,'order','Station_Lathe','station',nuevo_tiempo,'TIME_STATION','time')

        # Robot Lathe
    #    tiempo = base.get_data_relation('order',ID,'machine','Robot_Lathe','TIME_MACHINE')
    #    tiempo = tiempo[1][0][0]
    #    nuevo_tiempo = int(tiempo) + tiempo_robot_total
    #    base.update_data_relation(ID,'order','Robot_Lathe','machine',nuevo_tiempo,'TIME_MACHINE','time')

        # CNC Lathe
    #    tiempo = base.get_data_relation('order',ID,'machine','CNC_Lathe','TIME_MACHINE')
    #    tiempo = tiempo[1][0][0]
    #    nuevo_tiempo = int(tiempo) + tiempo_lathe_total
    #    base.update_data_relation(ID,'order','CNC_Lathe','machine',nuevo_tiempo,'TIME_MACHINE','time')
    
    #return(tiempo_transcurrido,tiempo_lathe_total,tiempo_robot_total)
    

#print(Run('AP2_2023_23_9_C2_H17_T30',2,'ffff','Piece1'))

#Run('ffff','Piece1')



