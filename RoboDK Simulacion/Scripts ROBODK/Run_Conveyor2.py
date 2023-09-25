# Type help("robolink") or help("robodk") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/index.html
# Note: It is not required to keep a copy of this file, your python script is saved with the station
from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
RDK = Robolink()

#Set the travel of the conveyors for each iterations
PART_TRAVEL_MM = 400

#Declaration of the conveyor object
Conv_mechanism2 = RDK.Item('Conv_Mech2',itemtype=ITEM_TYPE_ROBOT)

#If the conveyor exist, move it to the declared value.
if Conv_mechanism2.Valid():
    Conv_mechanism2.MoveJ(Conv_mechanism2.Joints() + PART_TRAVEL_MM)

