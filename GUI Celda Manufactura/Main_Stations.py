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


def Run_Conveyors(current_frame,ID,state):

    # Station UR3
    if current_frame == 'Curva1':
        obj_list2 = frame_curve1.Childs()
        for item in obj_list2:
            #print("\nOn Curve 1")
            moveCurve(Conv_curved1, PART_ROTATION_ANGLE,'Banda UR3',ID,'Station_Inspection','Conveyor_Inspection')
            item.setParentStatic(frame_conv2)
            return('Conv2')
    
    if current_frame == 'Conv1':
        obj_list1 = frame_conv1.Childs()
        for item in obj_list1:
            #print("\nOn Conveyor 1")
            piezaPosition,OnPickTarget= MoveConveyor1(Conv_mechanism1,PART_TRAVEL_MM2,item,ID)
            if piezaPosition:
                item.setParentStatic(frame_curve1)
                ResetConveyorPosition(Conv_mechanism1, 0)
                return('Curva1')
            
            if OnPickTarget:  
                resetCurve(Conv_curved4, PART_ROTATION_ANGLE)
                return('Curva1')
    
    # Station ASRS
    if current_frame == 'Curva2':
        obj_list4 = frame_curve2.Childs()
        for item in obj_list4:
            #print("\nOn Curve 2")
            moveCurve(Conv_curved2, PART_ROTATION_ANGLE,'Banda ASRS',ID,'Station_ASRS','Conveyor_ASRS')
            item.setParentStatic(frame_conv3)
            return('Conv3')
        
    if current_frame == 'Conv2':
        obj_list3 = frame_conv2.Childs()

        for item in obj_list3:
            #print("\nOn Conveyor 2")
            piezaPosition,OnPickTarget= MoveConveyor2(Conv_mechanism2,PART_TRAVEL_MM2,item,state,ID)
            if piezaPosition:
                item.setParentStatic(frame_curve2)
                ResetConveyorPosition(Conv_mechanism2,0)
                return('Curva2')
            
            if OnPickTarget:  
                resetCurve(Conv_curved1, PART_ROTATION_ANGLE)
                return('Curva2')
    
    # Station Lathe
    if current_frame == 'Curva3':
        obj_list6 = frame_curve3.Childs()
        for item in obj_list6:
            #print("\nOn Curve 3")
            moveCurve(Conv_curved3, PART_ROTATION_ANGLE,'Banda Torno',ID,'Station_Lathe','Conveyor_Lathe')
            item.setParentStatic(frame_conv4)
            return('Conv4')
    
    if current_frame == 'Conv3':
        obj_list5 = frame_conv3.Childs()

        for item in obj_list5:
            #print("\nOn Conveyor 3")
            piezaPosition,OnPickTarget = MoveConveyor3(Conv_mechanism3, PART_TRAVEL_MM3, item,ID)
            if piezaPosition: # LLegó al fin de linea
                item.setParentStatic(frame_curve3)
                ResetConveyorPosition(Conv_mechanism3, 0)
                return('Curva3')
                        
            if OnPickTarget:  
                resetCurve(Conv_curved2, PART_ROTATION_ANGLE)
                return('Curva3')

    # Station Melling
    if current_frame == 'Curva4':
        obj_list8 = frame_curve4.Childs()
        for item in obj_list8:
            #print("\nOn Curve 4")
            moveCurve(Conv_curved4, PART_ROTATION_ANGLE,'Banda Melling',ID,'Station_Melling','Conveyor_Melling')
            item.setParentStatic(frame_conv1)
            return('Conv1')
        
    if current_frame == 'Conv4':
        obj_list7 = frame_conv4.Childs()
        
        for item in obj_list7:
            #print("\nOn Conveyor 4")
            piezaPosition, OnPickTarget = MoveConveyor4(Conv_mechanism4, PART_TRAVEL_MM4,item,ID)    
            if OnPickTarget:
                resetCurve(Conv_curved3, PART_ROTATION_ANGLE)
                return('Curva4')
            
            if piezaPosition:
                item.setParentStatic(frame_curve4)
                ResetConveyorPosition(Conv_mechanism4, 0)
                return('Curva4')
            

# Process to run Lathe Station
def Lathe_Section(ID,loc,piece,run):
    state = Run_Conveyors('Conv2',ID,0)

    if state == 'Curva2':
        state= Run_Conveyors(state,ID,0)
    if state == 'Conv3':
        state = Run_Conveyors(state,ID,0)
    if state == 'Curva3':
        if run == 1:
            Station_Lathe.Run(ID,loc, piece)
        
# Process to run Lathe Station
def Melling_Section(ID,run):
    state = Run_Conveyors('Conv3',ID,0)

    if state == 'Curva3':
        state= Run_Conveyors(state,ID,0)
    if state == 'Conv4':
        state = Run_Conveyors(state,ID,0)
    if state == 'Curva4':
        if run == 1:
            Station_Melling.Run(ID)

# Process to run Lathe Station
def Inspection_Section(ID,run):
    state = Run_Conveyors('Conv4',ID,0)

    if state == 'Curva4':
        state= Run_Conveyors(state,ID,0)
    if state == 'Conv1':
        state = Run_Conveyors(state,ID,0)
    if state == 'Curva1':
        if run == 1:
            Station_Inspection.Run(ID)

# Process to run Lathe Station
def ASRS_Section(ID,loc,action,run):
    state = Run_Conveyors('Conv1',ID,0)

    if state == 'Curva1':
        state= Run_Conveyors(state,ID,0)
    if state == 'Conv2':
        state = Run_Conveyors(state,ID,2)
    if state == 'Curva2':
        if run == 1:
            Station_ASRS.Run(ID,loc,action)


#Lathe_Section('EP1_2023_23_10_C2_H10_T7',1,'[1,3]','piece1')
#Melling_Section('EP1_2023_23_10_C2_H10_T7',1)
#Inspection_Section('EP1_2023_23_10_C2_H10_T7',1)
#ASRS_Section('EP1_2023_23_10_C2_H10_T7','[1,3]','Put',1)
#Run_Conveyors('Conv2','EP1_2023_5_11_C1_H17_T18',0)