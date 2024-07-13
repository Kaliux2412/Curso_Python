"""Este día vamos a hacer que python lea, acceda y analice los archivos
de nuestra computadora"""

mi_archivo = open('archivo.txt')
print(mi_archivo.read())
mi_archivo.close()

from os import system
nombre = input("Dime tu nombre: ")
edad= input("Edad: ")

system('cls')
print(f"TU nombre es {nombre} y tines {edad} años")
from pathlib import Path
home = Path.home()
ruta = Path(home,"Curso Python",
"Día 6",
"practicas_path.py")

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
re = open("registro.txt","a")
for l in registro_ultima_sesion:
   re.writelines(l + '\t')
re.close()
nu = open("registro.txt","r")
print(nu.read())