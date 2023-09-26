# Type help("robolink") or help("robodk") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/index.html
# Note: It is not required to keep a copy of this file, your python script is saved with the station
from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
RDK = Robolink()

#This program reinitialize every mechanisms in the list to position 0
MECHANISM_LIST = ["Conv_Mech1","Conv_Mech2","Conv_Mech3","Conv_Mech4", "Curved_Conv_Mech", "Curved_Conv_Mech2", "Curved_Conv_Mech3", "Curved_Conv_Mech4"]

for i in range(len(MECHANISM_LIST)):
    MECHANISM_NAME=MECHANISM_LIST[i]
    mechanism = RDK.Item(MECHANISM_NAME,itemtype=ITEM_TYPE_ROBOT)
    if mechanism.Valid():
        mechanism.setJoints([0])



