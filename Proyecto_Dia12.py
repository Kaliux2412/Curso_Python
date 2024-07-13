from tkinter import *

#iniciar tkinter
aplicacion = Tk()

#tamaño de la ventana
aplicacion.geometry("1020x630+0+0")

#evitar maximizar
aplicacion.resizable(0,0)

#titulo de la ventana
aplicacion.title("Mi Restaurante - Sistema de Pagos")

#color de fondo
aplicacion.config(bg="burlywood")

#evitar que la pantalla cierre
aplicacion.mainloop()