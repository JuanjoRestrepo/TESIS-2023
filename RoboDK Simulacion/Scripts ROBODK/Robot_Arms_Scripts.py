from robodk import *      # RoboDK API
from robolink import *    # Robot toolbox
import time

# Link to RoboDK
RDK = Robolink()

# ==== Define la velocidad de movimiento ====
velocidad = 100  # en mm/s

# ==== ROBOTS ====
robotTorno = RDK.Item('Mitsubishi Torno')
TornoGripper = RDK.Item('Robot Torno Gripper (Closed)')

robotFresado = RDK.Item('Mitsubishi Fresado')
FresadoGripper = RDK.Item('Robot Fresado Gripper (Closed)')


# ==== Volver a "Home" ====
def goHome(robot, home_target):
    robot.MoveJ(home_target)  # Mueve el robot de regreso a la posición "Home"

# ==== Moverse hacia la Pieza ====
def getPiece(robot, piece_target):
    robot.setSpeed(velocidad)  # Configura la velocidad de movimiento del robot
    robot.MoveJ(piece_target)

def placePiece(robot, place_target):
    robot.setSpeed(velocidad)  # Configura la velocidad de movimiento del robot
    robot.MoveJ(place_target)

# ==== Recoger/Tomar la Pieza====
def pickPiece(robotTool):
    robotTool.AttachClosest()
    print("Pieza Tomada")

# ==== Drop/Devolver la Pieza====
def dropPiece(robotTool, destiny_frame):
    robotTool.DetachClosest()
    # Obtiene el objeto que fue desconectado (el objeto previamente adjunto)
    detached_object = robotTool.Childs()[0]
    # Establece "Frame_Conv3" como el padre del objeto previamente adjunto
    detached_object.setParentStatic(destiny_frame)
    print("Pieza Soltada")



# ==== Targets Torno ====
HomeTargetTorno = RDK.Item('Home_Robot_Torno2')
PickTargetTorno = RDK.Item('Pick_Robot_Torno2')
PlaceTargetTorno = RDK.Item('Place_Robot_Torno2')

frameConv3 = RDK.Item('Frame_Conv3')
frameMazakLathe = RDK.Item('Lathe')

# ==== Targets Fresado ====
HomeTargetFresado = RDK.Item('Home_Robot_Fresado2')
PickTargetFresado = RDK.Item('Pick_Robot_Fresado2')
PlaceTargetFresado  = RDK.Item('Place_Robot_Fresado2')

frameConv4 = RDK.Item('Frame_Conv4')
frameCNC = RDK.Item('CNC')

#goHome(robotFresado, HomeTargetFresado)
#getPiece(robotFresado, PickTargetFresado)
#placePiece(robotFresado, PlaceTargetFresado)

