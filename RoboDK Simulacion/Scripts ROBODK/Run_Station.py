from Run_Conveyor import MoveConveyor2, MoveConveyor3, ResetConveyorPosition
from Run_Conveyor import Conv_mechanism2, Conv_mechanism3
from Run_Conveyor import PART_TRAVEL_MM2, PART_TRAVEL_MM3


from Run_Conveyor_Curve import moveCurve, resetCurve

# === ROBODK Libraries ===
from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
RDK = Robolink()

# === Frames Declaration ===
frame_conv1 = RDK.Item('Frame_Conv1',itemtype=ITEM_TYPE_FRAME)
frame_conv2 = RDK.Item('Frame_Conv2',itemtype=ITEM_TYPE_FRAME)
frame_conv3 = RDK.Item('Frame_Conv3',itemtype=ITEM_TYPE_FRAME)
frame_conv4 = RDK.Item('Frame_Conv4',itemtype=ITEM_TYPE_FRAME)

frame_curve1 = RDK.Item('Frame_CurveConv',itemtype=ITEM_TYPE_FRAME)
frame_curve2 = RDK.Item('Frame_CurveConv2',itemtype=ITEM_TYPE_FRAME)
frame_curve3 = RDK.Item('Frame_CurveConv3',itemtype=ITEM_TYPE_FRAME)
frame_curve4 = RDK.Item('Frame_CurveConv4',itemtype=ITEM_TYPE_FRAME)

# === Child frames ===
obj_list1 = frame_conv1.Childs()
obj_list2 = frame_curve1.Childs()

obj_list3 = frame_conv2.Childs()
obj_list4 = frame_curve2.Childs()

obj_list5 = frame_conv3.Childs()
obj_list6 = frame_curve3.Childs()

obj_list7 = frame_conv4.Childs()
obj_list8 = frame_curve4.Childs()


#Set the travel of the conveyors for each iterations
PART_ROTATION_ANGLE = -30

#Declaration of the conveyor object
Conv_curved1 = RDK.Item('Curved_Conv_Mech',itemtype=ITEM_TYPE_ROBOT)
Conv_curved2 = RDK.Item('Curved_Conv_Mech2',itemtype=ITEM_TYPE_ROBOT)
Conv_curved3 = RDK.Item('Curved_Conv_Mech3',itemtype=ITEM_TYPE_ROBOT)
Conv_curved4 = RDK.Item('Curved_Conv_Mech4',itemtype=ITEM_TYPE_ROBOT)


def runLatheSection():
    FinalTimeConv2 = 0
    FinalTimeCurve2 = 0
    FinalTimeConv3 = 0
    
    for item in obj_list3:
        print("\nOn Conveyor 2")
        endTimeConv2, piezaPosition = MoveConveyor2(Conv_mechanism2, PART_TRAVEL_MM2, item)
        if piezaPosition > 3000:
            print("Llegué a Curva 2")
            item.setParentStatic(frame_curve2)
            ResetConveyorPosition(Conv_mechanism2, 960)
        FinalTimeConv2 = endTimeConv2
        endTimeConv2 = 0
        print("Time Conveyor 2: ", FinalTimeConv2)

    for item in obj_list4:
        print("\nOn Curve 2")
        endTimeCurve2 = moveCurve(Conv_curved2, PART_ROTATION_ANGLE)
        if item.PoseAbs()[0, 3] >= -16:
            item.setParentStatic(frame_conv3)
            resetCurve(Conv_curved2, PART_ROTATION_ANGLE)
        FinalTimeCurve2 = endTimeCurve2
        endTimeCurve2 = 0
        print(f"Tiempo acumulado en Curva 2: {FinalTimeCurve2} segundos")

    #for item in obj_list5:
    #    print("\nOn Conveyor 3")
        #print(item.PoseAbs()[0, 3] )
    #    endTimeConv3, piezaPosition = MoveConveyor3(Conv_mechanism3, PART_TRAVEL_MM3, item)
    #    if piezaPosition > 2080:
    #        item.setParentStatic(frame_curve3)
    #        ResetConveyorPosition(Conv_mechanism3, 0)

    #    FinalTimeConv3 = endTimeConv3
    #    endTimeConv3 = 0
    #    print(f"Tiempo acumulado en Banda 3:  {FinalTimeConv3} segundos")

    #FinalTimeLatheSection = FinalTimeConv2 + FinalTimeCurve2 + FinalTimeConv3
    #print(f"Tiempo total en la sección del torno: {FinalTimeLatheSection} segundos")

runLatheSection()
