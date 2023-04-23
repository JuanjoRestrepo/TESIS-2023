import tkinter as tk
from tkinter import ttk
import os

# Creamos la Ventana Principal
main_window = tk.Tk()

# Tamaño de la ventana
main_window.geometry("600x400")

# Labels de Pantallas
labelMainScreen = tk.Label(main_window, text="CELDA DE MANUFACTURA")
labelCrearOrdenScreen = tk.Label(main_window, text="CREAR ORDEN")

# Primer Texbox para la Cantidad de Piezas
cantidad_label = tk.Label(main_window, text="Cantidad")
cantidad_textbox = tk.Entry(main_window)

# Opciones de Materiales
material_label = tk.Label(main_window, text="Material")
material_combobox = ttk.Combobox(main_window, values=["Aluminium", "Empack"])

# Opciones de Piezas
pieza_label = tk.Label(main_window, text="Pieza")
pieza_combobox = ttk.Combobox(main_window, values=["Piece1", "Piece2", "Piece3"])


def crear_orden():
    print("Se ha creado una nueva orden")
    labelMainScreen.pack_forget()
    BotonCrearOrden.pack_forget()
    BotonEliminar.pack_forget()
    BotonModificar.pack_forget()

    # Mostrar los nuevos widgets
    '''labelCrearOrdenScreen.pack(anchor='nw')
    #cantidad_label.pack(side="left", padx=70, pady=50)
    #cantidad_textbox.pack(side="left", padx=10, pady=50)
    #BotonVolver.pack(side="bottom", anchor='se')'''

    labelCrearOrdenScreen.pack(anchor='nw')
    cantidad_label.pack(pady=30) 
    cantidad_textbox.pack(side="left", padx=10, pady=40)
    
    material_label.pack(side="left", padx=70, pady=60)
    material_combobox.pack(side="left", padx=10, pady=60)

    pieza_label.pack(side="left", padx=70, pady=80)
    pieza_combobox.pack(side="left", padx=70, pady=80)
    BotonVolver.pack(side="bottom", anchor='se')

    centrarVentana()

def eliminar_orden():
    print("Se ha eliminado una orden existente")

def modificar_orden():
    print("Se ha modificado una orden existente")

def centrarVentana():
    # Centrar la ventana
    main_window.update_idletasks()
    width = main_window.winfo_width()
    height = main_window.winfo_height()
    x = (main_window.winfo_screenwidth() // 2) - (width // 2)
    y = (main_window.winfo_screenheight() // 2) - (height // 2)
    main_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def volver():
    # Remover widgets actuales
    labelCrearOrdenScreen.pack_forget()
    BotonVolver.pack_forget()
    cantidad_label.pack_forget()
    cantidad_textbox.pack_forget()
    material_label.pack_forget()
    material_combobox.pack_forget()
    pieza_label.pack_forget()
    pieza_combobox.pack_forget()

    # Mostrar los widgets originales
    labelMainScreen.pack()
    BotonCrearOrden.pack()
    BotonEliminar.pack()
    BotonModificar.pack()

    centrarVentana()

BotonCrearOrden  = tk.Button(main_window, text="Crear Orden", command=crear_orden)
BotonEliminar = tk.Button(main_window, text="Eliminar Orden", command=eliminar_orden)
BotonModificar = tk.Button(main_window, text="Modificar Orden", command=modificar_orden)
BotonVolver = tk.Button(main_window, text="Volver", command=volver)

labelMainScreen.pack()
BotonCrearOrden .pack()
BotonEliminar.pack()
BotonModificar.pack()

def crearVentana():
    
    os.system('cls')
    centrarVentana()
    main_window.mainloop()

crearVentana()
