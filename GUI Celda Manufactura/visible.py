# Import the Robot DK Library
from robolink import *
from robodk import *

RDK = Robolink() 


# Obtener el objeto que deseas duplicar
nombre_objeto = 'Piece1'  # Reemplaza con el nombre de tu objeto
pieza_original = RDK.Item(nombre_objeto)
lathe= RDK.Item('Mazak Lathe Base torno')
pieza_original.Copy()
object_copy1 = RDK.Paste(paste_to=lathe)
object_copy1.setName('piece')
object_copy1.setPose(transl(-352.259,-145.960,-85.819))


# Actualizar la pantalla de RoboDK
RDK.Render()

print("Pieza copiada y pegada en la nueva posición.")