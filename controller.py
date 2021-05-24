import tkinter as tk
from tkinter import Tk, ttk, messagebox
from vistappal import App

"""
Este modulo simplemente da inicio a la aplicación llamando a la vista
permitiendo la iteracción con el usuario.
"""


if __name__ == "__main__":
	ventana1 = Tk()
	miap = App(ventana1)
	ventana1.mainloop()

