import tkinter as tk
import os
from tkinter import *
from tkinter import font
from modelo import Abmc
from PIL import Image, ImageTk
from PIL.ImageTk import PhotoImage
from ventanasecundaria import VentanaIngresar, Ventanaborrar, Ventanaconsulta 

"""
Esta clase contiene la configuración de la vista principal.
Es la primera interfaz con la que el usuario interactúa y manifiesta
que acción desea realizar. Luego a partir de la decisión del usuario
esta clase instancia a distintas clases de la ventana secundaria de acuerdo
a la decisión elegida. 
"""

class App:
    def __init__(self, window):
        """
        En el momento de ser instanciada esta clase genera la ventana principal
        el frame donde se colocarán los widgets y carga las imágenes para la vista y el 
        ícono. Luego llama a la función crear_thumbs para crear el directorio de imágenes miniatura
        necesario para poder cargar otras imágenes pequeñas en el programa. 
        Finalmente llama a la función crear_widgets que será la encargada de crear la estética
        de la vista principal. 
        """
        self.r = window
        self.objeto = Abmc()
        #self.r.iconbitmap("proyectofinal/logo1.ico")
        self.frame = Frame(self.r, bg= "DeepSkyBlue")
        self.frame.pack(expand = True, fill = "both")
        self.r.title('Bienvenido al portal de Socios del Club Atletico Belgrano')
        self.r.geometry('550x400')

        #Imagen
        BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
        STATIC_ROOT = os.path.join(BASE_DIR, "images")
        ruta = STATIC_ROOT + "/logo.png"

        self.image2 = Image.open(ruta)
        self.image1 = PhotoImage(self.image2)
        self.widget1 = Label(self.frame, image=self.image1, bg= "DeepSkyBlue")
        self.widget1.pack(side = TOP, padx=10, pady=5, expand= TRUE)

        #Ícono
        self.r.iconphoto(True, PhotoImage(self.image2))
   
        #Pregunta
        self.superior = Label(self.frame,
         text = '¿Qué operación desea realizar?',
         bg = "DeepSkyBlue" , fg = "White", width = "90", font=("Lato", 17, "bold")
         ).pack(expand = True, side = TOP)
            
        #Llamada a la funcion que habilita los botones 
        self.create_widgets()

        #Creacion de directorio thumbs imagenes en miniatura
        directorioImagenes = "/home/pedro/Documentos/programacion/python/python_intermedio_UTN/proyecto final/codigo/images/"
        thumbs = self.crear_thumbs(directorioImagenes)
    
    def crear_thumbs(self, directorio, size=(150, 150), subdirectorio='thumbs'):
        """
        Esta función crea el directorio de imágenes miniatura que luego serán utilizadas por el programa
        """
        directorio_para_thumb = os.path.join(directorio, subdirectorio)
        if not os.path.exists(directorio_para_thumb):
            os.mkdir(directorio_para_thumb)

        for imagen in os.listdir(directorio):
            thumbpath = os.path.join(directorio_para_thumb, imagen)
            print('Creando', thumbpath)
            imgpath = os.path.join(directorio, imagen)
            try:
                imgobj = Image.open(imgpath)
                imgobj.thumbnail(size, Image.ANTIALIAS)
                imgobj.save(thumbpath)
            except:
                print("Skipping: ", imgpath)


    def create_widgets(self):
        """
        Esta función es la encargada de crear los botones, Labels y Entry de la vista principal,
        con sus respectivas funciones y configuraciones. 
        """
        #Botones
        self.introduce = Button(self.frame,
                        text = "Ingresar Nuevo Socio", 
                        command = lambda: self.ingresar())
        self.consult = Button(self.frame,
                        text = "Consultar Socio", 
                        command = lambda: self.ventsec1())
        self.delac = Button(self.frame,
                            text = "Borrar / Actualizar Socio", 
                            command = lambda: self.ventsec2())
            
        self.introduce.pack(side=TOP, 
                            fill=BOTH, 
                            expand=True, 
                            padx=10, 
                            pady=5)

        self.consult.pack(side=TOP, 
                        fill=BOTH, 
                        expand=True, 
                        padx=10, 
                        pady=5)

        self.delac.pack(side=TOP, 
                        fill=BOTH, 
                        expand=True,
                        padx=10, 
                        pady=5)
            
    def ingresar(self):
        """
        Ejecuta la ventana secundaria de agregar datos.
        """
        vent = Toplevel()
        VentanaIngresar(vent)
        self.r.iconify()

    def ventsec1(self):
        """
        Ejecuta la ventana secundaria de consultas.
        """
        ventana = Toplevel()
        Ventanaconsulta(ventana)
        self.r.iconify()
        

    def ventsec2 (self):
        """
        Ejecuta la ventana secundaria de borrar y actualizar.
        """
        ventana = Toplevel()
        Ventanaborrar(ventana)
        self.r.iconify()