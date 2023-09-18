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
    
    def delete_order_screen(self):
        pass
        """
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
        order_combobox = ttk.Combobox(order_frame, values=[order.order_id for order in self.orders])
        order_combobox.pack(side="left")
        
        # Regresar
        back_button = tk.Button(delete_order_window, text="Regresar a pantalla principal", command=lambda: [delete_order_window.destroy(), delete_order_window.destroy(), self.go_to_main_screen()])
        back_button.pack(side="bottom", pady=10)
        def delete_order():
            if not order_combobox.get():
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
            
            confirm = messagebox.askyesno("Confirmación", "¿Estás seguro de que quieres eliminar esta orden?")
            if confirm:
                selected_order = self.orders[order_combobox.current()]
                selected_order_id = selected_order.order_id
                
                # Eliminar la orden de la lista de órdenes
                self.orders.remove(selected_order)
                
                # Cerrar la ventana de Eliminar Orden y volver a la pantalla principal
                print("Orden Eliminada: Orden {}".format(selected_order_id))
                deleted_order_message = tk.Toplevel(delete_order_window)
                deleted_order_message.title("Orden Eliminada")
                deleted_order_message.geometry("400x200")
                deleted_order_message.resizable(False, False)
                width = deleted_order_message.winfo_screenwidth()
                height = deleted_order_message.winfo_screenheight()
                x = (width - 400) // 2
                y = (height - 200) // 2
                deleted_order_message.geometry("+{}+{}".format(x, y))
                deleted_order_label = tk.Label(deleted_order_message, text="Orden Eliminada: Orden {}".format(selected_order_id))
                deleted_order_label.pack(side="top", pady=10)
                deleted_order_button = tk.Button(deleted_order_message, text="Aceptar", command=lambda: [deleted_order_message.destroy(), delete_order_window.destroy(), self.go_to_main_screen()])
                deleted_order_button.pack(side="bottom", pady=10)
        
        # Botón para eliminar la orden
        delete_order_button = tk.Button(delete_order_window, text="Eliminar Orden", command=delete_order)
        delete_order_button.pack(side="bottom", pady=10)
        """
    
    def modify_order_screen(self):
        pass
        """
        # Crear una ventana para modificar una orden existente
        self.master.withdraw()
        modify_order_window = tk.Toplevel(self)
        modify_order_window.title("Modificar Orden")
        # Centrar la ventana
        width = modify_order_window.winfo_screenwidth()
        height = modify_order_window.winfo_screenheight()
        x = (width - 450) // 2
        y = (height - 350) // 2
        modify_order_window.geometry("450x350+{}+{}".format(x, y))
        # Label y ComboBox para seleccionar la orden a modificar
        select_order_label = tk.Label(modify_order_window, text="Seleccione una orden:")
        select_order_label.pack(side="top", pady=10)
        # Botón para regresar al menú principal
        back_button = tk.Button(modify_order_window, text="Regresar al menú principal", command=lambda: [modify_order_window.destroy(), self.master.deiconify()],)
        back_button.pack(side="bottom", pady=10)
        order_ids = [order.order_id for order in self.orders]
        selected_order_id = tk.StringVar(modify_order_window)
        if order_ids:
            # asegurarse de que la lista order_ids no esté vacía antes de intentar establecer el primer elemento en selected_order_id. 
            # Si la lista está vacía, no se establece ningún valor inicial en el Combobox.
            selected_order_id.set(order_ids[0]) # Establecer el primer elemento solo si la lista no está vacía
        order_combobox = ttk.Combobox(modify_order_window, textvariable=selected_order_id, values=order_ids)
        order_combobox.pack(side="top", pady=10)
        # Función para mostrar los detalles de la orden seleccionada
        def show_order_details():
            order_id = selected_order_id.get()
            found_order = None
            for order in self.orders:
                if order.order_id == order_id:
                    found_order = order
                    break
            if found_order:
                # Crear la pantalla de modificación de orden con los datos de la orden cargados
                modify_order_details_window = tk.Toplevel()
                modify_order_details_window.title("Detalles de la Orden")
                # Centrar la ventana
                width = modify_order_details_window.winfo_screenwidth()
                height = modify_order_details_window.winfo_screenheight()
                x = (width - 450) // 2
                y = (height - 350) // 2
                modify_order_details_window.geometry("450x350+{}+{}".format(x, y))
                # Mostrar el ID de la orden
                order_id_label = tk.Label(modify_order_details_window, text="ID de la Orden: {}".format(found_order.order_id))
                order_id_label.pack(side="top", pady=10)
                # Frame para la cantidad de piezas
                piece_amount_frame = tk.Frame(modify_order_details_window)
                piece_amount_frame.pack(side="top", pady=10)
                piece_amount_label = tk.Label(piece_amount_frame, text="Cantidad de Piezas:")
                piece_amount_label.pack(side="left")
                piece_amount_entry = tk.Entry(piece_amount_frame)
                piece_amount_entry.pack(side="left")
                # Frame para el tipo de material
                material_frame = tk.Frame(modify_order_details_window)
                material_frame.pack(side="top", pady=10)
                material_label = tk.Label(material_frame, text="Tipo de Material:")
                material_label.pack(side="left")
                material_combobox = ttk.Combobox(material_frame, values=["Aluminio", "Empack"])
                material_combobox.pack(side="left")
                # Frame para el tipo de pieza
                piece_type_frame = tk.Frame(modify_order_details_window)
                piece_type_frame.pack(side="top", pady=10)
                piece_type_label = tk.Label(piece_type_frame, text="Tipo de Pieza:")
                piece_type_label.pack(side="left")
                piece_type_combobox = ttk.Combobox(piece_type_frame, values=["Pieza1", "Pieza2","Pieza3"])
                piece_type_combobox.pack(side="left")
                # Asignar los valores actuales de la orden a los campos correspondientes
                piece_amount_entry.insert(0, found_order.piece_amount)
                material_combobox.set(found_order.material)
                piece_type_combobox.set(found_order.piece_type)
                # Botón para guardar los cambios realizados a la orden
                def save_changes():
                    try:
                        new_piece_amount_str = piece_amount_entry.get()
                        new_piece_amount = int(new_piece_amount_str)  # Convertir a entero
                        new_material = material_combobox.get()
                        new_piece_type = piece_type_combobox.get()

                        if not new_piece_amount_str.isdigit() or new_piece_amount <= 0:
                            messagebox.showerror("Error", "La cantidad de piezas debe ser un valor positivo.")
                            return
                        
                        # Obtener la orden seleccionada para modificar
                        selected_order = None
                        for order in self.orders:
                            if order.order_id == selected_order_id.get():
                                selected_order = order
                                break
                        
                        if not selected_order:
                            messagebox.showerror("Error", "La orden seleccionada no existe.")
                            return

                        # Restar las piezas anteriores al almacén según corresponda
                        difference =  selected_order.piece_amount - new_piece_amount
                        if difference > 0:
                            # Verificar si hay suficientes piezas en el almacén para realizar el cambio
                            if self.warehouse.get_pieces(new_material) < difference:
                                messagebox.showerror("Error", "No hay suficientes piezas en el almacén para completar la modificación.")
                                return
                            else:
                                self.warehouse.add_pieces(new_material, -difference)

                        elif difference < 0:
                            self.warehouse.add_pieces(new_material, difference)

                        # Actualizar los datos de la orden con los cambios realizados
                        selected_order.piece_amount = new_piece_amount
                        selected_order.material = new_material
                        selected_order.piece_type = new_piece_type
                        selected_order.update_id()
                        messagebox.showinfo("Orden Modificada", f"Orden {selected_order.order_id} modificada exitosamente.")
                        modify_order_details_window.destroy()
                        modify_order_window.destroy()
                        self.master.deiconify()
                    except ValueError as e:
                        if "invalid literal for int()" in str(e):
                            messagebox.showerror("Error", "La cantidad de piezas debe ser un valor numérico.")
                        else:
                            messagebox.showerror("Error", str(e))
                #clear_fields()   
                save_button = tk.Button(modify_order_details_window, text="Guardar Cambios", command=save_changes)
                save_button.pack(side="top", pady=10)
            else:
                messagebox.showerror("Error", "La orden no existe.")
        # Botón para mostrar los detalles de la orden seleccionada
        details_button = tk.Button(modify_order_window, text="Mostrar Detalles de la Orden", command=show_order_details)
        details_button.pack(side="top", pady=10)
        # Función para mostrar una lista de todas las órdenes
        def show_orders():
            orders_list_window = tk.Toplevel()
            orders_list_window.title("Lista de Órdenes")
            # Centrar la ventana
            width = orders_list_window.winfo_screenwidth()
            height = orders_list_window.winfo_screenheight()
            x = (width - 450) // 2
            y = (height - 350) // 2
            orders_list_window.geometry("450x350+{}+{}".format(x, y))
            # Crear una tabla para mostrar las órdenes
            table_frame = tk.Frame(orders_list_window)
            table_frame.pack(side="top", padx=10, pady=10)
            table_headers = ["ID de la Orden", "Producto", "Cantidad de Piezas"]
            table = ttk.Treeview(table_frame, columns=table_headers, show="headings")
            table.pack(side="left")
            # Configurar el scrollbar
            scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
            scrollbar.pack(side="right", fill="y")
            table.configure(yscrollcommand=scrollbar.set)
            # Agregar los encabezados a la tabla
            for header in table_headers:
                table.heading(header, text=header, anchor="center")
                table.column(header, anchor="center")
            # Agregar las órdenes a la tabla
            for order in self.orders:
                table.insert("", "end", values=(order.order_id, order.product, order.piece_amount_amount))
            
            # Botón para cerrar la ventana de la lista de órdenes
            close_button = tk.Button(orders_list_window, text="Cerrar", command=self.go_to_main_screen())
            close_button.pack(side="bottom", pady=10)
            """
    
    def modify_storage_screen(self):
        pass
        """
        self.master.withdraw()
        modify_storage_window = tk.Toplevel(self.master)
        # Centrar la ventana de modificar almacén
        width = modify_storage_window.winfo_screenwidth()
        height = modify_storage_window.winfo_screenheight()
        x = (width - 400) // 2
        y = (height - 300) // 2
        modify_storage_window.geometry("400x300+{}+{}".format(x, y))
        modify_storage_window.title("Modificar Almacén")
        # Etiquetas y campos de entrada para la cantidad de piezas de cada tipo de material
        aluminum_label = tk.Label(modify_storage_window, text="Piezas de Aluminio:")
        aluminum_label.pack(side="top", pady=10)
        aluminum_entry = tk.Entry(modify_storage_window)
        aluminum_entry.pack(side="top", pady=5)
        empack_label = tk.Label(modify_storage_window, text="Piezas de Empack:")
        empack_label.pack(side="top", pady=10)
        empack_entry = tk.Entry(modify_storage_window)
        empack_entry.pack(side="top", pady=5)
        # Crear etiquetas para mostrar las cantidades actuales en el almacén
        self.aluminum_pieces_label = tk.Label(modify_storage_window, text="Cantidad de Piezas de Aluminio: {}".format(self.warehouse.get_pieces("Aluminio")))
        self.aluminum_pieces_label.pack(side="top", pady=5)
        self.empack_pieces_label = tk.Label(modify_storage_window, text="Cantidad de Piezas de Empack: {}".format(self.warehouse.get_pieces("Empack")))
        self.empack_pieces_label.pack(side="top", pady=5)
        # Limpiar los campos de entrada
        def clear_fields_warehouse():
            aluminum_entry.delete(0, tk.END)
            empack_entry.delete(0, tk.END)
        def save_changes():
            try:
                aluminum_pieces = int(aluminum_entry.get())
                empack_pieces = int(empack_entry.get())
                if aluminum_pieces < 0 or empack_pieces < 0:
                    messagebox.showerror("Error", "La cantidad de piezas debe ser un valor positivo.")
                    return
                # Actualizar la cantidad de piezas en el almacén
                self.warehouse.add_pieces("Aluminio", aluminum_pieces)
                self.warehouse.add_pieces("Empack", empack_pieces)
                # Actualizar las etiquetas con las nuevas cantidades
                self.aluminum_pieces_label.config(text="Cantidad Actual de Piezas de Aluminio: {}".format(self.warehouse.get_pieces("Aluminio")))
                self.empack_pieces_label.config(text="Cantidad Actual de Piezas de Empack: {}".format(self.warehouse.get_pieces("Empack")))
                # Mostrar mensaje de confirmación
                messagebox.showinfo("Modificación de Almacén", "La cantidad de piezas en el almacén se ha actualizado correctamente.")
                
            except ValueError:
                messagebox.showerror("Error", "La cantidad de piezas debe ser un valor numérico.")
            clear_fields_warehouse()
        # Botón para guardar los cambios
        save_button = tk.Button(modify_storage_window, text="Guardar Cambios", command=save_changes)
        save_button.pack(side="top", pady=10)
        back_button = tk.Button(modify_storage_window, text="Regresar al menú principal", command=lambda: [modify_storage_window.destroy(), modify_storage_window.destroy(), self.go_to_main_screen()])
        back_button.pack(side="bottom", pady=10)
        """