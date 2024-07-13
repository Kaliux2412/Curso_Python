import re
import shutil
import datetime
import math
import time
from pathlib import Path
import os
from os import system
inicio = time.time()

des_instrucciones = shutil.unpack_archive("Proyecto+Dia+9.zip", "Descomprimido", "zip")
direccion = Path("Descomprimido", "Instrucciones.txt")
abrir_instrucciones = open(direccion, "r")
print(abrir_instrucciones.read())
system("cls")

print("Bienvenido al lector de números de serie")
el_patron = r'N\D{3}-\d{5}'

fecha_busqueda = datetime.date.today()

nueva_dir = Path("Descomprimido\Mi_Gran_Directorio")
archivos_encontrados = []
numeros_encontrados = []
def buscar_numero(archivo,patron):
    este_archivo = open(archivo, "r")
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron,texto)
    else:
        return ''
def crear_listas():
    for carpeta, subcarpet, archivo in os.walk(nueva_dir):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta, a), el_patron)
            if resultado != '':
                numeros_encontrados.append(resultado.group())
                archivos_encontrados.append(a.title())
def mostrar_todo():
    indice = 0
    print("-" * 50)
    print(f"Fecha de Búsqueda: {fecha_busqueda.day}/{fecha_busqueda.month}/{fecha_busqueda.year}")
    print("\n")
    print("ARCHIVO\t\t\tNÚMERO DE SERIE")
    print("--------\t\t--------------")
    for a in archivos_encontrados:
        print(f"{a}\t{numeros_encontrados[indice]}")
        indice += 1
    print('\n')
    print(f"Números encontrados: {len(numeros_encontrados)}")
    fin = time.time()
    duracion = fin - inicio
    print(f"Duración de la busqueda: {math.ceil(duracion)} segundos")
crear_listas()
mostrar_todo()

