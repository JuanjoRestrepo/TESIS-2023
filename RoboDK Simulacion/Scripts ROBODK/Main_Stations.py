# Import Programs Conveyors
from Run_Conveyor import MoveConveyor1, MoveConveyor2, MoveConveyor3, MoveConveyor4, ResetConveyorPosition
from Run_Conveyor import Conv_mechanism1, Conv_mechanism2, Conv_mechanism3, Conv_mechanism4
from Run_Conveyor import PART_TRAVEL_MM1, PART_TRAVEL_MM2, PART_TRAVEL_MM3, PART_TRAVEL_MM4
from Run_Conveyor_Curve import moveCurve, resetCurve

# Import Programs Stations
import Station_Lathe
import Station_ASRS
import Station_Inspection
import Station_Melling

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

#Set the travel of the conveyors for each iterations
PART_ROTATION_ANGLE = -30

#Declaration of the conveyor object
Conv_curved1 = RDK.Item('Curved_Conv_Mech',itemtype=ITEM_TYPE_ROBOT)
Conv_curved2 = RDK.Item('Curved_Conv_Mech2',itemtype=ITEM_TYPE_ROBOT)
Conv_curved3 = RDK.Item('Curved_Conv_Mech3',itemtype=ITEM_TYPE_ROBOT)
Conv_curved4 = RDK.Item('Curved_Conv_Mech4',itemtype=ITEM_TYPE_ROBOT)


def Run_Conveyors(current_frame):
    if current_frame == 'Curva1':
        obj_list2 = frame_curve1.Childs()
        return('Conv2')
        
    if current_frame == 'Curva2':
        obj_list4 = frame_curve2.Childs()
        for item in obj_list4:
            print("\nOn Curve 2")
            endTimeCurve2 = moveCurve(Conv_curved2, PART_ROTATION_ANGLE)
            print('Pieza posición:',item.PoseAbs()[0, 3])
            if item.PoseAbs()[0, 3] <= -35:
                item.setParentStatic(frame_conv3)
                resetCurve(Conv_curved2, PART_ROTATION_ANGLE)
                return('Conv3')
        
    if current_frame == 'Curva3':
        obj_list6 = frame_curve3.Childs()

        return('Conv4')
        
    if current_frame == 'Curva4':
        obj_list8 = frame_curve4.Childs()

        return('Conv1')
        
    if current_frame == 'Conv1':
        obj_list1 = frame_conv1.Childs()
        return('Curva1')
        
    if current_frame == 'Conv2':
        obj_list3 = frame_conv2.Childs()

        for item in obj_list3:
            print("\nOn Conveyor 2")
            state= MoveConveyor2(Conv_mechanism2,PART_TRAVEL_MM2,item)
            if state:
                item.setParentStatic(frame_curve2)
                ResetConveyorPosition(Conv_mechanism2, 960)
                return('Curva2')
        
    if current_frame == 'Conv3':
        obj_list5 = frame_conv3.Childs()

        for item in obj_list5:
            print("\nOn Conveyor 3")
            piezaPosition,OnPickTarget = MoveConveyor3(Conv_mechanism3, PART_TRAVEL_MM3, item)
            if piezaPosition: # LLegó al fin de linea
                item.setParentStatic(frame_curve3)
                ResetConveyorPosition(Conv_mechanism3, 0)
                return('Curva3')
                        
            if OnPickTarget:  
                return('Curva3')
        
    if current_frame == 'Conv4':
        obj_list7 = frame_conv4.Childs()

        return('Curva4')
        
    

# Process to run Lathe Station
def Lathe_Section(ID,num,loc,piece):
    state = Run_Conveyors('Conv2')

    if state == 'Curva2':
        state= Run_Conveyors(state)
    if state == 'Conv3':
        state = Run_Conveyors(state)
    if state == 'Curva3':
        Station_Lathe.Run(ID, num, loc, piece)


# Process to run Melling Station
def Melling_Section(ID,num,loc,piece):
    state = Run_Conveyors('Conv3')

    if state == 'Curv3':
        state= Run_Conveyors(state)
    if state == 'Conv4':
        state = Run_Conveyors(state)
    if state == 'Curva4':
        Station_Lathe.Run(ID, num, loc, piece)

# Process to run Inspection Station
def Inspection_Section(ID,num,loc,piece):
    state = Run_Conveyors('Conv4')

    if state == 'Curva4':
        state= Run_Conveyors(state)
    if state == 'Conv1':
        state = Run_Conveyors(state)
    if state == 'Curva1':
        Station_Lathe.Run(ID, num, loc, piece)

#Process to run ASRS Section
def ASRS_Section(ID,num,loc,piece):
    state = Run_Conveyors('Conv1')

    if state == 'Curva1':
        state= Run_Conveyors(state)
    if state == 'Conv2':
        state = Run_Conveyors(state)
    if state == 'Curva2':
        Station_Lathe.Run(ID, num, loc, piece)



Lathe_Section('EP1_2023_23_10_C2_H10_T7',1,'[1,3]','piece1')