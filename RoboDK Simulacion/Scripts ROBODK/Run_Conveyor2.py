from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
import time

RDK = Robolink()

#Set the travel of the conveyors for each iterations
PART_TRAVEL_MM = 250

#Declaration of the conveyor object
Conv_mechanism2 = RDK.Item('Conv_Mech2',itemtype=ITEM_TYPE_ROBOT)

def MoveConveyor2(conveyor, part_travel_mm):
    if conveyor.Valid():
        conveyor.MoveJ(conveyor.Joints() + part_travel_mm)
        start_time = time.time()
        while conveyor.Valid():
            current_position = conveyor.Pose()[0, 3]  # Obtiene la posición actual del marco

            # Verifica si la próxima posición excederá el límite de 2000
            next_position = current_position + PART_TRAVEL_MM
            if next_position >= 2001:
                # Si la próxima posición excede el límite, establece la posición en exactamente 2000
                print("Out of Conveyor 2")
                break  # Sal del bucle
            else:
                # Mueve la banda
                conveyor.MoveJ(conveyor.Joints() + PART_TRAVEL_MM)

            # Calcula el tiempo transcurrido desde el inicio
            elapsed_time = time.time() - start_time

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Tiempo total: {elapsed_time} segundos")

def ResetConveyorPosition(conveyor):
    #This program reinitialize every mechanisms in the list to position 0
    if conveyor.Valid():
        conveyor.setJoints([1000])

#MoveConveyor2(Conv_mechanism2, PART_TRAVEL_MM)
#ResetConveyorPosition(Conv_mechanism2)

"""
def moveConveyor2(conveyor, PART_TRAVEL_MM):

    if conveyor.Valid():
        start_time = time.time()  # Obtiene el tiempo de inicio
        tiempo_limite = 5.80  # segundos (tu tiempo promedio)

        while conveyor.Valid():
            current_position = conveyor.Pose()[0, 3]  # Obtiene la posición actual del marco

            # Verifica si la próxima posición excederá el límite de 2000
            next_position = current_position + PART_TRAVEL_MM
            if next_position >= 2001:
                # Si la próxima posición excede el límite, establece la posición en exactamente 2000
                print("Out of Conveyor 2")
                break  # Sal del bucle
            else:
                # Mueve la banda
                conveyor.MoveJ(conveyor.Joints() + PART_TRAVEL_MM)

            # Calcula el tiempo transcurrido desde el inicio
            elapsed_time = time.time() - start_time

            # Verifica si el tiempo transcurrido alcanza el tiempo límite
            if elapsed_time >= tiempo_limite:
                print(f"Banda funcionando durante {elapsed_time} segundos")
                break  # Sal del bucle después de ejecutar durante el tiempo límite

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Tiempo total: {elapsed_time} segundos")


moveConveyor2(Conv_mechanism2, PART_TRAVEL_MM)
"""