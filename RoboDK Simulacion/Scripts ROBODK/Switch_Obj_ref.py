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
    print(item.PoseAbs()) #If you want to see the Abs pos matrix of the object
    #print(f"ErrorPosUR3: {abs(item.PoseAbs()[0,3] - pick_positionUR3)}")
    endTimeConv1 = MoveConveyor(Conv_mechanism1, PART_TRAVEL_MM1)
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
    #print(item.PoseAbs()) #If you want to see the Abs pos matrix of the object
    endTimeCurve1 = moveCurve(Conv_curved1, PART_ROTATION_ANGLE)
    if item.PoseAbs()[1,3] > 900: #[1,3] refer to line 1 column 3 in the pos matrix, so the Y position
        item.setParentStatic(frame_conv2)
        resetCurve(Conv_curved1, PART_ROTATION_ANGLE)
    
    FinalTimeCurve1 = endTimeCurve1
    endTimeCurve1 = 0
    print(f"Tiempo acumulado en Curva 1: {FinalTimeCurve1} segundos")

for item in obj_list3:
    print("\nOn Conveyor 2")
    #print(item.PoseAbs())
    endTimeConv2 = MoveConveyor(Conv_mechanism2, PART_TRAVEL_MM2)
    if item.PoseAbs()[1,3] > 2920:
        item.setParentStatic(frame_curve2)
        ResetConveyorPosition(Conv_mechanism2, 1000)
    else:
        ResetConveyorPosition(Conv_mechanism2, 1000)

    FinalTimeSection1 = endTimeConv2
    endTimeConv2 = 0
    print(f"Tiempo acumulado en Banda 2: {FinalTimeSection1} segundos")


for item in obj_list4:
    print("\nOn Curve 2")
    #print(item.PoseAbs()) 
    endTimeCurve2 = moveCurve(Conv_curved2, PART_ROTATION_ANGLE)
    if item.PoseAbs()[0,3] > -170: 
        item.setParentStatic(frame_conv3)
        resetCurve(Conv_curved2, PART_ROTATION_ANGLE)
    
    FinalTimeCurve2 = endTimeCurve2
    endTimeCurve2 = 0
    print(f"Tiempo acumulado en Curva 2: {FinalTimeCurve2} segundos")

for item in obj_list5:
    print("\nOn Conveyor 3")
    print(item.PoseAbs()) 
    #print(f"Error: {abs(item.PoseAbs()[0,3] - pick_position )}")
    endTimeConv3 = MoveConveyor(Conv_mechanism3, PART_TRAVEL_MM3)
    if item.PoseAbs()[0,3] > 2020:
        print("STOP!")
        item.setParentStatic(frame_curve3)
        ResetConveyorPosition(Conv_mechanism3, 0)

    FinalTimeSection2 = endTimeConv3
    endTimeConv3 = 0
    print(f"Tiempo acumulado en Banda 3: {FinalTimeSection2} segundos")
    
for item in obj_list6:
    print("\nOn Curve 3")
    #print(item.PoseAbs())
    endTimeCurve3 = moveCurve(Conv_curved3, PART_ROTATION_ANGLE)
    if item.PoseAbs()[1,3] < 3200: 
        item.setParentStatic(frame_conv4)
        resetCurve(Conv_curved3, PART_ROTATION_ANGLE)

    FinalTimeCurve3 = endTimeCurve3
    endTimeCurve3 = 0
    print(f"Tiempo acumulado en Curva 3: {FinalTimeCurve3} segundos")

for item in obj_list7:
    print("\nOn Conveyor 4")
    #print(item.PoseAbs()) 
    endTimeConv4 = MoveConveyor(Conv_mechanism4, PART_TRAVEL_MM4)
    if item.PoseAbs()[1,3] < 1200: 
        item.setParentStatic(frame_curve4)
        ResetConveyorPosition(Conv_mechanism4, 0)

    FinalTimeSection3 = endTimeConv4
    endTimeConv4 = 0
    print(f"Tiempo acumulado en Banda 4: {FinalTimeSection3} segundos")

for item in obj_list8:
    print("\nOn Curve 4")
    #print(item.PoseAbs())
    endTimeCurve4 = moveCurve(Conv_curved4, PART_ROTATION_ANGLE) 
    if item.PoseAbs()[0,3] < 2100 or item.PoseAbs()[1,3] < 260: 
        item.setParentStatic(frame_conv1)
        resetCurve(Conv_curved4, PART_ROTATION_ANGLE)

    FinalTimeCurve4 = endTimeCurve4
    endTimeCurve4 = 0
    print(f"Tiempo acumulado en Curva 4: {FinalTimeCurve4} segundos")

