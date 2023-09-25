# === Torno Objects ===
from Robot_Arms_Scripts import robotTorno, TornoGripper
from Robot_Arms_Scripts import goHome, getPiece, pickPiece, placePiece, dropPiece
from Robot_Arms_Scripts import HomeTargetTorno, PickTargetTorno, PlaceTargetTorno, frameConv3, LatheFrame

from Station_Scripts import DoorDisplacement, TornoPuerta, openDoor, closeDoor


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


for item in obj_list1:
    #print("\nOn Conveyor 1")
    #print(item.PoseAbs()) #If you want to see the Abs pos matrix of the object
    if item.PoseAbs()[0,3] < 0: #[0,3] refer to line 0 column 3 in the pos matrix, so the X position
        item.setParentStatic(frame_curve)

for item in obj_list2:
    #print("\nOn Curve 1")
    #print(item.PoseAbs()) #If you want to see the Abs pos matrix of the object
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

for item in obj_list8:
    print("\nOn Curve 4")
    print(item.PoseAbs()) 
    if item.PoseAbs()[0,3] < 2100 or item.PoseAbs()[1,3] < 260: 
        item.setParentStatic(frame_conv1)

