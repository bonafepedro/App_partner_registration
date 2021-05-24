import sqlite3
from sqlite3 import Error
import re

"""
En este modulo se realiza todo el back del crud, contiene metodos que interactúan con la base de datos.
"""

class Abmc():
    """
    Esta clase esta destinada a operar con la base de datos, genera un objeto del tipo Abmc
    cuya caracteristica es la creación e interacción con una base de datos llamada socioscab 
    """
    def __init__(
        self, ):
        """
        En el momento en que se instancia la clase Abmc el método __init__ crea  y configura
        la base de datos si esta no ha sido creada aun, y en caso de presentarse un Error
        lo atrapa e imprime Error. 
        """
        try:
            con = sqlite3.connect('socioscab.db')
            cursorObj = con.cursor()
            cursorObj.execute(
                "CREATE TABLE socios(id integer PRIMARY KEY AUTOINCREMENT, nombre TEXT, dni INTEGER, tipo TEXT, ubicacion TEXT, deuda INTEGER)"
            )
            con.commit()
        except Error:
            print(Error)

    
    def conexion(
    
        self,
    ):
        """
        Este método realiza solamente la conección con la base de datos. 
        """
        con = sqlite3.connect("socioscab.db")
        return con

    def cerrar_conexion(
        self,
    ):
        """
        Este método cierra la conexión a la base de datos
        """
        con = self.conexion()
        con.close()

    def alta(
        self,
        nombre, 
        dni, 
        tipo, 
        ubicacion, 
        deuda):
        """
        Este método recibe parámetros y los agrega a la base de datos.
        """
        
        self.nombre = nombre
        self.dni = dni
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.deuda = deuda
        datos = (self.nombre,
                self.dni, 
                self.tipo, 
                self.ubicacion, 
                self.deuda
                )

        con = self.conexion()
        sql = "INSERT INTO socios(nombre, dni, tipo, ubicacion, deuda) VALUES(?,?,?,?,?) "
        cur = con.cursor()
        cur.execute(sql, datos)
        con.commit()

    
    def baja(self, dnielim):
        """
        Este método recibe como parámetro un numero de dni para utilizarlo como indicador
        y eliminarlo de la base de datos.
        """
        
        datos =dnielim

        con = self.conexion()
        sql = "DELETE FROM socios WHERE dni= ? "
        cur = con.cursor()
        cur.execute(sql, [datos])
        con.commit()
  
    def modificar(
        self, dni_actual, 
        nueva_ubicacion, 
        nuevo_tipo,
        nueva_deuda):
        """
        Este método modifica un elemento de la base de datos
        recibe como parámetro un numero de dni para utilizarlo como indicador
        y la nueva información para dicho elemento.
        """

        self.dni = dni_actual
        self.nueva_ubicacion = nueva_ubicacion
        self.nuevo_tipo = nuevo_tipo
        self.nueva_deuda = nueva_deuda
        datos = (self.nueva_ubicacion, self.nuevo_tipo, self.nueva_deuda, self.dni)
  
        con = self.conexion()
        cur = con.cursor()
        sql = "UPDATE socios SET (ubicacion, tipo, deuda) = (?,?,?) WHERE dni = ?"
        try:
            cur.execute(sql, datos)
            con.commit()
            return True
        except:
            return False
            
    
    def actualizar_treeview(self, mytreeview):
        """
        Este método actualiza el trevieew para que cuando se realicen las consultas 
        se muestre solo el socio consultado. 
        """
        self.mytreeview = mytreeview
        self.registros = self.mytreeview.get_children()
        for self.elemento in self.registros:
            self.mytreeview.delete(self.elemento)

    def consulta(
        self, 
        dni, 
        mytreview):
        """
        Este método recibe como parámetro un numero de dni para utilizarlo como indicador
        y devuelve la información correspondiente a dicho elemento.
        """

        self.mytreeview = mytreview
        con = self.conexion()
        dni= dni
        sql = "SELECT * FROM socios WHERE dni = ? "
        cur = con.cursor()
        cur.execute(sql, [dni])
        research = cur.fetchall()
        
        
        self.mytreeview.insert(
                "",
                0,
                text= research[0][0],
                values=(
                    research[0][1],
                    research[0][2],
                    research[0][3],
                    research[0][4],
                    research[0][5]
                    )
                )
        

    def validar (self, 
                dato, 
                master=None
                ):
        """
        Este método recibe como parámetro un elemento y valida que cumpla las características
        necesarias para cada dato utilizando expresiones regulares.
        """
        self.dato = dato
        if master == "dni":
            c=["error"]
            if len(self.dato)>7 and len(self.dato) <=10:
                patron = re.compile(r'[^\d]')
                test = patron.findall(self.dato)
                return test
            else: return c
            
        if master ==  "nombre_apellido":
            patron = re.compile(r"[^a-zA-Z\süáéíóú]")
            test = patron.findall(self.dato)
            return test

        if master == "deuda":
            patron= re.compile(r'[^\d.]')
            test = patron.findall(self.dato)
            return test


    def encontrar_socio(self, dnibuscado):
        """
        Este método recibe como parametro un dni y verifica que se encuentre en la base de datos
        para luego poder ser utilizado por los otros métodos
        """
        con = self.conexion()
        cur = con.cursor()
        dnibuscado = str(dnibuscado)
        sql2 = "SELECT nombre FROM socios WHERE dni = ? "
        cur.execute(sql2, [dnibuscado])
        research = cur.fetchall()
        
        if research == []:
            return None
        else:
            return (research[0][0])
