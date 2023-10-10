from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
import time

# === Robot Arms Libraries ===
    # === Torno Objects ===
from Robot_Arms_Scripts import robotTorno, TornoGripperClose, TornoGripperOpen
from Robot_Arms_Scripts import goHome, getPiece, pickPiece, placePiece, dropPiece
from Robot_Arms_Scripts import HomeTargetTorno, PickTargetTorno, PlaceTargetTorno, frameConv3, LatheFrame
from Station_Scripts import DoorDisplacement, TornoPuerta, FresadoPuerta, openDoor, closeDoor

    # === Fresado Objects ===
from Robot_Arms_Scripts import robotFresado, FresadoGripper
from Robot_Arms_Scripts import HomeTargetFresado, PickTargetFresado, PlaceTargetFresado, frameConv4, CNCFrame

    # === UR3  Objects ===
from Robot_Arms_Scripts import robotUR3, UR3Gripper, scanPiece, DeskUR3Frame, frameConv1
from Robot_Arms_Scripts import HomeUR3, PickUR3, PlaceUR3, Scan1, Scan2, Scan3, Scan4, Scan5


RDK = Robolink()

#Set the travel of the conveyors for each iterations
PART_TRAVEL_MM1 = 100
PART_TRAVEL_MM2 = 100
PART_TRAVEL_MM3 = 25
PART_TRAVEL_MM4 = 100

#Declaration of the conveyor object
Conv_mechanism1 = RDK.Item('Conv_Mech1',itemtype=ITEM_TYPE_ROBOT)
Conv_mechanism2 = RDK.Item('Conv_Mech2',itemtype=ITEM_TYPE_ROBOT)
Conv_mechanism3 = RDK.Item('Conv_Mech3',itemtype=ITEM_TYPE_ROBOT)
Conv_mechanism4 = RDK.Item('Conv_Mech4',itemtype=ITEM_TYPE_ROBOT)

# === Pick Targets ===
pick_positionTorno = 1010.0
tolerance = 15
pick_positionFresado = 985.0

toleranceUR3 = 26
pick_positionUR3 = 875.0

# === Robot Scripts ===
# Activar Robot Torno
def activateRobotTorno():
    # Calling Actions
    PutPieceLatheProgram = RDK.Item('Put Piece Lathe')
    GetPieceLatheProgram = RDK.Item('Get Piece Lathe')

    PutPieceLatheProgram.RunProgram()
    time.sleep(5)
    GetPieceLatheProgram.RunProgram()
    time.sleep(5)
    dropPiece(TornoGripperClose,frameConv3)
    



# Activar Robot Fresado
def activateRobotFresado():
    # Calling Actions
    getPiece(robotFresado, PickTargetFresado)
    pickPiece(FresadoGripper)
    time.sleep(0.5)
    goHome(robotFresado, HomeTargetFresado)
    time.sleep(1)
    if FresadoPuerta.Valid():
        openDoor(FresadoPuerta, -DoorDisplacement)
        time.sleep(1)
        placePiece(robotFresado, PlaceTargetFresado)
        time.sleep(1)
        dropPiece(FresadoGripper, CNCFrame)
        time.sleep(0.5)
        goHome(robotFresado, HomeTargetFresado)
        closeDoor(FresadoPuerta, -DoorDisplacement)
        print("Fresando Pieza...")
        time.sleep(5)

        print("Pieza Finalizada!!")
        openDoor(FresadoPuerta, -DoorDisplacement)
        time.sleep(1)
        placePiece(robotFresado, PlaceTargetFresado)
        pickPiece(FresadoGripper)
        time.sleep(1)
        goHome(robotFresado, HomeTargetFresado)
        closeDoor(FresadoPuerta, -DoorDisplacement)
        time.sleep(0.5)
        getPiece(robotFresado, PickTargetFresado)
        dropPiece(FresadoGripper, frameConv4)
        time.sleep(0.5)
        goHome(robotFresado, HomeTargetFresado)
        print("Pieza en Conveyor 4")
        time.sleep(1)

# Activar Robot UR3
def activateUR3():
    getPiece(robotUR3, PickUR3)
    time.sleep(1)
    pickPiece(UR3Gripper)
    time.sleep(0.5)
    goHome(robotUR3, HomeUR3)
    time.sleep(1)
    placePiece(robotUR3, PlaceUR3)
    time.sleep(1)
    dropPiece(UR3Gripper, DeskUR3Frame)
    time.sleep(1)
    scanPiece(robotUR3, Scan1)
    time.sleep(1)
    scanPiece(robotUR3, Scan2)
    time.sleep(1)
    scanPiece(robotUR3, Scan3)
    time.sleep(1)
    scanPiece(robotUR3, Scan2)
    time.sleep(1)
    scanPiece(robotUR3, Scan1)
    time.sleep(1)
    scanPiece(robotUR3, Scan4)
    time.sleep(1)
    scanPiece(robotUR3, Scan5)
    time.sleep(1)
    scanPiece(robotUR3, Scan4)
    time.sleep(1)
    scanPiece(robotUR3, Scan1)
    time.sleep(1)
    print("Pieza Escaneada Correctamente!!")
    time.sleep(1)
    placePiece(robotUR3, PlaceUR3)
    time.sleep(1)
    pickPiece(UR3Gripper)
    time.sleep(1)
    goHome(robotUR3, HomeUR3)
    time.sleep(1)
    getPiece(robotUR3, PickUR3)
    time.sleep(1)
    dropPiece(UR3Gripper, frameConv1)
    time.sleep(1)
    goHome(robotUR3, HomeUR3)
    print("Finished")



def MoveConveyor2(conveyor, part_travel_mm, pieza):
    if conveyor.Valid():
        conveyor.MoveJ(conveyor.Joints() + part_travel_mm)
        start_time = time.time()
        while conveyor.Valid():
            current_position = conveyor.Pose()[0, 3]  # Obtiene la posición actual del marco
            piece_position = pieza.PoseAbs()[0, 3] 
            # Verifica si la próxima posición excederá el límite de 2000
            next_position = current_position + part_travel_mm
            print(next_position)
            if next_position > 2100:
                break  # Sal del bucle
            else:
                # Mueve la banda
                conveyor.MoveJ(conveyor.Joints() + part_travel_mm)

            # Calcula el tiempo transcurrido desde el inicio
            elapsed_time = time.time() - start_time

        end_time = time.time()
        elapsed_time = end_time - start_time
        return elapsed_time, piece_position

def MoveConveyor3(conveyor, part_travel_mm, pieza):
    if conveyor.Valid():
        conveyor.MoveJ(conveyor.Joints() + part_travel_mm)
        start_time = time.time()
        while conveyor.Valid():
            current_position = conveyor.Pose()[0, 3]  # Obtiene la posición actual del marco
            piece_position = pieza.PoseAbs()[0, 3] 
            print("Pieza Position: ", piece_position)
            print(f"Error {abs(current_position - pick_positionTorno)}")

            # Verifica si la próxima posición excederá el límite de 2000
            next_position = current_position + part_travel_mm
            print(next_position)
            if next_position > 2075:
                # Si la próxima posición excede el límite, establece la posición en exactamente 2000
                break  # Sal del bucle
            elif abs(current_position - pick_positionTorno) < tolerance:
                print("\n==== ESTACION TORNO ====")
                activateRobotTorno()
                time.sleep(1)
                conveyor.MoveJ(conveyor.Joints() + part_travel_mm)
            else:
                # Mueve la banda
                conveyor.MoveJ(conveyor.Joints() + part_travel_mm)

            # Calcula el tiempo transcurrido desde el inicio
            elapsed_time = time.time() - start_time
            
        end_time = time.time()
        elapsed_time = end_time - start_time
        return elapsed_time#, piece_position

def MoveConveyor4(conveyor, part_travel_mm, pieza):
    if conveyor.Valid():
        conveyor.MoveJ(conveyor.Joints() + part_travel_mm)
        start_time = time.time()
        while conveyor.Valid():
            current_position = conveyor.Pose()[0, 3]  # Obtiene la posición actual del marco
            piece_position = pieza.PoseAbs()[0, 3] 
            print("Pieza Position: ", piece_position)
            print(f"Error {abs(current_position - pick_positionFresado)}")

            # Verifica si la próxima posición excederá el límite de 2000
            next_position = current_position + part_travel_mm
            print(next_position)
            if next_position > 2100:
                # Si la próxima posición excede el límite, establece la posición en exactamente 2000
                break  # Sal del bucle
            elif abs(current_position - pick_positionFresado) < tolerance:
                print("\n==== ESTACION FRESADO ====")
                activateRobotFresado()
                time.sleep(1)
                conveyor.MoveJ(conveyor.Joints() + part_travel_mm)
            else:
                # Mueve la banda
                conveyor.MoveJ(conveyor.Joints() + part_travel_mm)

            # Calcula el tiempo transcurrido desde el inicio
            elapsed_time = time.time() - start_time

        end_time = time.time()
        elapsed_time = end_time - start_time
        return elapsed_time, piece_position

def MoveConveyor1(conveyor, part_travel_mm, pieza):
    if conveyor.Valid():
        conveyor.MoveJ(conveyor.Joints() + part_travel_mm)
        start_time = time.time()
        while conveyor.Valid():
            current_position = conveyor.Pose()[0, 3]  # Obtiene la posición actual del marco
            piece_position = pieza.PoseAbs()[0, 3] 
            #print("Pieza Position: ", piece_position)
            #print(f"Error {abs(current_position - pick_positionTorno)}")

            # Verifica si la próxima posición excederá el límite de 2000
            next_position = current_position + part_travel_mm
            print(next_position)
            if next_position > 2100:
                # Si la próxima posición excede el límite, establece la posición en exactamente 2000
                break  # Sal del bucle
            elif abs(current_position - pick_positionUR3) < toleranceUR3:
                print("\n==== ESTACION UR3 ====")
                time.sleep(1)
                activateUR3()
                conveyor.MoveJ(conveyor.Joints() + part_travel_mm)
            else:
                # Mueve la banda
                conveyor.MoveJ(conveyor.Joints() + part_travel_mm)

            # Calcula el tiempo transcurrido desde el inicio
            elapsed_time = time.time() - start_time

        end_time = time.time()
        elapsed_time = end_time - start_time
        return elapsed_time, piece_position


def ResetConveyorPosition(conveyor, resetFramePoint):
    if conveyor.Valid():
        conveyor.setJoints([resetFramePoint])


#ResetConveyorPosition(Conv_mechanism2, 960)
#MoveConveyor3(Conv_mechanism3, PART_TRAVEL_MM3)
