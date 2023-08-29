import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import Coordinador_Main
import Graph
from PIL import ImageTk, Image  


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # Agregar el atributo para la instancia del coordinador
        self.base = Graph.graph()
        self.coordinator = Coordinador_Main.coordinator()

        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        x = (width - 600) // 2
        y = (height - 400) // 2
        self.master.geometry("600x400+{}+{}".format(x, y))
        self.master.title("Celda de Manufactura")
        self.master.configure(bg='white')
        img = Image.open("logoazul javeriana.png")
        img = img.resize((150,50))

        self.logo = ImageTk.PhotoImage(img)
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        
        self.configure(bg='white')
        self.label = ttk.Label(self, image=self.logo,background='white')
        self.label.grid(row=2, column=3,sticky='NE', pady=40)
        self.label2 = ttk.Label(self, text="CELDA DE MANUFACTURA CAP",background='white',foreground='#3B628C')
        self.label2.grid(row=2, column=0, columnspan=2,padx=5, pady=40, sticky='W')
        

        self.create_order_button = tk.Button(self, text="CREAR ORDEN", command=self.create_order_screen,bg="white")
        self.create_order_button.grid(row=4, column=1,padx=20, pady=7,ipadx=60, ipady=5)

        self.delete_order_button = tk.Button(self, text="ELIMINAR ORDEN", command=self.delete_order,bg="white")
        self.delete_order_button.grid(row=5, column=1,padx=20, pady=7,ipadx=50, ipady=5)

        self.modify_order_button = tk.Button(self, text="MODIFICAR UNA ORDEN", command=self.modify_order,bg="white")
        self.modify_order_button.grid(row=6, column=1,padx=20, pady=7,ipadx=30, ipady=5)

        self.print_orders_button = tk.Button(self, text="ÓRDENES", command=self.print_orders,bg="white")
        self.print_orders_button.grid(row=7, column=1,columnspan=3,padx=20, pady=7,ipadx=70, ipady=5)



        self.modify_storage_button = tk.Button(self, text="MODIFICAR ALMACÉN", command=self.modify_storage,bg="white")
        self.modify_storage_button.grid(row=4, column=3,padx=20, pady=7,ipadx=35, ipady=5)

        self.start_button = tk.Button(self, text="EJECUTAR CELDA", command=self.print_orders,bg="white")
        self.start_button.grid(row=5, column=3,padx=20, pady=7,ipadx=50, ipady=5)

        self.stop_button = tk.Button(self, text="DESACTIVAR CELDA", command=self.print_orders,bg="white")
        self.stop_button.grid(row=6, column=3,padx=20, pady=7,ipadx=42, ipady=5)
     
    def create_order_screen(self):
        # Lógica para crear una orden aquí
        self.master.withdraw()
        create_order_window = tk.Toplevel(self)
        """
        #Traer la información necesaria
        base = self.base
        key_m,material= base.get_data('material')
        key_p,pieces = self.base.get_data('pieces')
        f_pieces = eval(pieces[self.Find_Index_Key(key_p[0],'Name')])
        f_material = eval(material[self.Find_Index_Key(key_m[0],'Name')])
        """
        
        # Centrar la ventana de crear ordenes
        width = create_order_window.winfo_screenwidth()
        height = create_order_window.winfo_screenheight()
        x = (width - 600) // 2
        y = (height - 400) // 2
        create_order_window.geometry("600x400+{}+{}".format(x, y))
        create_order_window.title("CREAR ORDEN")
        create_order_window.configure(bg='white')

        # Ingresar Logo y Título
        logo = tk.Label(create_order_window, image=self.logo,background='white')
        logo.grid(row=0, column=6,sticky='NSEW',pady=30)
        titulo = tk.Label(create_order_window, text="CREAR ORDEN",background='white',foreground='#3B628C',anchor='e')
        titulo.grid(row=0, column=0,padx=20,pady=30,ipadx=15,sticky='W')
        
        # Frame para la cantidad de piezas
        piece_amount_label = tk.Label(create_order_window, text="CANTIDAD :",background='white')
        piece_amount_label.grid(row=1, column=1,columnspan=2,padx=15,pady=7,ipady=3,sticky='E')
        piece_amount_entry = tk.Entry(create_order_window,bg='white')
        piece_amount_entry.grid(row=1, column=3,columnspan=3,pady=7,ipady=3,ipadx=12,sticky='NSEW')

        # Frame para la cantidad de piezas
        material_label = tk.Label(create_order_window, text="MATERIAL :",background='white')
        material_label.grid(row=2, column=1,columnspan=2,padx=15,pady=7,ipady=3,sticky='E')
        material_combobox = ttk.Combobox(create_order_window, values= ['pepe'],background='white')
        material_combobox.grid(row=2, column=3,columnspan=3,pady=7,ipady=3,ipadx=12,sticky='NSEW')

        # Frame para la cantidad de piezas
        piece_type_label = tk.Label(create_order_window, text="PIEZA :",background='white')
        piece_type_label.grid(row=3, column=1,columnspan=2,padx=15,pady=7,ipady=3,sticky='E')
        piece_type_combobox = ttk.Combobox(create_order_window, values= ['pepe'],background='white')
        piece_type_combobox.grid(row=3, column=3,columnspan=3,pady=7,ipady=3,ipadx=12,sticky='NSEW')
        
        def clear_fields():
            piece_amount_entry.delete(0, tk.END)
            material_combobox.set('')
            piece_type_combobox.set('')

        def create_order():
            piece_amount = piece_amount_entry.get()
            material = material_combobox.get()
            piece_type = piece_type_combobox.get()

            # Validación de campos de entrada
            if not piece_amount or not material or not piece_type:
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
                piece_amount = int(piece_amount)
                if piece_amount <= 0:
                    # Si la entrada es un valor menor o igual a cero
                    raise ValueError("La cantidad de piezas debe ser un valor positivo.")
            
            except ValueError as e:
                # Si la entrada es un valor NO NUMÉRICO
                if "invalid literal for int()" in str(e):
                    messagebox.showerror("Error", "La cantidad de piezas debe ser un valor numérico.")
                    clear_fields()
                else:
                    messagebox.showerror("Error", str(e))
                    clear_fields()
                return
            
            # Llamar al método create_order del coordinador
            success, order_data = self.coordinator.create_order(material, piece_type, piece_amount)

        # Regresar
        back_button = tk.Button(create_order_window, text="REGRESAR",  command=lambda: [create_order_window.destroy(), create_order_window.destroy(), self.go_to_main_screen()],bg='white')
        back_button.grid(row=5, column=0,columnspan=2, pady=30,ipady=3,ipadx=10)

        # Botón para crear la orden
        create_order_button = tk.Button(create_order_window, text="CREAR ORDEN", command=create_order,bg='white')
        create_order_button.grid(row=4, column=1,columnspan=5, pady=20,ipady=3,ipadx=80,sticky='E')
        
    def delete_order(self):
        # Lógica para eliminar una orden aquí
        self.delete_order_screen()
        print("Orden eliminada")
   
    def modify_order(self):
        # Lógica para modificar una orden aquí
        self.modify_order_screen()
        print("Orden Modificada")
    
    def modify_storage(self):
        # Lógica para modificar almacen
        self.modify_storage_screen()
        print("Almacen Modificado")

    def print_orders(self):
        pass

    # Volver al menú principal
    def go_to_main_screen(self):
        self.master.deiconify()  # Mostrar la pantalla principal

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
