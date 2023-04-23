import tkinter as tk
from tkinter import ttk

class Order:
    def __init__(self, pieces, material, piece):
        self.pieces = pieces
        self.material = material
        self.piece = piece


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.orders = [] # Definición de la lista de órdenes vacía
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

        self.print_orders_button = tk.Button(self, text="Ver órdenes", command=self.print_orders)
        self.print_orders_button.pack(side="top")

    def create_order(self):
        # Lógica para crear una orden aquí
        self.create_order_screen()
        

    def delete_order(self):
        # Lógica para eliminar una orden aquí
        self.delete_order_screen()


    def modify_order(self):
        # Lógica para modificar una orden aquí
        print("Orden Modificada")



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


        def create_order():
            pieces = pieces_entry.get()
            material = material_combobox.get()
            piece = piece_combobox.get()

            # Crear una instancia de la clase Order con los datos ingresados
            order = Order(pieces, material, piece)

            # Agregar la orden a la lista de órdenes
            self.orders.append(order)

            # Cerrar la ventana de Crear Orden y volver a la pantalla principal
            print("Orden Creada")
            create_order_window.destroy()
            self.go_to_main_screen()
        
        # Botón para crear la orden
        create_order_button = tk.Button(create_order_window, text="Crear Orden", command=create_order)
        create_order_button.pack(side="bottom", pady=10)
    


    def delete_order_screen(self):
        self.master.withdraw()
        delete_order_window = tk.Toplevel(self)
        # Centrar la ventana de eliminar ordenes
        width = delete_order_window.winfo_screenwidth()
        height = delete_order_window.winfo_screenheight()
        x = (width - 600) // 2
        y = (height - 400) // 2
        delete_order_window.geometry("600x400+{}+{}".format(x, y))
        delete_order_window.title("ELIMINAR ORDEN")

        # Frame para seleccionar la orden a eliminar
        order_frame = tk.Frame(delete_order_window)
        order_frame.pack(side="top", pady=10)
        order_label = tk.Label(order_frame, text="Seleccione la Orden a Eliminar:")
        order_label.pack(side="left")
        order_combobox = ttk.Combobox(order_frame, values=[str(i) for i in range(1, len(self.orders) + 1)])
        order_combobox.pack(side="left")

        # Regresar
        back_button = tk.Button(delete_order_window, text="Regresar a pantalla principal", command=self.go_to_main_screen)
        back_button.pack(side="bottom", pady=10)

        def delete_order():
            order_index = int(order_combobox.get()) - 1
            if order_index < 0 or order_index >= len(self.orders):
                print("Error: Seleccione una orden válida")
            else:
                # Eliminar la orden de la lista de órdenes
                del self.orders[order_index]

                # Cerrar la ventana de Eliminar Orden y volver a la pantalla principal
                print("Orden Eliminada: Orden {}".format(order_index+1))
                delete_order_window.destroy()
                self.go_to_main_screen()

        # Botón para eliminar la orden
        delete_order_button = tk.Button(delete_order_window, text="Eliminar Orden", command=delete_order)
        delete_order_button.pack(side="bottom", pady=10)



    def print_orders(self):
        print("\n===== Ordenes =====")
        for order in self.orders:
            print("Piezas: {}, Material: {}, Tipo de Pieza: {}".format(order.pieces, order.material, order.piece))
    


    def go_to_main_screen(self):
        self.master.deiconify()  # Mostrar la pantalla principal




if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

