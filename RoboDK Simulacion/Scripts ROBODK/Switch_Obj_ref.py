# =========== Torno ===========
from Robot_Arms_Scripts import robotTorno, TornoGripper, frameMazakLathe, frameConv3
from Robot_Arms_Scripts import getPiece, pickPiece, goHome, placePiece, dropPiece
from Robot_Arms_Scripts import HomeTargetTorno, PickTargetTorno, PlaceTargetTorno

# Fresado 
from Robot_Arms_Scripts import robotFresado, FresadoGripper
from Robot_Arms_Scripts import HomeTargetFresado, PickTargetFresado, PlaceTargetFresado
from Robot_Arms_Scripts import frameConv4, frameCNC

import Torno_Station_Scripts
from Torno_Station_Scripts import TornoPuerta, FresadoPuerta, DoorDisplacement


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
pick_position = 1085.485  # Posición objetivo del brazo del Torno
tolerance = 0.01
pick_position_fresado = 1998.584 # Posición objetivo del brazo del Fresado


def activateTornoStation():
    # Calling Actions
    getPiece(robotTorno, PickTargetTorno)
    time.sleep(1)

    pickPiece(TornoGripper)
    time.sleep(1)

    goHome(robotTorno, HomeTargetTorno)
    time.sleep(1)
    
    if Torno_Station_Scripts.TornoPuerta.Valid():
        Torno_Station_Scripts.openDoor(TornoPuerta, DoorDisplacement)
        time.sleep(1)
        placePiece(robotTorno, PlaceTargetTorno)
        time.sleep(1)
        dropPiece(TornoGripper, frameMazakLathe)
        time.sleep(1)
        goHome(robotTorno, HomeTargetTorno)
        Torno_Station_Scripts.closeDoor(TornoPuerta, DoorDisplacement)
        print("Torneando Pieza...")
        time.sleep(5)
        print("Pieza Terminada!!!")
        Torno_Station_Scripts.openDoor(TornoPuerta, DoorDisplacement)
        time.sleep(1)
        placePiece(robotTorno, PlaceTargetTorno)
        time.sleep(1)
        pickPiece(TornoGripper)
        goHome(robotTorno, HomeTargetTorno)
        Torno_Station_Scripts.closeDoor(TornoPuerta, DoorDisplacement)
        time.sleep(1)
        getPiece(robotTorno, PickTargetTorno)
        time.sleep(1)
        dropPiece(TornoGripper, frameConv3)
        time.sleep(1)
        goHome(robotTorno, HomeTargetTorno)


def activateFresadoStation():
    getPiece(robotFresado, PickTargetFresado)
    time.sleep(1)

    pickPiece(FresadoGripper)
    time.sleep(1)

    goHome(robotFresado, HomeTargetFresado)
    time.sleep(10)
    if Torno_Station_Scripts.FresadoPuerta.Valid():
        Torno_Station_Scripts.openDoor(FresadoPuerta, DoorDisplacement)
        time.sleep(1)
        placePiece(robotFresado, PlaceTargetFresado)
        time.sleep(1)
        dropPiece(FresadoGripper, frameCNC)
        time.sleep(1)
        goHome(robotFresado, HomeTargetFresado)
        Torno_Station_Scripts.closeDoor(FresadoPuerta, -DoorDisplacement)
        print("Fresando Pieza...")
        time.sleep(5)
        print("Pieza Terminada!!!")
        Torno_Station_Scripts.openDoor(FresadoPuerta, DoorDisplacement)
        time.sleep(1)
        placePiece(robotFresado, PlaceTargetFresado)
        time.sleep(1)
        pickPiece(FresadoGripper)
        goHome(robotFresado, HomeTargetFresado)
        Torno_Station_Scripts.closeDoor(FresadoPuerta, -DoorDisplacement)
        time.sleep(1)
        getPiece(robotFresado, PickTargetFresado)
        time.sleep(1)
        dropPiece(FresadoGripper, frameConv4)
        time.sleep(1)
        goHome(robotFresado, HomeTargetFresado)
        

for item in obj_list1:
    #print("\n===== On Conveyor 1 =====")
    #print(item.PoseAbs()) #If you want to see the Abs pos matrix of the object
    if item.PoseAbs()[0,3] < 0: #[0,3] refer to line 0 column 3 in the pos matrix, so the X position
        item.setParentStatic(frame_curve)

for item in obj_list2:
    #print("\n===== On Curve 1 =====")
    #print(item.PoseAbs()) #If you want to see the Abs pos matrix of the object
    if item.PoseAbs()[1,3] > 900: #[1,3] refer to line 1 column 3 in the pos matrix, so the Y position
        item.setParentStatic(frame_conv2)

for item in obj_list3:
    #print("\n===== On Conveyor 2 =====")
    #print(item.PoseAbs()) 
    if item.PoseAbs()[1,3] > 2920: 
        item.setParentStatic(frame_curve2)

for item in obj_list4:
    #print("\n===== On Curve 2 =====")
    #print(item.PoseAbs()) 
    if item.PoseAbs()[0,3] > -170: 
        item.setParentStatic(frame_conv3)

for item in obj_list5:
    #print("\n===== On Conveyor 3 =====")
    #print(item.PoseAbs()) 
    if item.PoseAbs()[0,3] > 1800: 
        item.setParentStatic(frame_curve3)
    elif abs(item.PoseAbs()[0,3] - pick_position ) < tolerance:
        print("\nRECOGIENDO PIEZA EN TORNO!!!!!")
        activateTornoStation()
    

for item in obj_list6:
    #print("\n===== On Curve 3 =====")
    #print(item.PoseAbs()) 
    if item.PoseAbs()[1,3] < 3200: 
        item.setParentStatic(frame_conv4)

for item in obj_list7:
    #print("\n===== On Conveyor 4 =====")
    ##print(item.PoseAbs()) 
    if item.PoseAbs()[1,3] < 1200: 
        item.setParentStatic(frame_curve4)
    elif abs(item.PoseAbs()[1,3] - pick_position_fresado ) < tolerance:
        print("\nRECOGIENDO PIEZA EN FRESADO!!!!!")
        activateFresadoStation()

for item in obj_list8:
    print("\n===== On Curve 4 =====")
    print(item.PoseAbs()) 
    if item.PoseAbs()[0,3] < 2100 or item.PoseAbs()[1,3] < 260: 
        item.setParentStatic(frame_conv1)

