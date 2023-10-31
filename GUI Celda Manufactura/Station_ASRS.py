# Import the Robot DK Library
from robolink import *
import time
import Graph
import Dashboard
from datetime import datetime


# DEFINE GRIPPERS FUNCTIONS
def gripper(action,RDK):
    Grip_Open = RDK.Item('Grip Open ASRS')
    Grip_Close = RDK.Item('Grip Close ASRS')

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

# DEFINE THE LOGIC TO GET A PIECE
def Get_Piece(Up,Piece,RDK,num,ID):
    #Connect to ASRS Robot
    velocidad = 100
    robot = RDK.Item('ASRS')
    Home = RDK.Item('Home ASRS')
    Band = RDK.Item('Put Band ASRS')

    base = Graph.graph()
    dash = Dashboard.dashboard()

    # Guardar el tiempo de inicio
    tiempo_inicio = time.time()

    # Open gripper
    gripper('O',RDK)
    robot.setSpeed(velocidad)

    # Secuence  to get the Piece
    robot.MoveJ(Home)
    robot.MoveJ(Up)

    # Close gripper
    tool = gripper('C',RDK)
    robot.setSpeed(velocidad)
    robot.MoveL(Piece)

    # Attach the piece
    tool.AttachClosest()

    # Secuence to put it in the Band
    robot.MoveL(Up)
    robot.MoveJ(Home)
    robot.MoveL(Band)

    # Detach the piece and go Home
    frame = RDK.Item('Frame_Conv2')
    dropPiece(tool, frame)
    

    # Open gripper
    tool = gripper('O',RDK)
    robot.setSpeed(velocidad)
    robot.MoveJ(Home)

    # Guardar el tiempo de finalización
    tiempo_fin = time.time()
    # Calcular el tiempo transcurrido
    tiempo_transcurrido = tiempo_fin - tiempo_inicio

    tiempo_transcurrido =  round(tiempo_transcurrido,2)

    # Actualización de la base y dashboard
    dash.Add_End(['ASRS',str(datetime.now()),tiempo_transcurrido,ID,'Exitoso'],'Ejecuciones Máquinas')
   
    if num == 1:
        base.create_relation_data('TIME_STATION',"time:"+str(tiempo_transcurrido),'order','station',ID,'Station_ASRS')
    else:
        tiempo = base.get_data_relation('order',ID,'station','Station_ASRS','TIME_STATION')
        tiempo = tiempo[1][0][0]
        nuevo_tiempo = int(tiempo) + tiempo_transcurrido
        base.update_data_relation(ID,'order','Station_ASRS','station',nuevo_tiempo,'TIME_STATION','time')

    return()

# DEFINE THE LOGIC TO PUT A PIECE
def Put_Piece(Down,Piece,RDK,num,ID):
    #Connect to ASRS Robot
    velocidad = 100
    robot = RDK.Item('ASRS')
    Home = RDK.Item('Home2')
    Band = RDK.Item('Get Band ASRS')

    base = Graph.graph()
    dash = Dashboard.dashboard()

    # Guardar el tiempo de inicio
    tiempo_inicio = time.time()

    # Open gripper
    gripper('O',RDK)
    robot.setSpeed(velocidad)

    # Secuence  to get the Piece
    robot.MoveJ(Home)
    robot.MoveJ(Band)

    # Close gripper
    tool = gripper('C',RDK)
    robot.setSpeed(velocidad)
    # Attach the piece
    tool.AttachClosest()

    # Secuence to put it in Table
    robot.MoveJ(Home)
    robot.MoveL(Down)
    robot.MoveL(Piece)

    # Detach the piece and go Home
    frame = RDK.Item('Table_Put')
    dropPiece(tool, frame)
    
    # Open gripper
    tool = gripper('O',RDK)
    robot.setSpeed(velocidad)
    robot.MoveL(Down)
    robot.MoveL(Home)

    # Guardar el tiempo de finalización
    tiempo_fin = time.time()
    # Calcular el tiempo transcurrido
    tiempo_transcurrido = tiempo_fin - tiempo_inicio

    # Actualización de la base y dashboard
    dash.Add_End(['ASRS',str(datetime.now()),tiempo_transcurrido,ID,'Exitoso'],'Ejecuciones Máquinas')
   
    if num == 1:
        base.create_relation_data('TIME_STATION',"time:"+str(tiempo_transcurrido),'order','station',ID,'Station_ASRS')
    else:
        tiempo = base.get_data_relation('order',ID,'station','Station_ASRS','TIME_STATION')
        tiempo = tiempo[1][0][0]
        nuevo_tiempo = int(tiempo) + tiempo_transcurrido
        base.update_data_relation(ID,'order','Station_ASRS','station',nuevo_tiempo,'TIME_STATION','time')

    return()

# THE MAIN PROCESS ( WE SEND THE TARGETS INFORMATION OF THE PIECE)
def Run(ID,loc,action,num):
    # Connect to DK
    RDK = Robolink() 

    if loc == '[1,1]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_AC[1,1]')
        Piece_Get = RDK.Item('Piece_AC[1,1]')
        Piece_Put = RDK.Item('PiecePutAC[1,1]')
        Up_Piece_Put = RDK.Item('UpPut_AC')
    elif loc == '[1,2]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_AC[1,2]')
        Piece_Get = RDK.Item('Piece_AC[1,2]')
        Piece_Put = RDK.Item('PiecePutAC[1,2]')
        Up_Piece_Put = RDK.Item('UpPut_AC')
    elif loc == '[1,3]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_EC[1,3]')
        Piece_Get = RDK.Item('Piece_EC[1,3]')
        Piece_Put = RDK.Item('PiecePutEC[1,3]')
        Up_Piece_Put = RDK.Item('UpPut_EC')
    elif loc == '[1,4]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_EC[1,4]')
        Piece_Get = RDK.Item('Piece_EC[1,4]')
        Piece_Put = RDK.Item('PiecePutEC[1,4]')
        Up_Piece_Put = RDK.Item('UpPut_EC')
    elif loc == '[1,5]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_EC[1,5]')
        Piece_Get = RDK.Item('Piece_EC[1,5]')
        Piece_Put = RDK.Item('PiecePutEC[1,5]')
        Up_Piece_Put = RDK.Item('UpPut_EC')

    elif loc == '[2,1]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_AC[2,1]')
        Piece_Get = RDK.Item('Piece_AC[2,1]')
        Piece_Put = RDK.Item('PiecePutAC[2,1]')
        Up_Piece_Put = RDK.Item('UpPut_AC')
    elif loc == '[2,2]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_AC[2,2]')
        Piece_Get = RDK.Item('Piece_AC[2,2]')
        Piece_Put = RDK.Item('PiecePutAC[2,2]')
        Up_Piece_Put = RDK.Item('UpPut_AC')
    elif loc == '[2,3]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_EC[2,3]')
        Piece_Get = RDK.Item('Piece_EC[2,3]')
        Piece_Put = RDK.Item('PiecePutEC[2,3]')
        Up_Piece_Put = RDK.Item('UpPut_EC')
    elif loc == '[2,4]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_EC[2,4]')
        Piece_Get = RDK.Item('Piece_EC[2,4]')
        Piece_Put = RDK.Item('PiecePutEC[2,4]')
        Up_Piece_Put = RDK.Item('UpPut_EC')
    elif loc == '[2,5]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_EC[2,5]')
        Piece_Get = RDK.Item('Piece_EC[2,5]')
        Piece_Put = RDK.Item('PiecePutEC[2,5]')
        Up_Piece_Put = RDK.Item('UpPut_EC')

    elif loc == '[3,1]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_AC[3,1]')
        Piece_Get = RDK.Item('Piece_AC[3,1]')
        Piece_Put = RDK.Item('PiecePutAC[3,1]')
        Up_Piece_Put = RDK.Item('UpPut_AC')
    elif loc == '[3,2]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_AC[3,2]')
        Piece_Get = RDK.Item('Piece_AC[3,2]')
        Piece_Put = RDK.Item('PiecePutAC[3,2]')
        Up_Piece_Put = RDK.Item('UpPut_AC')
    elif loc == '[3,3]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_EC[3,3]')
        Piece_Get = RDK.Item('Piece_EC[3,3]')
        Piece_Put = RDK.Item('PiecePutEC[3,3]')
        Up_Piece_Put = RDK.Item('UpPut_EC')
    elif loc == '[3,4]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_EC[3,4]')
        Piece_Get = RDK.Item('Piece_EC[3,4]')
        Piece_Put = RDK.Item('PiecePutEC[3,4]')
        Up_Piece_Put = RDK.Item('UpPut_EC')
    elif loc == '[3,5]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_EC[3,5]')
        Piece_Get = RDK.Item('Piece_EC[3,5]')
        Piece_Put = RDK.Item('PiecePutEC[3,5]')
        Up_Piece_Put = RDK.Item('UpPut_EC')

    elif loc == '[4,1]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_AC[4,1]')
        Piece_Get = RDK.Item('Piece_AC[4,1]')
        Piece_Put = RDK.Item('PiecePutAC[4,1]')
        Up_Piece_Put = RDK.Item('UpPut_AC')
    elif loc == '[4,2]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_AC[4,2]')
        Piece_Get = RDK.Item('Piece_AC[4,2]')
        Piece_Put = RDK.Item('PiecePutAC[4,2]')
        Up_Piece_Put = RDK.Item('UpPut_AC')
    elif loc == '[4,3]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_EC[4,3]')
        Piece_Get = RDK.Item('Piece_EC[4,3]')
        Piece_Put = RDK.Item('PiecePutEC[4,3]')
        Up_Piece_Put = RDK.Item('UpPut_EC')
    elif loc == '[4,4]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_EC[4,4]')
        Piece_Get = RDK.Item('Piece_EC[4,4]')
        Piece_Put = RDK.Item('PiecePutEC[4,4]')
        Up_Piece_Put = RDK.Item('UpPut_EC')
    elif loc == '[4,5]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_EC[4,5]')
        Piece_Get = RDK.Item('Piece_EC[4,5]')
        Piece_Put = RDK.Item('PiecePutEC[4,5]')
        Up_Piece_Put = RDK.Item('UpPut_EC')

    elif loc == '[5,1]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_AC[5,1]')
        Piece_Get = RDK.Item('Piece_AC[5,1]')
        Piece_Put = RDK.Item('PiecePutAC[5,1]')
        Up_Piece_Put = RDK.Item('UpPut_AC')
    elif loc == '[5,2]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_AC[5,2]')
        Piece_Get = RDK.Item('Piece_AC[5,2]')
        Piece_Put = RDK.Item('PiecePutAC[5,2]')
        Up_Piece_Put = RDK.Item('UpPut_AC')
    elif loc == '[5,3]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_EC[5,3]')
        Piece_Get = RDK.Item('Piece_EC[5,3]')
        Piece_Put = RDK.Item('PiecePutEC[5,3]')
        Up_Piece_Put = RDK.Item('UpPut_EC')
    elif loc == '[5,4]':
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_EC[5,4]')
        Piece_Get = RDK.Item('Piece_EC[5,4]')
        Piece_Put = RDK.Item('PiecePutEC[5,4]')
        Up_Piece_Put = RDK.Item('UpPut_EC')
    else:
        # Obtener el objeto del objetivo
        Up_Piece = RDK.Item('Up_EC[5,5]')
        Piece_Get = RDK.Item('Piece_EC[5,5]')
        Piece_Put = RDK.Item('PiecePutEC[5,5]')
        Up_Piece_Put = RDK.Item('UpPut_EC')

    if action == 'Get':
        Get_Piece(Up_Piece,Piece_Get,RDK,num,ID)

    else:
        Put_Piece(Up_Piece_Put,Piece_Put,RDK,num,ID)
    return()

#Run('AP2_2023_23_9_C2_H17_T30','[1,3]','Put',2)




