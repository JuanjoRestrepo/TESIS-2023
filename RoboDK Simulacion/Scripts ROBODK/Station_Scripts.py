from robodk import *      # RoboDK API
from robolink import *    # Robot toolbox
# Link to RoboDK
RDK = Robolink()

#Set the travel of the conveyors for each iterations
DoorDisplacement = 675

#Declaration of the conveyor object
TornoPuerta = RDK.Item('Mazak Lathe',itemtype=ITEM_TYPE_ROBOT)
FresadoPuerta = RDK.Item('Haas UMC-500',itemtype=ITEM_TYPE_ROBOT)

def openDoor(Station, DoorDisplacement):
    Station.MoveJ(Station.Joints() + DoorDisplacement)
    print(f"Puerta {Station} Abierta")

def closeDoor(Station, DoorDisplacement):
    Station.MoveJ(Station.Joints() - DoorDisplacement)
    print(f"Puerta {Station} Cerrada")

#If the conveyor exist, move it to the declared value.
#if TornoPuerta.Valid():
    #openDoor(TornoPuerta, DoorDisplacement)
    #closeDoor(TornoPuerta, DoorDisplacement)

#if FresadoPuerta.Valid():
    #openDoor(FresadoPuerta, -DoorDisplacement)
    #closeDoor(FresadoPuerta, -DoorDisplacement)