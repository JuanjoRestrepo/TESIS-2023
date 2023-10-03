from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
import time

RDK = Robolink()

#Set the travel of the conveyors for each iterations
PART_TRAVEL_MM1 = 100
PART_TRAVEL_MM2 = 100
PART_TRAVEL_MM3 = 100
PART_TRAVEL_MM4 = 100

#Declaration of the conveyor object
Conv_mechanism1 = RDK.Item('Conv_Mech1',itemtype=ITEM_TYPE_ROBOT)
Conv_mechanism2 = RDK.Item('Conv_Mech2',itemtype=ITEM_TYPE_ROBOT)
Conv_mechanism3 = RDK.Item('Conv_Mech3',itemtype=ITEM_TYPE_ROBOT)
Conv_mechanism4 = RDK.Item('Conv_Mech4',itemtype=ITEM_TYPE_ROBOT)

def MoveConveyor(conveyor, part_travel_mm):
    if conveyor.Valid():
        conveyor.MoveJ(conveyor.Joints() + part_travel_mm)
        start_time = time.time()
        while conveyor.Valid():
            current_position = conveyor.Pose()[0, 3]  # Obtiene la posición actual del marco

            # Verifica si la próxima posición excederá el límite de 2000
            next_position = current_position + part_travel_mm
            print(next_position)
            if next_position > 2100:
                # Si la próxima posición excede el límite, establece la posición en exactamente 2000
                break  # Sal del bucle
            else:
                # Mueve la banda
                conveyor.MoveJ(conveyor.Joints() + part_travel_mm)

            # Calcula el tiempo transcurrido desde el inicio
            elapsed_time = time.time() - start_time

        end_time = time.time()
        elapsed_time = end_time - start_time
        #print(f"Tiempo total: {elapsed_time} segundos")
        return elapsed_time

def ResetConveyorPosition(conveyor, resetFramePoint):
    #This program reinitialize every mechanisms in the list to position 0
    if conveyor.Valid():
        conveyor.setJoints([resetFramePoint])

#MoveConveyor(Conv_mechanism1, PART_TRAVEL_MM1)
#ResetConveyorPosition(Conv_mechanism1, 0)

