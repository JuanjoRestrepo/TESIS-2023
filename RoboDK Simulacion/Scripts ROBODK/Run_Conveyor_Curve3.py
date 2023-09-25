# Type help("robolink") or help("robodk") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/index.html
# Note: It is not required to keep a copy of this file, your python script is saved with the station
from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
RDK = Robolink()

#Set the travel of the conveyors for each iterations
PART_ROTATION_ANGLE = -30

#Declaration of the conveyor object
Conv_curved3 = RDK.Item('Curved_Conv_Mech3',itemtype=ITEM_TYPE_ROBOT)

#setSpeed(speed_linear, speed_joints, accel_linear, accel_joints), 
#Must adjust to match the linear conveyors speed
Conv_curved3.setSpeed(7,7,7,7)

#If the conveyor exist, move it to the declared value.
if Conv_curved3.Valid():
    Conv_curved3.MoveJ(Conv_curved3.Joints() + PART_ROTATION_ANGLE)