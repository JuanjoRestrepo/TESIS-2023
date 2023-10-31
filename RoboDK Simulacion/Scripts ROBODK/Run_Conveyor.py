from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
import time

RDK = Robolink()

#Set the travel of the conveyors for each iterations
PART_TRAVEL_MM1 = 105
PART_TRAVEL_MM2 = 20
PART_TRAVEL_MM3 = 25
PART_TRAVEL_MM4 = 25

#Declaration of the conveyor object
Conv_mechanism1 = RDK.Item('Conv_Mech1',itemtype=ITEM_TYPE_ROBOT)
Conv_mechanism2 = RDK.Item('Conv_Mech2',itemtype=ITEM_TYPE_ROBOT)
Conv_mechanism3 = RDK.Item('Conv_Mech3',itemtype=ITEM_TYPE_ROBOT)
Conv_mechanism4 = RDK.Item('Conv_Mech4',itemtype=ITEM_TYPE_ROBOT)

frameConv3 = RDK.Item('Frame_Conv3')
LatheFrame = RDK.Item('Lathe')

# === Pick Targets ===
pick_positionTorno = 1025.0
tolerance = 15
pick_positionFresado = 975.0
pick_positionASRS = 1920.0

toleranceUR3 = 26
pick_positionUR3 = 875.0
    


def MoveConveyor2(conveyor, part_travel_mm, pieza):
    OnPickTarget = None
    if conveyor.Valid():
        conveyor.MoveJ(conveyor.Joints() + part_travel_mm)
        while conveyor.Valid():
            current_position = conveyor.Pose()[0, 3]  # Obtiene la posición actual del marco
            piece_position = pieza.PoseAbs()[1, 3]
            print("Pieza Position: ", piece_position)
            print("Current Position: ", current_position)
            # Verifica si la próxima posición excederá el límite de 2000
            next_position = current_position + part_travel_mm
            #print(next_position)
            if next_position > 2050:
                return(True)
            
            else:
                # Mueve la banda
                conveyor.MoveJ(conveyor.Joints() + part_travel_mm)


def MoveConveyor3(conveyor, part_travel_mm, pieza):
    OnPickTarget = None
    if conveyor.Valid():
        conveyor.MoveJ(conveyor.Joints() + part_travel_mm)
        while conveyor.Valid():
            current_position = conveyor.Pose()[0, 3]  # Obtiene la posición actual del marco
            piece_position = pieza.PoseAbs()[0, 3]
            print("Current Position: ", current_position)
            print("Pieza Position: ", piece_position)

            # Verifica si la próxima posición excederá el límite de 2000
            next_position = current_position + part_travel_mm
            #print(next_position)
            if next_position > 2100:
                return(True,False)
            elif abs(current_position - pick_positionTorno) < tolerance:
                print("\n==== ESTACION TORNO ====")
                OnPickTarget = True
                return(False,OnPickTarget)
            else:
                # Mueve la banda
                conveyor.MoveJ(conveyor.Joints() + part_travel_mm)

            

def MoveConveyor4(conveyor, part_travel_mm, pieza):
    OnPickTarget = None
    if conveyor.Valid():
        conveyor.MoveJ(conveyor.Joints() + part_travel_mm)
        start_time = time.time()
        while conveyor.Valid():
            current_position = conveyor.Pose()[0, 3]  # Obtiene la posición actual del marco
            piece_position = pieza.PoseAbs()[1, 3] 
            print("Pieza Position: ", piece_position)
            print(f"Error {abs(current_position - pick_positionFresado)}")

            # Verifica si la próxima posición excederá el límite de 2000
            next_position = current_position + part_travel_mm
            if next_position > 2100:
                # Si la próxima posición excede el límite, establece la posición en exactamente 2000
                break  # Sal del bucle
            elif abs(current_position - pick_positionFresado) <= tolerance:
                print("\n==== ESTACION FRESADO ====")
                OnPickTarget = True
                break

            else:
                # Mueve la banda
                conveyor.MoveJ(conveyor.Joints() + part_travel_mm)

            # Calcula el tiempo transcurrido desde el inicio
            elapsed_time = time.time() - start_time

        end_time = time.time()
        elapsed_time = end_time - start_time
        return elapsed_time, piece_position, OnPickTarget

def MoveConveyor1(conveyor, part_travel_mm, pieza):
    OnPickTarget = None
    if conveyor.Valid():
        conveyor.MoveJ(conveyor.Joints() + part_travel_mm)
        start_time = time.time()
        while conveyor.Valid():
            current_position = conveyor.Pose()[0, 3]  # Obtiene la posición actual del marco
            piece_position = pieza.PoseAbs()[0, 3] 
            print("Pieza xd: ", piece_position)
            #print(f"Error {abs(current_position - pick_positionTorno)}")

            # Verifica si la próxima posición excederá el límite de 2000
            next_position = current_position + part_travel_mm
            print(next_position)
            if next_position > 2000:
                # Si la próxima posición excede el límite, establece la posición en exactamente 2000
                break  # Sal del bucle
            elif abs(current_position - pick_positionUR3) < toleranceUR3:
                print("\n==== ESTACION UR3 ====")
                OnPickTarget = True
                break
            else:
                # Mueve la banda
                conveyor.MoveJ(conveyor.Joints() + part_travel_mm)

            # Calcula el tiempo transcurrido desde el inicio
            elapsed_time = time.time() - start_time

        end_time = time.time()
        elapsed_time = end_time - start_time
        return elapsed_time, piece_position, OnPickTarget


def ResetConveyorPosition(conveyor, resetFramePoint):
    if conveyor.Valid():
        conveyor.setJoints([resetFramePoint])


#ResetConveyorPosition(Conv_mechanism2, 960)
#MoveConveyor3(Conv_mechanism3, PART_TRAVEL_MM3)
