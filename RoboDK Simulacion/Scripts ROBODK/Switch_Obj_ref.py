# === ROBODK Libraries ===
from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
RDK = Robolink()

# === Run Conveyor Libraries ===
from Run_Conveyor import MoveConveyor, ResetConveyorPosition
from Run_Conveyor import Conv_mechanism1, Conv_mechanism2, Conv_mechanism3, Conv_mechanism4
from Run_Conveyor import PART_TRAVEL_MM1, PART_TRAVEL_MM2, PART_TRAVEL_MM3, PART_TRAVEL_MM4


# === Run Curve Conveyors ===
from Run_Conveyor_Curve import moveCurve, resetCurve
from Run_Conveyor_Curve import Conv_curved1, Conv_curved2, Conv_curved3, Conv_curved4
from Run_Conveyor_Curve import PART_ROTATION_ANGLE

# === Robot Arms Libraries ===

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



# === Frames Declaration ===
frame_conv1 = RDK.Item('Frame_Conv1',itemtype=ITEM_TYPE_FRAME)
frame_conv2 = RDK.Item('Frame_Conv2',itemtype=ITEM_TYPE_FRAME)
frame_conv3 = RDK.Item('Frame_Conv3',itemtype=ITEM_TYPE_FRAME)
frame_conv4 = RDK.Item('Frame_Conv4',itemtype=ITEM_TYPE_FRAME)

frame_curve = RDK.Item('Frame_CurveConv',itemtype=ITEM_TYPE_FRAME)
frame_curve2 = RDK.Item('Frame_CurveConv2',itemtype=ITEM_TYPE_FRAME)
frame_curve3 = RDK.Item('Frame_CurveConv3',itemtype=ITEM_TYPE_FRAME)
frame_curve4 = RDK.Item('Frame_CurveConv4',itemtype=ITEM_TYPE_FRAME)

# === Child frames ===
obj_list1 = frame_conv1.Childs()
obj_list2 = frame_curve.Childs()

obj_list3 = frame_conv2.Childs()
obj_list4 = frame_curve2.Childs()

obj_list5 = frame_conv3.Childs()
obj_list6 = frame_curve3.Childs()

obj_list7 = frame_conv4.Childs()
obj_list8 = frame_curve4.Childs()


# === Pick Targets ===
pick_position = 1084.779 #1085.485  CUBOS
tolerance = 0.05
pick_positionFresado = 1998.3 # Cubos 1998.520
pick_positionUR3 = 1030.046 # 1030.046 Cubos


# === Robot Scripts ===
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
        time.sleep(1)
        placePiece(robotFresado, PlaceTargetFresado)
        pickPiece(FresadoGripper)
        time.sleep(1)
        goHome(robotFresado, HomeTargetFresado)
        closeDoor(FresadoPuerta, -DoorDisplacement)
        time.sleep(0.5)
        getPiece(robotFresado, PickTargetFresado)
        dropPiece(FresadoGripper, frameConv4)
        time.sleep(0.5)
        goHome(robotFresado, HomeTargetFresado)
        print("Pieza en Conveyor 4")
        time.sleep(1)

# Activar Robot UR3
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

# === Convs and Curves Times ===
endTimeConv1 = None
endTimeConv2 = None
endTimeConv3 = None
endTimeConv4 = None

endTimeCurve1 = None
endTimeCurve2 = None
endTimeCurve3 = None
endTimeCurve4 = None

for item in obj_list1:
    print("\nOn Conveyor 1")
    endTimeConv1 = MoveConveyor(Conv_mechanism1, PART_TRAVEL_MM1)
    print(item.PoseAbs())
    #time.sleep(60)
    if item.PoseAbs()[0,3] < 0 or item.PoseAbs()[1,3] > 250: #[0,3] refer to line 0 column 3 in the pos matrix, so the X position
        item.setParentStatic(frame_curve)
        ResetConveyorPosition(Conv_mechanism1, 0)
    else:
        ResetConveyorPosition(Conv_mechanism1, 0)
        
    FinalTimeSection4 = endTimeConv1
    endTimeConv1 = 0
    print(f"Tiempo acumulado en Banda 1: {FinalTimeSection4} segundos")

for item in obj_list2:
    print("\nOn Curve 1")
    endTimeCurve1 = moveCurve(Conv_curved1, PART_ROTATION_ANGLE)
    if item.PoseAbs()[1,3] > 900: #[1,3] refer to line 1 column 3 in the pos matrix, so the Y position
        item.setParentStatic(frame_conv2)
        resetCurve(Conv_curved1, PART_ROTATION_ANGLE)
    else:
        resetCurve(Conv_curved1, PART_ROTATION_ANGLE)
    
    FinalTimeCurve1 = endTimeCurve1
    endTimeCurve1 = 0
    print(f"Tiempo acumulado en Curva 1: {FinalTimeCurve1} segundos")

for item in obj_list3:
    print("\nOn Conveyor 2")
    endTimeConv2 = MoveConveyor(Conv_mechanism2, PART_TRAVEL_MM2)
    if item.PoseAbs()[1,3] > 3000:
        item.setParentStatic(frame_curve2)
        ResetConveyorPosition(Conv_mechanism2, 1000)

    FinalTimeSection1 = endTimeConv2
    endTimeConv2 = 0
    print(f"Tiempo acumulado en Banda 2: {FinalTimeSection1} segundos")

for item in obj_list4:
    print("\nOn Curve 2")
    endTimeCurve2 = moveCurve(Conv_curved2, PART_ROTATION_ANGLE)
    if item.PoseAbs()[0,3] >= -16: 
        item.setParentStatic(frame_conv3)
        resetCurve(Conv_curved2, PART_ROTATION_ANGLE)

    FinalTimeCurve2 = endTimeCurve2
    endTimeCurve2 = 0
    print(f"Tiempo acumulado en Curva 2: {FinalTimeCurve2} segundos")

for item in obj_list5:
    print("\nOn Conveyor 3")
    endTimeConv3 = MoveConveyor(Conv_mechanism3, PART_TRAVEL_MM3)
    if item.PoseAbs()[0,3] > 2080:
        item.setParentStatic(frame_curve3)
        ResetConveyorPosition(Conv_mechanism3, 0)

    FinalTimeSection2 = endTimeConv3
    endTimeConv3 = 0
    print(f"Tiempo acumulado en Banda 3: {FinalTimeSection2} segundos")
    
for item in obj_list6:
    print("\nOn Curve 3")
    endTimeCurve3 = moveCurve(Conv_curved3, PART_ROTATION_ANGLE)
    if item.PoseAbs()[0,3] >= 2700: 
        item.setParentStatic(frame_conv4)
        resetCurve(Conv_curved3, PART_ROTATION_ANGLE)

    FinalTimeCurve3 = endTimeCurve3
    endTimeCurve3 = 0
    print(f"Tiempo acumulado en Curva 3: {FinalTimeCurve3} segundos")

for item in obj_list7:
    print("\nOn Conveyor 4")
    endTimeConv4 = MoveConveyor(Conv_mechanism4, PART_TRAVEL_MM4)
    if item.PoseAbs()[0,3] > 2750: 
        item.setParentStatic(frame_curve4)
        ResetConveyorPosition(Conv_mechanism4, 0)
    #elif abs(item.PoseAbs()[0,3] - pick_position ) < tolerance or abs(item.PoseAbs()[0,3] - pick_position ) < 125:
    #    print("\n==== ESTACION TORNO ====")
    #    activateRobotTorno()

    FinalTimeSection3 = endTimeConv4
    endTimeConv4 = 0
    print(f"Tiempo acumulado en Banda 4: {FinalTimeSection3} segundos")
    

for item in obj_list8:
    print("\nOn Curve 4")
    endTimeCurve4 = moveCurve(Conv_curved4, PART_ROTATION_ANGLE)
    print(item.PoseAbs())
    time.sleep(30)
    if item.PoseAbs()[0,3] >= 1900: 
        item.setParentStatic(frame_conv1)
        resetCurve(Conv_curved4, PART_ROTATION_ANGLE)

    FinalTimeCurve4 = endTimeCurve4
    endTimeCurve4 = 0
    print(f"Tiempo acumulado en Curva 4: {FinalTimeCurve4} segundos")
    

