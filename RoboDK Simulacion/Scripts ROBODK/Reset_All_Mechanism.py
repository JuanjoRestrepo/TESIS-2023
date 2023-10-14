from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
RDK = Robolink()

#This program reinitialize every mechanisms in the list to position 0
MECHANISM_LIST = ["Conv_Mech1","Conv_Mech3","Conv_Mech4", "Curved_Conv_Mech", "Curved_Conv_Mech2", "Curved_Conv_Mech3", "Curved_Conv_Mech4"]

for i in range(len(MECHANISM_LIST)):
    MECHANISM_NAME=MECHANISM_LIST[i]
    mechanism = RDK.Item(MECHANISM_NAME,itemtype=ITEM_TYPE_ROBOT)
    
    mechanismConv2 = RDK.Item("Conv_Mech2",itemtype=ITEM_TYPE_ROBOT)
    if mechanism.Valid() and mechanismConv2.Valid():
        mechanism.setJoints([0])
        mechanismConv2.setJoints([960])
        

