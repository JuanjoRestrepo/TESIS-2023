import tkinter as tk
from tkinter import ttk
from datetime import datetime


class Order:
    def __init__(self, order_id, pieces, material, piece, date_created):
        self.order_id = order_id
        self.pieces = pieces
        self.material = material
        self.piece = piece
        self.date_created = date_created
    
    def __str__(self):
        return f"ID de Orden: {self.order_id}"



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


    def print_orders(self):
        print("\n===== Ordenes =====")
        for order in self.orders:
            print(order.order_id)
        
        # Crear una ventana para mostrar las órdenes
        orders_window = tk.Toplevel()
        orders_window.title("Órdenes")
        
        # Centrar la ventana
        width = orders_window.winfo_screenwidth()
        height = orders_window.winfo_screenheight()
        x = (width - 1000) // 2
        y = (height - 400) // 2
        orders_window.geometry("1000x400+{}+{}".format(x, y))

        # Mostrar el encabezado de la tabla de órdenes
        header_frame = tk.Frame(orders_window)
        header_frame.pack(side="top", fill="x", pady=10)

        order_id_label = tk.Label(header_frame, text="ID de la Orden", width=30)
        order_id_label.pack(side="left")

        pieces_label = tk.Label(header_frame, text="Cantidad de Piezas", width=20)
        pieces_label.pack(side="left")

        material_label = tk.Label(header_frame, text="Tipo de Material", width=20)
        material_label.pack(side="left")

        piece_label = tk.Label(header_frame, text="Tipo de Pieza", width=20)
        piece_label.pack(side="left")

        date_created_label = tk.Label(header_frame, text="Fecha de Creación", width=20)
        date_created_label.pack(side="left")

        # Mostrar cada orden en una fila de la tabla
        for order in self.orders:
            order_frame = tk.Frame(orders_window)
            order_frame.pack(side="top", fill="x", pady=5)

            order_id_label = tk.Label(order_frame, text=order.order_id, width=30)
            order_id_label.pack(side="left")

            pieces_label = tk.Label(order_frame, text=order.pieces, width=20)
            pieces_label.pack(side="left")

            material_label = tk.Label(order_frame, text=order.material, width=20)
            material_label.pack(side="left")

            piece_label = tk.Label(order_frame, text=order.piece, width=20)
            piece_label.pack(side="left")

            date_created_label = tk.Label(order_frame, text=order.date_created.strftime("%Y-%m-%d"), width=20)
            date_created_label.pack(side="left")

        # Botón para cerrar la ventana de órdenes
        close_button = tk.Button(orders_window, text="Cerrar", command=orders_window.destroy)
        close_button.pack(side="bottom", pady=10)
        


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

            # Validación de campos de entrada
            if not pieces or not material or not piece:
                error_message = tk.Toplevel(create_order_window)
                # Centrar la ventana de error
                width = error_message.winfo_screenwidth()
                height = error_message.winfo_screenheight()
                x = (width - 200) // 2
                y = (height - 100) // 2
                error_message.geometry("200x100+{}+{}".format(x, y))
                error_message.title("Error")
                error_label = tk.Label(error_message, text="Debe llenar todos los campos.")
                error_label.pack(side="top", pady=10)
                error_button = tk.Button(error_message, text="Aceptar", command=error_message.destroy)
                error_button.pack(side="bottom", pady=10)
                return


            try:
                pieces = int(pieces)
                if pieces <= 0:
                    raise ValueError("La cantidad de piezas debe ser un número positivo.")
            except ValueError as e:
                error_message = tk.Toplevel(create_order_window)
                error_message.title("Error")
                error_message.geometry("400x200")
                error_message.resizable(False, False)
                width = error_message.winfo_screenwidth()
                height = error_message.winfo_screenheight()
                x = (width - 400) // 2
                y = (height - 200) // 2
                error_message.geometry("+{}+{}".format(x, y))
                error_label = tk.Label(error_message, text=str(e))
                error_label.pack(side="top", pady=10)
                error_button = tk.Button(error_message, text="Aceptar", command=error_message.destroy)
                error_button.pack(side="bottom", pady=10)
                return


            # Crear el ID de la orden y la fecha de creación
            date_created = datetime.now()
            #Convertimos la fecha 
            # de formato <class 'datetime.datetime'>
            # a formato <string>
            date_string = date_created.strftime("%Y-%m-%d")
            order_id = "{}P{}_{}_C{}".format(material[0], piece[-1], date_string, pieces)

            # Crear una instancia de la clase Order con los datos ingresados
            order = Order(order_id, pieces, material, piece, date_created)

            # Agregar la orden a la lista de órdenes
            self.orders.append(order)

            # Cerrar la ventana de Crear Orde con sus detalles y volver a la pantalla principal
            order_details_window = tk.Toplevel(create_order_window)
            width = order_details_window.winfo_screenwidth()
            height = order_details_window.winfo_screenheight()
            x = (width - 400) // 2
            y = (height - 250) // 2
            order_details_window.title("Detalles de la Orden")
            order_details_window.geometry("400x250+{}+{}".format(x, y))
            # Mostrar el ID de la orden
            order_id_label = tk.Label(order_details_window, text="ID de la Orden: {}".format(order.order_id))
            order_id_label.pack(side="top", pady=10)

            # Mostrar la fecha de creación de la orden
            date_created_label = tk.Label(order_details_window, text="Fecha de Creación: {}".format(order.date_created.strftime("%Y-%m-%d")))
            date_created_label.pack(side="top", pady=10)


            # Mostrar la cantidad de piezas de la orden
            pieces_label = tk.Label(order_details_window, text="Cantidad de Piezas: {}".format(order.pieces))
            pieces_label.pack(side="top", pady=10)

            # Mostrar el tipo de material de la orden
            material_label = tk.Label(order_details_window, text="Tipo de Material: {}".format(order.material))
            material_label.pack(side="top", pady=10)

            # Mostrar el tipo de pieza de la orden
            piece_label = tk.Label(order_details_window, text="Tipo de Pieza: {}".format(order.piece))
            piece_label.pack(side="top", pady=10)

            # Botón para cerrar la ventana de detalles de la orden
            close_button = tk.Button(order_details_window, text="Cerrar", command=order_details_window.destroy)
            close_button.pack(side="bottom", pady=10)


            #print("Orden Creada")
            #create_order_window.destroy()
            #self.go_to_main_screen()
        
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
            order_index = order_combobox.get()
            if not order_index:
                error_message = tk.Toplevel(delete_order_window)
                
                # Centrar la ventana de mensaje de eliminar ordenes
                width = delete_order_window.winfo_screenwidth()
                height = delete_order_window.winfo_screenheight()
                x = (width - 200) // 2
                y = (height - 100) // 2
                error_message.geometry("200x100+{}+{}".format(x, y))
                error_message.title("Error")
                error_label = tk.Label(error_message, text="Debe seleccionar una orden.")
                error_label.pack(side="top", pady=10)
                error_button = tk.Button(error_message, text="Aceptar", command=error_message.destroy)
                error_button.pack(side="bottom", pady=10)
                return
            else:
                order_index = int(order_index) - 1
                if order_index < 0 or order_index >= len(self.orders):
                    error_message = tk.Toplevel(delete_order_window)
                    error_message.geometry("200x100")
                    error_message.title("Error")
                    error_label = tk.Label(error_message, text="Seleccione una orden válida.")
                    error_label.pack(side="top", pady=10)
                    error_button = tk.Button(error_message, text="Aceptar", command=error_message.destroy)
                    error_button.pack(side="bottom", pady=10)
                    return

            # Eliminar la orden de la lista de órdenes
            del self.orders[order_index]

            # Cerrar la ventana de Eliminar Orden y volver a la pantalla principal
            print("Orden Eliminada: Orden {}".format(order_index+1))
            delete_order_window.destroy()
            self.go_to_main_screen()


        # Botón para eliminar la orden
        delete_order_button = tk.Button(delete_order_window, text="Eliminar Orden", command=delete_order)
        delete_order_button.pack(side="bottom", pady=10)

    def modify_order_screen():
        pass


    def show_order_details(order):
        # Crear una ventana para mostrar los detalles de la orden
        order_details_window = tk.Toplevel()
        order_details_window.title("Detalles de la Orden")
        
        # Centrar la ventana
        width = order_details_window.winfo_screenwidth()
        height = order_details_window.winfo_screenheight()
        x = (width - 450) // 2
        y = (height - 250) // 2
        order_details_window.geometry("450x250+{}+{}".format(x, y))

        # Mostrar el ID de la orden
        order_id_label = tk.Label(order_details_window, text="ID de la Orden: {}".format(order.order_id))
        order_id_label.pack(side="top", pady=10)

        # Mostrar la fecha de creación de la orden
        date_created_label = tk.Label(order_details_window, text="Fecha de Creación: {}".format(order.date_created.strftime("%Y-%m-%d")))
        date_created_label.pack(side="top", pady=10)


        # Mostrar la cantidad de piezas de la orden
        pieces_label = tk.Label(order_details_window, text="Cantidad de Piezas: {}".format(order.pieces))
        pieces_label.pack(side="top", pady=10)

        # Mostrar el tipo de material de la orden
        material_label = tk.Label(order_details_window, text="Tipo de Material: {}".format(order.material))
        material_label.pack(side="top", pady=10)

        # Mostrar el tipo de pieza de la orden
        piece_label = tk.Label(order_details_window, text="Tipo de Pieza: {}".format(order.piece))
        piece_label.pack(side="top", pady=10)

        # Botón para cerrar la ventana de detalles de la orden
        close_button = tk.Button(order_details_window, text="Cerrar", command=order_details_window.destroy)
        close_button.pack(side="bottom", pady=10)

    

    def go_to_main_screen(self):
        self.master.deiconify()  # Mostrar la pantalla principal




if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

