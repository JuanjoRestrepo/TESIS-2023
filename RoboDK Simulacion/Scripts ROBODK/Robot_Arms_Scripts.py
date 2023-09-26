from robodk import *      # RoboDK API
from robolink import *    # Robot toolbox
import time

# Link to RoboDK
RDK = Robolink()

# ==== Define la velocidad de movimiento ====
velocidad = 50  # en mm/s
robotTorno = RDK.Item('Mitsubishi Torno')
TornoGripper = RDK.Item('Robot Torno Gripper (Closed)')

robotFresado = RDK.Item('Mitsubishi Fresado')
FresadoGripper = RDK.Item('Robot Fresado Gripper (Closed)')

robotUR3 = RDK.Item('Robot UR3')
UR3Gripper = RDK.Item('Robot UR3 Gripper (Open)')

# ==== Volver a "Home" ====
def goHome(robot, home_target):
    robot.setSpeed(velocidad)
    robot.MoveJ(home_target)  # Mueve el robot de regreso a la posición "Home"

# ==== Moverse hacia la Pieza ====
def getPiece(robot, piece_target):
    robot.setSpeed(velocidad)  # Configura la velocidad de movimiento del robot
    robot.MoveJ(piece_target)

# ==== Recoger/Tomar la Pieza====
def pickPiece(robotTool):
    robotTool.AttachClosest()
    print("Pieza Tomada")

# === Colocar Pieza en Torno/Fresado
def placePiece(robot, place_target):
    robot.setSpeed(velocidad)
    robot.MoveJ(place_target)

# ==== Drop/Devolver la Pieza====
def dropPiece(robotTool, drop_frame):
    robotTool.DetachClosest()
    # Obtiene el objeto que fue desconectado (el objeto previamente adjunto)
    detached_object = robotTool.Childs()[0]
    # Establece "Frame_Conv3" como el padre del objeto previamente adjunto
    detached_object.setParentStatic(drop_frame)

def scanPiece(robot, scan_target):
    robot.setSpeed(velocidad)
    robot.MoveJ(scan_target)

# ==== Targets Torno ====
HomeTargetTorno = RDK.Item('Home_Robot_Torno2')
PickTargetTorno = RDK.Item('Pick_Robot_Torno2')
PlaceTargetTorno = RDK.Item('Place_Robot_Torno2')
frameConv3 = RDK.Item('Frame_Conv3')
LatheFrame = RDK.Item('Lathe')

# ==== Targets Fresado ====
HomeTargetFresado = RDK.Item('Casita')
PickTargetFresado = RDK.Item('Recoger')
PlaceTargetFresado = RDK.Item('Colocar')
frameConv4 = RDK.Item('Frame_Conv4')
CNCFrame = RDK.Item('CNC')

# ==== Targets UR3 ====
HomeUR3 = RDK.Item('HomeUR3')
PickUR3 = RDK.Item('Pick')
PlaceUR3 = RDK.Item('PlacePieceUR3')
frameConv1 = RDK.Item('Frame_Conv1')
DeskUR3Frame = RDK.Item('DeskUR3')

# Scan Targets
Scan1 = RDK.Item('Scan1')
Scan2 = RDK.Item('Scan2')
Scan3 = RDK.Item('Scan3')
Scan4 = RDK.Item('Scan4')
Scan5 = RDK.Item('Scan5')

#pickPiece(UR3Gripper)
#time.sleep(0.5)
#goHome(robotUR3, HomeUR3)
#time.sleep(1)
#placePiece(robotUR3, PlaceUR3)
#time.sleep(1)
#dropPiece(UR3Gripper, DeskUR3Frame)
#time.sleep(1)
#dropPiece(UR3Gripper, frameConv1)
#pickPiece(UR3Gripper)
#dropPiece(UR3Gripper, DeskUR3Frame)
#goHome(robotUR3, HomeUR3)
#scanPiece(robotUR3, Scan1)
#dropPiece(UR3Gripper, frameConv1)
