import os
import subprocess
import time

# Obtiene la ruta completa del script actual (main.py)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define las rutas completas a tus scripts de la banda transportadora
scriptsBanda = [ 
    os.path.join(script_dir, "Run_Station.py"),

    #os.path.join(script_dir, "Switch_Obj_ref.py"),
    #os.path.join(script_dir, "Run_Conveyor_Curve.py"),

    #os.path.join(script_dir, "Run_Conveyor.py"),
    #os.path.join(script_dir, "Run_Conveyor_Curve.py"),

    #os.path.join(script_dir, "Run_Conveyor.py"),
    #os.path.join(script_dir, "Run_Conveyor_Curve.py"),
    
    #os.path.join(script_dir, "Run_Conveyor.py"),
    #os.path.join(script_dir, "Run_Conveyor_Curve.py")
    
]

pieza_recogida = False  # Indica si la pieza ha sido recogida por el robot
banda_activa = True     # Indica si la banda está en funcionamiento

print("Scripts Banda")
while True:
    for script_path in scriptsBanda:
        #print("========== Current Script: ", script_path)
        try:
            if banda_activa and pieza_recogida is False:
                subprocess.run(["python", script_path], check=True)

        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar {script_path}: El proceso hijo devolvió un código de retorno no válido ({e.returncode})")

    time.sleep(0.5)  # Espera 0.5 segundos