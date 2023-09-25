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

#robotFresado.MoveJ(PlaceTargetFresado)