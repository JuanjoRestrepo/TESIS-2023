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

        self.modify_storage_button = tk.Button(self, text="REABASTECER ALMACÉN", command=self.modify_storage,bg="white")
        self.modify_storage_button.grid(row=4, column=3,padx=20, pady=7,ipadx=35, ipady=5)

        self.start_button = tk.Button(self, text="EJECUTAR CELDA", command=self.run,bg="white")
        self.start_button.grid(row=5, column=3,padx=20, pady=7,ipadx=55, ipady=5)

        self.stop_button = tk.Button(self, text="PARADA DE EMERGENCIA", command=self.stop,bg="white")
        self.stop_button.grid(row=6, column=3,padx=20, pady=7,ipadx=32, ipady=5)
     
    def create_order_screen(self):
        # Lógica para crear una orden aquí
        self.master.withdraw()
        create_order_window = tk.Toplevel(self)
        
        #Traer la información necesaria
        base = self.base
        coordinator = self.coordinator

        pieces = (base.get_pieces())
        keys,values= base.get_data('material')
        index= coordinator.Find_Index_Key(keys[0],'Name')
        materials =[]

        for i in values:
            materials.append(i[index]) # Materiales

        
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
        material_combobox = ttk.Combobox(create_order_window, values=materials,background='white')
        material_combobox.grid(row=2, column=3,columnspan=3,pady=7,ipady=3,ipadx=12,sticky='NSEW')

        # Frame para la cantidad de piezas
        piece_type_label = tk.Label(create_order_window, text="PIEZA :",background='white')
        piece_type_label.grid(row=3, column=1,columnspan=2,padx=15,pady=7,ipady=3,sticky='E')
        piece_type_combobox = ttk.Combobox(create_order_window, values=pieces ,background='white')
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
        

            if success:
                # Si la orden se creó exitosamente, crear un objeto Order
                order_details_window = tk.Toplevel(create_order_window)
                order_details_window.title("DETALLES DE LA ORDEN")
                order_details_window.geometry("300x300")
                order_details_window.configure(bg='white')
                
                # Ingresar Logo y Título
                logo = tk.Label(order_details_window, image=self.logo,background='white')
                logo.grid(row=0, column=0,columnspan=2,sticky='NE',ipady=5)

                order_id_label = tk.Label(order_details_window, text="ID :",background='white',foreground='#3B628C')
                order_id_label.grid(row=1, column=0,pady=3,ipady=3,ipadx=12,sticky='NSEW')
                order_id_label2 = tk.Label(order_details_window, text= order_data[0],background='white')
                order_id_label2.grid(row=1, column=1,pady=3,ipady=3,sticky='NSEW')
                
                date_created_label = tk.Label(order_details_window, text="FECHA CREACIÓN :",background='white',foreground='#3B628C')
                date_created_label.grid(row=2, column=0,pady=3,ipady=3,ipadx=12,sticky='NSEW')
                date_created_label2 = tk.Label(order_details_window, text=(order_data[1]),background='white')
                date_created_label2.grid(row=2, column=1,pady=3,ipady=3,sticky='NSEW')

                piece_amount_label = tk.Label(order_details_window, text="CANTIDAD: ",background='white',foreground='#3B628C')
                piece_amount_label.grid(row=3, column=0,pady=3,ipady=3,ipadx=12,sticky='NSEW')
                piece_amount_label2 = tk.Label(order_details_window, text=(order_data[5]),background='white')
                piece_amount_label2.grid(row=3, column=1,pady=3,ipady=3,sticky='NSEW')
                
                material_label = tk.Label(order_details_window, text="MATERIAL :",background='white',foreground='#3B628C')
                material_label.grid(row=4, column=0,pady=3,ipady=3,ipadx=12,sticky='NSEW')
                material_label2 = tk.Label(order_details_window, text=(order_data[4]),background='white')
                material_label2.grid(row=4, column=1,pady=3,ipady=3,sticky='NSEW')

                piece_type_label = tk.Label(order_details_window, text="PIEZA :",background='white',foreground='#3B628C')
                piece_type_label.grid(row=5, column=0,pady=3,ipady=3,ipadx=12,sticky='NSEW')
                piece_type_label2 = tk.Label(order_details_window, text=(order_data[3]),background='white')
                piece_type_label2.grid(row=5, column=1,pady=3,ipady=3,sticky='NSEW')
                
                close_button = tk.Button(order_details_window, text="CERRAR", command=order_details_window.destroy,background='white')
                close_button.grid(row=6, column=0,columnspan=2,pady=7,ipady=3,sticky='NS')
            else:
                messagebox.showerror("Error", "No hay suficientes piezas en el almacén.")

            # Limpiar campos de entrada
            clear_fields()

        # Regresar
        back_button = tk.Button(create_order_window, text="REGRESAR",  command=lambda: [create_order_window.destroy(), create_order_window.destroy(), self.go_to_main_screen()],bg='white')
        back_button.grid(row=5, column=0,columnspan=2, pady=30,ipady=3,ipadx=10)

        # Botón para crear la orden
        create_order_button = tk.Button(create_order_window, text="CREAR ORDEN", command=create_order,bg='white')
        create_order_button.grid(row=4, column=1,columnspan=5, pady=20,ipady=3,ipadx=80,sticky='E')
        
    def delete_order(self):
        # Lógica para eliminar una orden aquí
        self.master.withdraw()
        delete_order_window = tk.Toplevel(self)

        #Traer la información necesaria
        coordinator = self.coordinator

        def getID():
            return(coordinator.get_ID())
        
        
        # Centrar la ventana de eliminar ordenes
        width = delete_order_window.winfo_screenwidth()
        height = delete_order_window.winfo_screenheight()
        x = (width - 600) // 2
        y = (height - 400) // 2
        delete_order_window.geometry("600x400+{}+{}".format(x, y))
        delete_order_window.title("ELIMINAR ORDEN")
        delete_order_window.configure(bg='white')

        # Ingresar Logo y Título
        logo = tk.Label(delete_order_window, image=self.logo,background='white')
        logo.grid(row=0, column=5,sticky='NE',pady=30)
        titulo = tk.Label(delete_order_window, text="ELIMINAR ORDEN",background='white',foreground='#3B628C',anchor='e')
        titulo.grid(row=0, column=0,padx=20,pady=30,ipadx=15,sticky='W')

        # Frame para seleccionar la orden a eliminar
        order_label = tk.Label(delete_order_window, text="Seleccione la Orden a Eliminar:")
        order_label.grid(row=1, column=0,columnspan=2,padx=20,pady=3,ipady=3,sticky='E')
        order_combobox = ttk.Combobox(delete_order_window, values= getID())
        order_combobox.grid(row=1, column=2,columnspan=3,ipadx=30,pady=3,ipady=3,sticky='NSEW')

        date_created_label = tk.Label(delete_order_window, text="FECHA CREACIÓN",background='white',foreground='#3B628C')
        date_created_label.grid(row=2, column=0,pady=3,ipady=3,padx=20,sticky='W')

        piece_amount_label = tk.Label(delete_order_window, text="CANTIDAD",background='white',foreground='#3B628C')
        piece_amount_label.grid(row=3, column=0,pady=3,ipady=3,padx=20,sticky='W')
                
        material_label = tk.Label(delete_order_window, text="MATERIAL",background='white',foreground='#3B628C')
        material_label.grid(row=4, column=0,pady=3,ipady=3,padx=20,sticky='W')

        piece_type_label = tk.Label(delete_order_window, text="PIEZA",background='white',foreground='#3B628C')
        piece_type_label.grid(row=5, column=0,pady=3,ipady=3,padx=20,sticky='W')

        def select_order():
            order = order_combobox.get()

            if not order:
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
            
            key,value = coordinator.information_order(order)

            amount = value[coordinator.Find_Index_Key(key,'Amount')]
            material = value[coordinator.Find_Index_Key(key,'Material')]
            piece = value[coordinator.Find_Index_Key(key,'Piece')]
            date = value[coordinator.Find_Index_Key(key,'Create_Date')]

            date_created_label2 = tk.Label(delete_order_window,text=date,background='white')
            date_created_label2.grid(row=2, column=2,pady=3,ipady=3,sticky='E')

            piece_amount_label2 = tk.Label(delete_order_window,text=amount,background='white')
            piece_amount_label2.grid(row=3, column=2,pady=3,ipady=3,sticky='E')

            material_label2 = tk.Label(delete_order_window,text=material,background='white')
            material_label2.grid(row=4, column=2,pady=3,ipady=3,sticky='E')

            piece_type_label2 = tk.Label(delete_order_window,text=piece,background='white')
            piece_type_label2.grid(row=5, column=2,pady=3,ipady=3,sticky='E')

            def delete_order():
                confirm = messagebox.askyesno("Confirmación", "¿Estás seguro de que quieres eliminar esta orden?")
                if confirm:
                    order = order_combobox.get()
                    text= coordinator.delete_order(order)

                    mensaje_message = tk.Toplevel(delete_order_window)
                    width = mensaje_message.winfo_screenwidth()
                    height = mensaje_message.winfo_screenheight()
                    x = (width - 200) // 2
                    y = (height - 100) // 2
                    mensaje_message.geometry("500x100+{}+{}".format(x, y))
                    mensaje_message.title("MENSAJE")
                    mensaje_message_label = tk.Label(mensaje_message, text=text)
                    mensaje_message_label.pack(side="top", pady=5)
                    mensaje_message_button = tk.Button(mensaje_message, text="Aceptar", command=lambda:[mensaje_message.destroy(),delete_order_button.destroy(),
                                                                                            order_combobox.set(''),piece_type_label2.destroy(),piece_amount_label2.destroy(),
                                                                                            material_label2.destroy(),date_created_label2.destroy()])
                    mensaje_message_button.pack(side="bottom", pady=10)
                   

        


            # Botón para eliminar Orden
            delete_order_button = tk.Button(delete_order_window, text="ELIMINAR ORDEN", command= delete_order,bg='white')
            delete_order_button.grid(row=6, column=5,padx=20, pady=3,ipady=3,sticky='E')
            
        # Botón para seleccionar Orden
        select_order_button = tk.Button(delete_order_window, text="SELECCIONAR", command= select_order,bg='white')
        select_order_button.grid(row=1, column=5,padx=20, pady=3,ipady=3,sticky='E')

        # Regresar
        back_button = tk.Button(delete_order_window, text="REGRESAR",  command=lambda: [delete_order_window.destroy(), delete_order_window.destroy(), self.go_to_main_screen()],bg='white')
        back_button.grid(row=7, column=0,columnspan=2, pady=30,ipady=3,padx=20,sticky='NSEW')


   
    def modify_order(self):

        # Lógica para eliminar una orden aquí
        self.master.withdraw()
        modified_order_window = tk.Toplevel(self)

        #Traer la información necesaria
        coordinator = self.coordinator
        base = self.base
        orders_ID = coordinator.get_ID()
        
        # Centrar la ventana de eliminar ordenes
        width = modified_order_window.winfo_screenwidth()
        height = modified_order_window.winfo_screenheight()
        x = (width - 600) // 2
        y = (height - 400) // 2
        modified_order_window.geometry("600x400+{}+{}".format(x, y))
        modified_order_window.title("MODIFICAR ORDEN")
        modified_order_window.configure(bg='white')

        # Ingresar Logo y Título
        logo = tk.Label(modified_order_window, image=self.logo,background='white')
        logo.grid(row=0, column=5,sticky='NE',pady=30)
        titulo = tk.Label(modified_order_window, text="MODIFICAR ORDEN",background='white',foreground='#3B628C',anchor='e')
        titulo.grid(row=0, column=0,padx=20,pady=30,ipadx=15,sticky='W')

        # Frame para seleccionar la orden a eliminar
        order_label = tk.Label(modified_order_window, text="Seleccione la Orden a Modificar:")
        order_label.grid(row=1, column=0,columnspan=2,padx=20,pady=3,ipady=3,sticky='E')
        order_combobox = ttk.Combobox(modified_order_window, values= orders_ID)
        order_combobox.grid(row=1, column=2,columnspan=3,ipadx=30,pady=3,ipady=3,sticky='NSEW')

        piece_amount_label = tk.Label(modified_order_window, text="CANTIDAD",background='white',foreground='#3B628C')
        piece_amount_label.grid(row=2, column=0,pady=3,ipady=3,padx=20,sticky='W')
                
        material_label = tk.Label(modified_order_window, text="MATERIAL",background='white',foreground='#3B628C')
        material_label.grid(row=3, column=0,pady=3,ipady=3,padx=20,sticky='W')

        piece_type_label = tk.Label(modified_order_window, text="PIEZA",background='white',foreground='#3B628C')
        piece_type_label.grid(row=4, column=0,pady=3,ipady=3,padx=20,sticky='W')

        def select_order():
            order = order_combobox.get()

            if not order:
                error_message = tk.Toplevel(modified_order_window)
                
                # Centrar la ventana de mensaje de eliminar ordenes
                width = modified_order_window.winfo_screenwidth()
                height = modified_order_window.winfo_screenheight()
                x = (width - 200) // 2
                y = (height - 100) // 2
                error_message.geometry("200x100+{}+{}".format(x, y))
                error_message.title("Error")
                error_label = tk.Label(error_message, text="Debe seleccionar una orden.")
                error_label.pack(side="top", pady=10)
                error_button = tk.Button(error_message, text="Aceptar", command=error_message.destroy)
                error_button.pack(side="bottom", pady=10)
                return
            
            key,value = coordinator.information_order(order)

            amount = value[coordinator.Find_Index_Key(key,'Amount')]
            material = value[coordinator.Find_Index_Key(key,'Material')]
            piece = value[coordinator.Find_Index_Key(key,'Piece')]

            
            nested_list = (base.get_pieces())
            exist_pieces = [piece for sublist in nested_list for piece in sublist]
            keys,values= base.get_data('material')
            index= coordinator.Find_Index_Key(keys[0],'Name')
            exist_materials =[]

            for i in values:
                exist_materials.append(i[index]) # Materiales

            piece_amount_label2 = tk.Label(modified_order_window,text=amount,background='white')
            piece_amount_label2.grid(row=2, column=2,pady=3,ipady=3,sticky='W')

            material_label2 = tk.Label(modified_order_window,text=material,background='white')
            material_label2.grid(row=3, column=2,pady=3,ipady=3,sticky='W')

            piece_type_label2 = tk.Label(modified_order_window,text=piece,background='white')
            piece_type_label2.grid(row=4, column=2,pady=3,ipady=3,sticky='W')

            amount_entry = tk.Entry(modified_order_window,text='',background='white')
            amount_entry.grid(row=2, column=3,pady=3,ipady=3,sticky='E')

            material_combobox = ttk.Combobox(modified_order_window, values= exist_materials,background='white')
            material_combobox.grid(row=3, column=3,pady=3,ipady=3,sticky='E')

            piece_combobox = ttk.Combobox(modified_order_window, values= exist_pieces,background='white')
            piece_combobox.grid(row=4, column=3,pady=3,ipady=3,sticky='E')


            def modified_order():
                new_piece= piece_combobox.get()
                new_amount= amount_entry.get()
                new_material= material_combobox.get()

                # Validación de campos de entrada
                if not new_amount or not new_material or not new_piece:
                    error_message = tk.Toplevel(modified_order_window)

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
                    new_amount = int(new_amount)
                    if new_amount <= 0:
                        # Si la entrada es un valor menor o igual a cero
                        raise ValueError("La cantidad de piezas debe ser un valor positivo.")
            
                except ValueError as e:
                    # Si la entrada es un valor NO NUMÉRICO
                    if "invalid literal for int()" in str(e):
                        messagebox.showerror("Error", "La cantidad de piezas debe ser un valor numérico.")
                        material_combobox.set('')
                        piece_combobox.set('')
                        amount_entry.set('')
                    else:
                        messagebox.showerror("Error", str(e))
                        material_combobox.set('')
                        piece_combobox.set('')
                        amount_entry.set('')
                    return
            
                confirm = messagebox.askyesno("Confirmación", "¿Estás seguro de que quieres modificar esta orden?")
                cmaterial = cpiece= camount = False

                if confirm:

                    if material == new_material:
                        cmaterial=False
                    else:
                        cmaterial= True

                    if piece == new_piece:
                        cpiece=False
                    else:
                        cpiece= True

                    if int(amount) == int(new_amount):
                        camount = False
                    else:
                        camount = True

                    text= coordinator.modify_order(order,new_piece,new_material,new_amount,cpiece,cmaterial,camount)
                    
                    mensaje_message = tk.Toplevel(modified_order_window)
                    width = mensaje_message.winfo_screenwidth()
                    height = mensaje_message.winfo_screenheight()
                    x = (width - 200) // 2
                    y = (height - 100) // 2
                    mensaje_message.geometry("600x100+{}+{}".format(x, y))
                    mensaje_message.title("MENSAJE")
                    mensaje_message_label = tk.Label(mensaje_message, text=text)
                    mensaje_message_label.pack(side="top", pady=5)
                    mensaje_message_button = tk.Button(mensaje_message, text="Aceptar", command=lambda:[mensaje_message.destroy(),delete_order_button.destroy(),
                                                                                            material_combobox.destroy(),piece_combobox.destroy(),
                                                                                            amount_entry.destroy(),order_combobox.set('')])
                    mensaje_message_button.pack(side="bottom", pady=10)
                    

            # Botón para eliminar Orden
            delete_order_button = tk.Button(modified_order_window, text="MODIFICAR ORDEN", command= modified_order,bg='white')
            delete_order_button.grid(row=5, column=5,padx=20, pady=3,ipady=3,sticky='E')
            
        # Botón para seleccionar Orden
        select_order_button = tk.Button(modified_order_window, text="SELECCIONAR", command= select_order,bg='white')
        select_order_button.grid(row=1, column=5,padx=20, pady=3,ipady=3,sticky='E')

        # Regresar
        back_button = tk.Button(modified_order_window, text="REGRESAR",  command=lambda: [modified_order_window.destroy(), modified_order_window.destroy(), self.go_to_main_screen()],bg='white')
        back_button.grid(row=7, column=0,columnspan=2, pady=30,ipady=3,padx=20,sticky='NSEW')
    
    def modify_storage(self):
        # Lógica para modificar almacen
        coordinator = self.coordinator
        base = self.base
        import Storage_Refill

        confirm = messagebox.askyesno("Confirmación", "¿Estás seguro de que quieres eliminar esta orden?")

        if confirm:
            available_E = '15'
            available_A = '10'
            locations_E = '[[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]]'
            locations_A = '[[1,1],[1,2],[2,1],[2,2],[3,1],[3,2],[4,1],[4,2],[5,1],[5,2]]'
            used_A = '[]'
            used_E = '[]'

            base.update_data('Empack','material',[available_E,locations_E,used_E,str(datetime.now())],['Available','Location','Used','Update_Date'])
            base.update_data('Aluminio','material',[available_A,locations_A,used_A,str(datetime.now())],['Available','Location','Used','Update_Date'])

            created = coordinator.get_ID()

            for i in created:

                key,value = coordinator.information_order(i)
                amount = value[coordinator.Find_Index_Key(key,'Amount')]
                material = value[coordinator.Find_Index_Key(key,'Material')]
                
                confirm2 = coordinator.modify_storage(material,int(amount),i)

                if confirm2:
                    Storage_Refill.Storage()
        
    def print_orders(self):
        
        # Crear una ventana para mostrar las órdenes
        self.master.withdraw()
        orders_window = tk.Toplevel(self)
        orders_window.title("ÓRDENES")
        orders_window.configure(bg='white')
        
        # Centrar la ventana
        width = orders_window.winfo_screenwidth()
        height = orders_window.winfo_screenheight()
        x = (width - 1000) // 2
        y = (height - 400) // 2
        orders_window.geometry("1000x400+{}+{}".format(x, y))

        # Ingresar Logo 
        logo = tk.Label(orders_window, image=self.logo,background='white')
        logo.grid(row=0, column=0,columnspan=2,sticky='NE',pady=12)
        titulo = tk.Label(orders_window, text="DETALLES DE ÓRDENES",background='white',foreground='#3B628C',anchor='e')
        titulo.grid(row=0,column=0,pady=12,padx=12,sticky='W')
        
        coordinator = self.coordinator
        orders = coordinator.get_orders()
        orders= sorted(orders, key=lambda x: (x[4]),reverse=True)

        # Mostrar el encabezado de la tabla de órdenes
        columns =["ID ORDEN",'CANTIDAD','MATERIAL','PIEZA','FECHA CREACIÓN','STATUS']
   
        tv = ttk.Treeview(orders_window,columns=columns, show='headings')
        tv.tag_configure("Black.Treeview.Column", foreground="black")
        for i in columns:
            tv.column(i,width=155,anchor='center')
        
        for order in orders:
            tv.insert('',tk.END,values=order)
        
        tv.grid(row=1, column=0, sticky='NSEW',padx=10)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(orders_window, orient=tk.VERTICAL, command=tv.yview)
        tv.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky='ns')

        # Regresar
        back_button = tk.Button(orders_window, text="REGRESAR",  command=lambda: [orders_window.destroy(), orders_window.destroy(), self.go_to_main_screen()],bg='white')
        back_button.grid(row=2, column=0,columnspan=2, pady=40,ipady=3,ipadx=15,sticky='E',padx=10)


    # Volver al menú principal
    def go_to_main_screen(self):
        self.master.deiconify()  # Mostrar la pantalla principal

    def run(self):
        pass

    def stop(self):
        pass

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()