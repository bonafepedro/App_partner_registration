import tkinter as tk
import os
from tkinter import * 
from tkinter import ttk, Entry, Frame
from PIL import Image, ImageTk
from PIL.ImageTk import PhotoImage
from modelo import Abmc


"""
Este modulo contiene las ventanas de iteracción con el usuario
permitiendole realizar las acciones que desee
de acuerdo a la elección que este realice en la ventana principal.

"""


class VentanaIngresar():
    """
    Esta clase contiene las características visuales de la ventana 
    de ingreso de nuevos socios a la base de datos.
    """
    def __init__(self, ventana):
        self.r = ventana
        self.objeto = Abmc()

        self.frame = Frame(self.r, bg= "LightSlateGray")
        self.frame.pack(expand = True, fill = "both")
        self.r.title('Ingreso de Nuevo Socio')
        self.r.geometry('500x300')
        
        self.create_widgets()


    def create_widgets(self):
        """
        Este método crea los botones y entradas 
        que serán incluidos en la ventana  de ingreso de nuevos socios.
        """

        #Label
        self.label_name = Label(self.frame, text = "Nombre del socio a ingresar:  ", bg= "LightSlateGray", font=("Lato", 11, "bold"), fg= "white")
        self.label_dni = Label(self.frame, text = "Número de DNI:  ", bg= "LightSlateGray", font=("Lato", 11, "bold"), fg= "white")
        self.label_status = Label(self.frame, text = "Tipo de socio:  ", bg= "LightSlateGray", font=("Lato", 11, "bold"), fg= "white")
        self.label_ubication = Label(self.frame, text = "Ubicación:  ", bg= "LightSlateGray", font=("Lato", 11, "bold"), fg= "white")
        self.label_debt = Label(self.frame, text = "Deuda:  ", bg= "LightSlateGray", font=("Lato", 11, "bold"), fg= "white")

        #Entry
        self.entry_name = Entry(self.frame, bg = "LightBlue" )
        self.entry_dni = Entry(self.frame, bg = "LightBlue" )
        self.entry_status = ttk.Combobox(self.frame, state= "readonly")
        self.entry_ubication = ttk.Combobox(self.frame, state= "readonly")
        self.entry_debt = Entry(self.frame, bg = "LightBlue" )

        #BOX Categories
        self.entry_status["values"] = ["Menor", 
                                        "Adulto", 
                                        "Jubilado", 
                                        "Vitalicio", 
                                        "Grupo Familiar"
                                        ]
                                        
        self.entry_ubication["values"] = ["Popular pirata", 
                                        "Popular Preferencial", 
                                        "Cuellar baja", 
                                        "Cuellar Alta", 
                                        "Platea Dorada", 
                                        "Platea Celeste", 
                                        "Palco"
                                        ]


        #Localización
        self.label_name.grid(row = 0, column = 0, pady = 6)
        self.label_dni.grid(row = 1, column = 0, pady = 6)
        self.label_status.grid(row = 2, column = 0,pady = 6)
        self.label_ubication.grid(row = 3, column = 0,pady = 6)
        self.label_debt.grid(row = 4, column = 0,pady = 4)

        self.entry_name.grid(row = 0, column = 1, pady = 6)
        self.entry_dni.grid(row =1, column = 1, pady = 6)
        self.entry_status.grid(row = 2, column = 1, pady = 6)
        self.entry_ubication.grid(row = 3, column = 1, pady = 6)
        self.entry_debt.grid(row = 4, column = 1, pady = 4)

        #Botones
        self.ingr = Button(self.frame,
                        font=("Lato", 11, "bold"), 
                        fg= "Black",
                        text = "Ingresar Socio", 
                        command = lambda: self.agregar()
                        )
        self.ingr.grid(row = 5, column = 1, pady = 0)
           
        #Imagen
        direc_base = os.path.dirname((os.path.abspath(__file__)))
        ruta_estatica = os.path.join(direc_base, "images/thumbs")
        ruta = ruta_estatica + "/logo.png"
        
        self.image2 = Image.open(ruta)
        self.image1 = PhotoImage(self.image2)
        self.widget1 = Label(self.frame, image=self.image1, bg= "LightSlateGray")
        self.widget1.grid(row = 5, column = 0, pady = 0)


    def agregar(self):
        """
        Este método es el encargado de recibir los datos del nuevo socio, validar que sean 
        correctos llamando al método validar del modulo modelo, luego buscar que el socio no exista ya
        mediante el método encontrar_socio del módulo modelo. Finalmente si todo es correcto
        cargarlo a la base de datos pasando la información al método alta del módulo modelo.
        """

        try:
            
            name1 = self.entry_name.get()
            dni1 = self.entry_dni.get()
            status1 = self.entry_status.get()
            ubication1 = self.entry_ubication.get()
            debt1 = self.entry_debt.get()

            valid_name = self.objeto.validar(name1, master = "nombre_apellido")
            valid_dni = self.objeto.validar(dni1, master = "dni")
            valid_deuda = self.objeto.validar(debt1, master = "deuda")
            
            if len(valid_name) != 0:
                tk.messagebox.showerror(title = "Sede Socios CAB informa: ",
             message = "Su incorporación no pudo ser realizada  \nIngrese el nombre correctamente  ")
                self.r.withdraw()
            elif len(valid_dni) !=0:
                tk.messagebox.showerror(title = "Sede Socios CAB informa: ",
             message = "Su incorporación no pudo ser realizada  \nIngrese el dni correctamente \nsin puntos ni espacios ")
                self.r.withdraw()
                
            elif len(valid_deuda) !=0:
                tk.messagebox.showerror(title = "Sede Socios CAB informa: ",
             message = "Su incorporación no pudo ser realizada  \nIngrese la deuda correctamente\n para decimales usar un .")
                self.r.withdraw()
            
            else:
                busqueda = self.objeto.encontrar_socio(dni1)
                if busqueda == None:
                    self.objeto.alta(name1, dni1, status1, ubication1, debt1)
                    tk.messagebox.showinfo(title = "Sede Socios CAB informa: ",
                                        message = "Su incorporación fue realizada con exito"
                                        )
                    self.r.withdraw()
                else:
                    tk.messagebox.showerror(title = "Sede Socios CAB informa: ",
                message = f"Su incorporación no pudo ser realizada  \nEl socio ya existe como {busqueda}")
                    self.r.withdraw()
  
        except (TypeError, NameError, ValueError):
            tk.messagebox.showerror(title = "Sede Socios CAB informa: ",
             message = "Su incorporación no pudo ser realizada  \nIngrese los datos correctamente  ")
            self.r.withdraw()


class Ventanaconsulta:
    """
    Esta clase contiene las características visuales de la ventana 
    de consulta de socios a la base de datos.
    """
    objeto = Abmc()
    def __init__(self, ventana):
        """
        En el momento de ser instanciada la clase genera mediante el método __init__
        la configuración de la ventana y el frame, con título, tamaño, color, etc.
        Luego llama al método widgets que crea los botones y entradas de la ventana. 
        """
        self.ventana = ventana
        self.objeto = Abmc()
        self.ventana.geometry("700x350")
        self.frame = Frame(self.ventana, bg= "LightSlateGray")
        self.frame.pack(expand = True, fill = "both")
        self.ventana.title("Consulta de Socios")

        self.widgets()

    def widgets(self):
        """
        Este método crea los botones y entradas 
        que serán incluidos en la ventana  de consulta de socios.
        """
        #Label
        self.label_dni = Label(self.frame, 
                                text = "DNI del socio que desea consultar ",
                                font=("Lato", 11, "bold"), 
                                fg= "white",
                                bg= "LightSlateGray"
                                )
        #Entry
        self.entry_dni = Entry(self.frame, bg = "LightBlue" )
        #Localización
        self.label_dni.grid(row = 0, column = 0, pady = 6)
        self.entry_dni.grid(row = 0, column = 1, pady = 6)

        #Botones
        self.ingr = Button(self.frame,
                            text = "Consulta Socio", 
                            font=("Lato", 11, "normal"), 
                            fg= "Black",
                            command = lambda: self.consultar()
                            )
        self.ingr.grid(row = 0, column = 2, pady = 10)

        self.fin = Button(self.frame,
                            text = "Finalizar Consulta",
                            font=("Lato", 11, "normal"), 
                            fg= "Black", 
                            command = lambda: self.finalizar()
                            )
        self.fin.grid(row = 3, column = 1, pady = 10)

        #Treview
        self.tree = ttk.Treeview(self.frame)
        self.tree["columns"] = ("col1", "col2", "col3", "col4", "col5")

        self.tree.column("#0", width=50, minwidth=50)  #ID
        self.tree.column("col1", width=200, minwidth=200) # Nombre
        self.tree.column("col2", width=100, minwidth=100)   # DNI
        self.tree.column("col3", width=150, minwidth=150)  # Tipo de socio
        self.tree.column("col4", width=100, minwidth=100) # Ubicación
        self.tree.column("col5", width=100, minwidth=100)  # Deuda

        self.tree.heading("#0", text="ID", anchor=CENTER)
        self.tree.heading("col1", text="Nombre", anchor=CENTER)
        self.tree.heading("col2", text="DNI", anchor=CENTER)
        self.tree.heading("col3", text="Tipo de Socio", anchor=CENTER)
        self.tree.heading("col4", text="Ubicación", anchor=CENTER)
        self.tree.heading("col5", text="Deuda", anchor=CENTER)

        self.tree.grid(column=0, 
                        row=2, 
                        columnspan=5, 
                        padx=2, 
                        pady=2, 
                        sticky="nsew"
                        )

    def consultar(self):
        """
        Este método toma el dni ingresado y se lo envía al método consulta
        del módulo modelo, para efectivizar la consulta, finalmente imprime 
        en pantalla la información consultada.
        """
        valid = self.objeto.validar(self.entry_dni.get(), master = "dni")
        if len(valid) == 0:
            dni = int(self.entry_dni.get())
            
            busqueda = self.objeto.encontrar_socio(dni)
            if busqueda != None:
                self.objeto.actualizar_treeview(self.tree)
                self.consulta = self.objeto.consulta(dni, self.tree)
                
            else:
                tk.messagebox.showerror(title = "Sede Socios CAB informa: ",
                message = "Su busqueda no pudo ser realizada, el socio no existe")
                self.ventana.destroy()
        else:
            tk.messagebox.showerror(title = "Sede Socios CAB informa: ",
                message = "Valores mal ingresados")
            self.ventana.destroy()
        
    def finalizar(self):
        """
        Este método, invocado a travez de un boton en la ventana
        simplemente destruye la ventana cuando el usuario
        desea finalizar la consulta.
        """
        self.ventana.destroy()


class Ventanaborrar:
    """
    Esta clase será la encargada de crear la ventana 
    de borrado y actualización de socios.
    """
    def __init__(self, ventana):
        """
        En el momento de ser instanciada la clase genera mediante el método __init__
        la configuración de la ventana y el frame, con título, tamaño, color, etc.
        Luego llama al método widgets que crea los botones y entradas de la ventana. 
        """
        self.objeto = Abmc()
        self.ventana = ventana
        self.ventana.geometry("500x300")
        self.frame = Frame(self.ventana, bg= "LightSlateGray")
        self.frame.pack(expand = True, fill = "both")
        self.ventana.title("Borrar o Actualizar Socio")
        
        self.widgets()

    def widgets(self):
        """
        Este método crea los botones y entradas 
        que serán incluidos en la ventana  de borrado y actualización de socios.
        """

        #Label
        self.label_dni = Label(self.frame, 
                                text = "DNI del Socio: ", 
                                bg= "LightSlateGray", 
                                font=("Lato", 11, "bold"), 
                                fg= "white"
                                )
        #Entry
        self.entry_dni = Entry(self.frame, bg = "LightBlue" )
        #Localización
        self.label_dni.grid(row = 0, column = 0, padx= 30, pady = 6)
        self.entry_dni.grid(row = 0, column = 1, padx= 10, pady = 6)

        #Botones
        self.ingr = Button(self.frame,
                            text = "Borrar Socio",
                            font=("Lato", 11, "normal"), 
                            fg= "Black",
                            command = lambda: self.borrar()
                            )

        self.ingr.grid(row = 3, column = 0, padx= 30, pady = 10)
        self.ingr = Button(self.frame,
                            text = "Modificar Socio", 
                            font=("Lato", 11, "normal"), 
                            fg= "Black",
                            command = lambda: self.actualizar()
                            )

        self.ingr.grid(row = 3, column = 1, padx= 10, pady = 10)
        
        #Imagen
        direc_base = os.path.dirname((os.path.abspath(__file__)))
        ruta_estatica = os.path.join(direc_base, "images")
        ruta = ruta_estatica + "/logo.png"
        
        self.image2 = Image.open(ruta)
        self.image1 = PhotoImage(self.image2)
        self.widget1 = Label(self.frame, image=self.image1, bg= "LightSlateGray")
        self.widget1.grid(row = 4, column = 1, padx= 0, pady = 10)

    def borrar(self):
        """
        Este método toma el dni ingresado
        valida que sea un dni correcto mediante el metodo validar
        y que sea un socio existente mediante el método encontrar_socio.
        Luego mediante el método baja del módulo modelo, 
        se efectiviza la baja. Finalmente pide una confirmación
        para asegurar la voluntad del usuario de realizar la baja.
        """

        dniaeliminar = (self.entry_dni.get())
        validacion = self.objeto.validar(dniaeliminar, master = "dni")
        if len(validacion) == 0:
                busqueda = self.objeto.encontrar_socio(dniaeliminar)
                if busqueda != None:
                    pregunta= tk.messagebox.askokcancel("Advertencia", 
                                                        "¿Seguro que desea irse de este hermoso club?"
                                                        )
                    if pregunta:
                        self.objeto.baja(dniaeliminar)
                else:
                    tk.messagebox.showerror(title = "Sede Socios CAB informa: ",
                                            message = "Su operación no pudo ser realizada, el socio no existe"
                                            )
                
                self.ventana.destroy()
        else:
            tk.messagebox.showerror(title = "Sede Socios CAB informa: ",
                                    message = "El DNI ingresado no es válido"
                                    )
            self.ventana.destroy()

    def actualizar(self):
        """
        Este método recibe la información a modificar
        tomando como parámetro un dni que utilizará 
        como indicador y la nueva información
        que se introduce en una ventana de dialogo dependiente de la Ventanaborrar
        para enviarla al método modificar del módulo modelo
        el cual realizara las modificaciones deseadas en la base de datos. Previamente
        valida mediante el método validar del modulo modelo que la información sea correcta,
        y mediante el método encontrar_socio también del modulo modelo, que el socio a modificar exista.
        """
        self.dni_socioamodificar = (self.entry_dni.get())

        validacion = self.objeto.validar(self.dni_socioamodificar, master = "dni")

        if len(validacion)!= 0:
            tk.messagebox.showerror("Advertencia", "Valores mal ingresados")
            self.ventana.destroy()
        
        else:
            busqueda = self.objeto.encontrar_socio(self.dni_socioamodificar)
            if busqueda != None:
                win= Toplevel()
                Ventanitamodificar(win,  self.dni_socioamodificar)
         
            else:
                    tk.messagebox.showerror(title = "Sede Socios CAB informa: ",
                    message = "Su operación no pudo ser realizada, el socio no existe")
                           

            self.ventana.destroy()
    
    
class Ventanitamodificar(Ventanaborrar):
    """
    Esta clase contiene las caracteristicas de la ventana de diálogo
    donde se introducirán los nuevos datos del socio que se deseea modificar.
    """
    def __init__(self, ventanaopciones, dni):
        """    
        En el momento de ser instanciada la clase genera mediante el método __init__
        la configuración de la ventana y el frame, con título, tamaño, color, etc.
        Luego llama al método create_widgets que crea los botones y entradas de la ventana. 

        """
        self.win = ventanaopciones
        self.dnimodif = dni
        self.objeto = Abmc()
        self.win.geometry("500x350")
        self.frame = Frame(self.win, bg= "LightSlateGray")
        self.frame.pack(expand = True, fill = "both")
        self.win.title("Modificar Socio")
        self.create_widgets()

    def create_widgets(self):
        """
        Este método crea los botones y entradas 
        que serán incluidos en la ventana.
        """

        #Label
        self.label_newubication = Label(self.frame, 
                                        text = "Nueva ubicación del Socio: ",
                                        bg= "LightSlateGray", 
                                        font=("Lato", 11, "bold"), 
                                        fg= "white"
                                        )

        self.label_newtipe = Label(self.frame, 
                                    text = "Nuevo tipo de Socio: ",
                                    bg= "LightSlateGray", 
                                    font=("Lato", 11, "bold"), 
                                    fg= "white"
                                    )

        self.label_newdebt = Label(self.frame, 
                                    text = "Deuda: ",
                                    bg= "LightSlateGray", 
                                    font=("Lato", 11, "bold"), 
                                    fg= "white"
                                    )

        #Entry
        self.entry_newubication = ttk.Combobox(self.frame, state= "readonly")
        self.entry_newtipe = ttk.Combobox(self.frame, state= "readonly")
        self.entry_newdebt = Entry(self.frame, bg = "LightBlue")

        #BOX Categories
        self.entry_newtipe["values"] = ["Menor", 
                                        "Adulto", 
                                        "Jubilado", 
                                        "Vitalicio", 
                                        "Grupo Familiar"
                                        ]

        self.entry_newubication["values"] = ["Popular pirata", 
                                            "Popular Preferencial", 
                                            "Cuellar baja", 
                                            "Cuellar Alta", 
                                            "Platea Dorada", 
                                            "Platea Celeste", 
                                            "Palco"
                                            ]

        #Localización
        self.label_newubication.grid(row = 0, column = 0, pady = 6)
        self.entry_newubication.grid(row = 0, column = 1, pady = 6)
        self.label_newtipe.grid(row = 1, column = 0, pady = 6)
        self.entry_newtipe.grid(row = 1, column = 1, pady = 6)
        self.label_newdebt.grid(row = 2, column = 0, pady = 6)
        self.entry_newdebt.grid(row = 2, column = 1, pady = 6)

        #Botones
        self.updat1 = Button(self.frame,
                            text = "Modificar",
                            font=("Lato", 11, "normal"), 
                            fg= "Black",
                            command = lambda: self.confirmar(self.dnimodif, 
                                                            self.entry_newubication.get(), 
                                                            self.entry_newtipe.get(), 
                                                            self.entry_newdebt.get()
                                                            )
                            )
        #Localización
        self.updat1.grid(row = 3, 
                        column = 1, 
                        padx= 5, 
                        pady = 5
                        )
        #Imagen
        direc_base = os.path.dirname((os.path.abspath(__file__)))
        ruta_estatica = os.path.join(direc_base, "images")
        ruta = ruta_estatica + "/logo.png"
        
        self.image2 = Image.open(ruta)
        self.image1 = PhotoImage(self.image2)
        self.widget1 = Label(self.frame, image=self.image1, bg= "LightSlateGray")
        self.widget1.grid(row = 4, column = 1, padx= 0, pady= 0)

    def confirmar(self,
                datadni, 
                dataubic, 
                datatipo, 
                datadeuda):
        """
        Este método toma la nueva información registrada por el usuario 
        en la ventana de diálogo y mediante el método modificar del módulo modelo
        actualiza la base de datos del socio correspondiente. Previamente valida que la información
        brindada sea correcta, mediante el método validar del módulo modelo.
        """
        validacion_deuda = self.objeto.validar(datadeuda, master = "deuda")
        if len(validacion_deuda) == 0:
            prueba = self.objeto.modificar(datadni, 
                                        dataubic, 
                                        datatipo, 
                                        datadeuda
                                        )
            if prueba:
                mensaje = tk.messagebox.showinfo("Modificación correcta",
                                                f"El socio ha sido guardado como : {datatipo} "
                                                ) 
            else:
                mensaje2 = tk.messagebox.showinfo("Error", "El socio no ha podido actualizarse correctamente")
            
            self.win.destroy()
        else:
            mensaje2 = tk.messagebox.showerror("Error", "Valores mal ingresados")
