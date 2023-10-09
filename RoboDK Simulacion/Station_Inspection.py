from robolink import Robolink
import time

def Run (ID):
    # Conectar a RoboDK
    RDK = Robolink()
    name_robot = 'Robot UR3'  # Reemplaza con el nombre de tu robot
    robot = RDK.Item(name_robot)
    
    # Guardar el tiempo de inicio
    tiempo_inicio = time.time()

    # Verificar si el robot existe
    if robot.Valid():
        # Establecer la velocidad del robot en mm/s (ajusta según tus necesidades)
        nueva_velocidad = 100  # por ejemplo, 100 mm/s
        robot.setSpeed(nueva_velocidad)

        # Obtener el programa que deseas ejecutar
        name_program = 'Inspection'  # Reemplaza con el nombre de tu programa
        programa = RDK.Item(name_program)

        # Verificar si el programa existe
        if programa.Valid():
            # Ejecutar el programa
            programa.RunProgram()

            print(f"Programa '{name_program}' ejecutado con éxito.")
        else:
            print(f"El programa '{name_program}' no existe en la estación de RoboDK.")

    # Guardar el tiempo de finalización
    tiempo_fin = time.time()

    # Calcular el tiempo transcurrido
    tiempo_transcurrido = tiempo_fin - tiempo_inicio

    print(f"Tiempo transcurrido: {tiempo_transcurrido} segundos")

Run(3)