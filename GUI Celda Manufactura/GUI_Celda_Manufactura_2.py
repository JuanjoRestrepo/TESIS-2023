import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("600x400")
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        x = (width - 600) // 2
        y = (height - 400) // 2
        self.master.geometry("600x400+{}+{}".format(x, y))
        self.master.title("Celda de Manufactura")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.create_order_button = tk.Button(self, text="Crear Orden", command=self.create_order)
        self.create_order_button.pack(side="top")

        self.delete_order_button = tk.Button(self, text="Eliminar Orden", command=self.delete_order)
        self.delete_order_button.pack(side="top")

        self.modify_order_button = tk.Button(self, text="Modificar Orden", command=self.modify_order)
        self.modify_order_button.pack(side="top")

    def create_order(self):
        # Lógica para crear una orden aquí
        self.create_order_screen()
        print("Orden Creada")

    def delete_order(self):
        # Lógica para eliminar una orden aquí
        print("Orden Eliminada")
        pass

    def modify_order(self):
        # Lógica para modificar una orden aquí
        print("Orden Modificada")
        pass


    # Screens/Pantallas
    def create_order_screen(self):
        self.master.withdraw()
        create_order_window = tk.Toplevel(self)
        # Centrar la ventana de crear ordenes
        width = create_order_window.winfo_screenwidth()
        height = create_order_window.winfo_screenheight()
        x = (width - 600) // 2
        y = (height - 400) // 2
        create_order_window.geometry("600x400+{}+{}".format(x, y))
        create_order_window.title("CREAR ORDEN")

        # Frame para la cantidad de piezas
        pieces_frame = tk.Frame(create_order_window)
        pieces_frame.pack(side="top", pady=10)
        pieces_label = tk.Label(pieces_frame, text="Cantidad de Piezas:")
        pieces_label.pack(side="left")
        pieces_entry = tk.Entry(pieces_frame)
        pieces_entry.pack(side="left")

        # Frame para el tipo de material
        material_frame = tk.Frame(create_order_window)
        material_frame.pack(side="top", pady=10)
        material_label = tk.Label(material_frame, text="Tipo de Material:")
        material_label.pack(side="left")
        material_combobox = ttk.Combobox(material_frame, values=["Aluminio", "Empack"])
        material_combobox.pack(side="left")

        # Frame para el tipo de pieza
        piece_frame = tk.Frame(create_order_window)
        piece_frame.pack(side="top", pady=10)
        piece_label = tk.Label(piece_frame, text="Tipo de Pieza:")
        piece_label.pack(side="left")
        piece_combobox = ttk.Combobox(piece_frame, values=["Pieza1", "Pieza2", "Pieza3"])
        piece_combobox.pack(side="left")

        # Regresar
        back_button = tk.Button(create_order_window, text="Regresar a pantalla principal", command=self.go_to_main_screen)
        back_button.pack(side="bottom", pady=10)

    def go_to_main_screen(self):
        self.master.deiconify()  # Mostrar la pantalla principal




if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()







