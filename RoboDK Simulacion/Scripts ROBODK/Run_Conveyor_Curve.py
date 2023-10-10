from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
RDK = Robolink()

#Set the travel of the conveyors for each iterations
PART_ROTATION_ANGLE = -30

#Declaration of the conveyor object
Conv_curved1 = RDK.Item('Curved_Conv_Mech',itemtype=ITEM_TYPE_ROBOT)
Conv_curved2 = RDK.Item('Curved_Conv_Mech2',itemtype=ITEM_TYPE_ROBOT)
Conv_curved3 = RDK.Item('Curved_Conv_Mech3',itemtype=ITEM_TYPE_ROBOT)
Conv_curved4 = RDK.Item('Curved_Conv_Mech4',itemtype=ITEM_TYPE_ROBOT)


#If the conveyor exist, move it to the declared value.
def moveCurve(curveConveyor, rotationAngle):
    #setSpeed(speed_linear, speed_joints, accel_linear, accel_joints), 
    #Must adjust to match the linear conveyors speed
    curveConveyor.setSpeed(7,7,7,7)
    if curveConveyor.Valid():
        curveConveyor.MoveJ(curveConveyor.Joints() + rotationAngle)
        start_time = time.time()
        counter = 1
        while curveConveyor.Valid() and counter < 3:
            curveConveyor.MoveJ(curveConveyor.Joints() + rotationAngle)
            counter += 1
    
        end_time = time.time()
        elapsed_time = end_time - start_time
        return elapsed_time

def resetCurve(curveConveyor, rotationAngle):
    curveConveyor.MoveJ(curveConveyor.Joints() - rotationAngle * 3)

#moveCurve(Conv_curved2, PART_ROTATION_ANGLE)