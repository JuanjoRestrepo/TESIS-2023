# === Torno Objects ===
from Robot_Arms_Scripts import robotTorno, TornoGripper
from Robot_Arms_Scripts import goHome, getPiece, pickPiece, placePiece, dropPiece
from Robot_Arms_Scripts import HomeTargetTorno, PickTargetTorno, PlaceTargetTorno, frameConv3, LatheFrame

from Station_Scripts import DoorDisplacement, TornoPuerta, FresadoPuerta, openDoor, closeDoor


# === Fresado Objects ===
from Robot_Arms_Scripts import robotFresado, FresadoGripper
from Robot_Arms_Scripts import HomeTargetFresado, PickTargetFresado, PlaceTargetFresado, frameConv4, CNCFrame


# === UR3  Objects ===
from Robot_Arms_Scripts import robotUR3, UR3Gripper, scanPiece, DeskUR3Frame, frameConv1
from Robot_Arms_Scripts import HomeUR3, PickUR3, PlaceUR3, Scan1, Scan2, Scan3, Scan4, Scan5

# === ROBODK Libraries ===
from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
RDK = Robolink()

#Declaration of the frames
frame_conv1 = RDK.Item('Frame_Conv1',itemtype=ITEM_TYPE_FRAME)
frame_conv2 = RDK.Item('Frame_Conv2',itemtype=ITEM_TYPE_FRAME)
frame_conv3 = RDK.Item('Frame_Conv3',itemtype=ITEM_TYPE_FRAME)
frame_conv4 = RDK.Item('Frame_Conv4',itemtype=ITEM_TYPE_FRAME)

frame_curve = RDK.Item('Frame_CurveConv',itemtype=ITEM_TYPE_FRAME)
frame_curve2 = RDK.Item('Frame_CurveConv2',itemtype=ITEM_TYPE_FRAME)
frame_curve3 = RDK.Item('Frame_CurveConv3',itemtype=ITEM_TYPE_FRAME)
frame_curve4 = RDK.Item('Frame_CurveConv4',itemtype=ITEM_TYPE_FRAME)

#Declaration of the child frames
obj_list1 = frame_conv1.Childs()
obj_list2 = frame_curve.Childs()

obj_list3 = frame_conv2.Childs()
obj_list4 = frame_curve2.Childs()

obj_list5 = frame_conv3.Childs()
obj_list6 = frame_curve3.Childs()

obj_list7 = frame_conv4.Childs()
obj_list8 = frame_curve4.Childs()


# Variables de estado
pick_position = 1085.485  # Posición objetivo del brazo del robot
tolerance = 0.02
pick_positionFresado = 1998.520
pick_positionUR3 = 1830.221 #1030.219 cuando los cubos estan con reset

# Activar Robot Torno
def activateRobotTorno():
    # Calling Actions
    getPiece(robotTorno, PickTargetTorno)
    pickPiece(TornoGripper)
    time.sleep(0.5)
    goHome(robotTorno, HomeTargetTorno)
    time.sleep(1)
    if TornoPuerta.Valid():
        openDoor(TornoPuerta, DoorDisplacement)
        time.sleep(1)
        placePiece(robotTorno, PlaceTargetTorno)
        time.sleep(1)
        dropPiece(TornoGripper, LatheFrame)
        time.sleep(0.5)
        goHome(robotTorno, HomeTargetTorno)
        closeDoor(TornoPuerta, DoorDisplacement)
        print("Torneando Pieza...")
        time.sleep(5)

        print("Pieza Finalizada!!")
        openDoor(TornoPuerta, DoorDisplacement)
        placePiece(robotTorno, PlaceTargetTorno)
        pickPiece(TornoGripper)
        goHome(robotTorno, HomeTargetTorno)
        closeDoor(TornoPuerta, DoorDisplacement)
        time.sleep(0.5)
        getPiece(robotTorno, PickTargetTorno)
        dropPiece(TornoGripper, frameConv3)
        time.sleep(0.5)
        goHome(robotTorno, HomeTargetTorno)
        print("Pieza en Conveyor 3")
        time.sleep(1)


# Activar Robot Fresado
def activateRobotFresado():
    # Calling Actions
    getPiece(robotFresado, PickTargetFresado)
    pickPiece(FresadoGripper)
    time.sleep(0.5)
    goHome(robotFresado, HomeTargetFresado)
    time.sleep(1)
    if FresadoPuerta.Valid():
        openDoor(FresadoPuerta, -DoorDisplacement)
        time.sleep(1)
        placePiece(robotFresado, PlaceTargetFresado)
        time.sleep(1)
        dropPiece(FresadoGripper, CNCFrame)
        time.sleep(0.5)
        goHome(robotFresado, HomeTargetFresado)
        closeDoor(FresadoPuerta, -DoorDisplacement)
        print("Fresando Pieza...")
        time.sleep(5)

        print("Pieza Finalizada!!")
        openDoor(FresadoPuerta, -DoorDisplacement)
        placePiece(robotFresado, PlaceTargetFresado)
        pickPiece(FresadoGripper)
        goHome(robotFresado, HomeTargetFresado)
        closeDoor(FresadoPuerta, -DoorDisplacement)
        time.sleep(0.5)
        getPiece(robotFresado, PickTargetFresado)
        dropPiece(FresadoGripper, frameConv4)
        time.sleep(0.5)
        goHome(robotFresado, HomeTargetFresado)
        print("Pieza en Conveyor 4")
        time.sleep(1)


def activateUR3():
    getPiece(robotUR3, PickUR3)
    time.sleep(1)
    pickPiece(UR3Gripper)
    time.sleep(0.5)
    goHome(robotUR3, HomeUR3)
    time.sleep(1)
    placePiece(robotUR3, PlaceUR3)
    time.sleep(1)
    dropPiece(UR3Gripper, DeskUR3Frame)
    time.sleep(1)

    scanPiece(robotUR3, Scan1)
    time.sleep(1)
    scanPiece(robotUR3, Scan2)
    time.sleep(1)
    scanPiece(robotUR3, Scan3)
    time.sleep(1)
    scanPiece(robotUR3, Scan2)
    time.sleep(1)
    scanPiece(robotUR3, Scan1)
    time.sleep(1)
    scanPiece(robotUR3, Scan4)
    time.sleep(1)
    scanPiece(robotUR3, Scan5)
    time.sleep(1)
    scanPiece(robotUR3, Scan4)
    time.sleep(1)
    scanPiece(robotUR3, Scan1)
    time.sleep(1)
    print("Pieza Escaneada Correctamente!!")
    time.sleep(1)

    placePiece(robotUR3, PlaceUR3)
    time.sleep(1)
    pickPiece(UR3Gripper)
    time.sleep(1)
    goHome(robotUR3, HomeUR3)
    time.sleep(1)
    getPiece(robotUR3, PickUR3)
    time.sleep(1)
    dropPiece(UR3Gripper, frameConv1)
    time.sleep(1)
    goHome(robotUR3, HomeUR3)
    print("Finished")

for item in obj_list1:
    print("\nOn Conveyor 1")
    print(item.PoseAbs()) #If you want to see the Abs pos matrix of the object
    print(f"ErrorPosUR3: {abs(item.PoseAbs()[0,3] - pick_positionUR3)}")
    if item.PoseAbs()[0,3] < 0: #[0,3] refer to line 0 column 3 in the pos matrix, so the X position
        item.setParentStatic(frame_curve)
    elif abs(item.PoseAbs()[0,3] - pick_positionUR3) < tolerance:
        print("\n==== UR3 PICKING ====")
        activateUR3()

for item in obj_list2:
    print("\nOn Curve 1")
    print(item.PoseAbs()) #If you want to see the Abs pos matrix of the object
    if item.PoseAbs()[1,3] > 900: #[1,3] refer to line 1 column 3 in the pos matrix, so the Y position
        item.setParentStatic(frame_conv2)

for item in obj_list3:
    #print("\nOn Conveyor 2")
    #print(item.PoseAbs()) 
    if item.PoseAbs()[1,3] > 2920: 
        item.setParentStatic(frame_curve2)

for item in obj_list4:
    #print("\nOn Curve 2")
    #print(item.PoseAbs()) 
    if item.PoseAbs()[0,3] > -170: 
        item.setParentStatic(frame_conv3)

for item in obj_list5:
    print("\nOn Conveyor 3")
    print(item.PoseAbs()) 
    print(f"Error: {abs(item.PoseAbs()[0,3] - pick_position )}")
    if item.PoseAbs()[0,3] > 1800: 
        item.setParentStatic(frame_curve3)
    elif abs(item.PoseAbs()[0,3] - pick_position ) < tolerance:
        print("\n==== ESTACION TORNO ====")
        activateRobotTorno()
    
for item in obj_list6:
    #print("\nOn Curve 3")
    #print(item.PoseAbs()) 
    if item.PoseAbs()[1,3] < 3200: 
        item.setParentStatic(frame_conv4)

for item in obj_list7:
    print("\nOn Conveyor 4")
    print(item.PoseAbs()) 
    if item.PoseAbs()[1,3] < 1200: 
        item.setParentStatic(frame_curve4)
    elif abs(item.PoseAbs()[1,3] - pick_positionFresado) < tolerance:
        print("\n==== ESTACION FRESADO ====")
        activateRobotFresado()

for item in obj_list8:
    print("\nOn Curve 4")
    print(item.PoseAbs()) 
    if item.PoseAbs()[0,3] < 2100 or item.PoseAbs()[1,3] < 260: 
        item.setParentStatic(frame_conv1)

