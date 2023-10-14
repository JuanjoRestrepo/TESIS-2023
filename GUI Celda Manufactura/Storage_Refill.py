from robolink import *

def Storage():
    RDK = Robolink()
    Init = RDK.Item('Init')
    Init.RunProgram()

    # Obtener todas las piezas con el mismo nombre
    piezas = RDK.ItemList(filter= ITEM_TYPE_OBJECT,list_names=True)

    num = piezas.count('piece')

    for i in range(num):
        pieza = RDK.Item('piece')
        pieza.Delete()

Storage()