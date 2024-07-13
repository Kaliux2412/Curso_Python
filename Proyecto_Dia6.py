"""En este proyecto se hara uso de diferente librerías de Python para
abrir y analizar archivos y hacer una interfaz para que el usuario lea y
navegue en archivos de en este caso recetas y pueda modificarlos a su
 antojo desde la consola (MEDIA)"""

import os
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(), 'Recetas')
def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador
#Mostrar menú de inicio
def inicio():
    system('cls')
    print('🍳🍳🍗🍜🍕🧆🍩🍓🍔' * 6)
    print("Bienvenido al administrador de Recetas")
    print('🍳🍳🍗🍜🍕🧆🍩🍓🍔' * 6)
    print('\n')
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"Cantidad de recetas: {contar_recetas(mi_ruta)}")
    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opción:")
        print('''
        [1] - Leer Recetas
        [2] - Crear Receta Nueva
        [3] - Crear Categoría nueva
        [4] - Eliminar Receta
        [5] - Eliminar Categoría
        [6] - Salir del Programa''')
        eleccion_menu = input()
    return int(eleccion_menu)
inicio()

def mostrar_categorias(ruta):
    print("Categorías: ")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1
    return lista_categorias

def elegir_categoría(lista):
    eleccion_correcta = 'x'
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista)+1):
        eleccion_correcta = input("\nElige una Categoría: ")
    return lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print("Recetas: ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    for receta in ruta_recetas.glob("*.txt"):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador +=1
    return lista_recetas

def elegir_recetas(lista):
    eleccion = 'x'
    while not eleccion.isnumeric() or int(eleccion) not in range(1,len(lista) +1):
        eleccion = input("\n Elige una receta: ")
    return  lista[int(eleccion) -1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de tu receta:")
        nombre_receta = input() + '.txt'
        print("Escribe la nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)
        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu recetas {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento esa receta ya existe")
def crear_categoría(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de tu nueva categoría: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)
        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoría {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento esa categoría ya existe")
def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")
def elimar_categoria(categoría):
    Path(categoría).rmdir()
    print(f"La categoría {categoría.name} ha sido elimnada")
def volver_inicio():
    eleccion = "x"
    while eleccion.lower() != "i":
        eleccion = input("\nPresione I para volver al menú inicial:  ")
finalizar_programa = False
while not finalizar_programa:
    menu = inicio()

    if menu == 1:
        mis_categorías = mostrar_categorias(mi_ruta)
        categoria_elegida = elegir_categoría(mis_categorías)
        mis_recetas = mostrar_recetas(categoria_elegida)
        mi_receta = elegir_recetas(mis_recetas)
        leer_receta(mi_receta)
        volver_inicio()
    elif menu == 2:
        mis_categorías = mostrar_categorias(mi_ruta)
        categoria_elegida = elegir_categoría(mis_categorías)
        crear_receta(categoria_elegida)
        volver_inicio()
    elif menu ==3:
        crear_categoría(mi_ruta)
        volver_inicio()
    elif menu == 4:
        mis_categorías = mostrar_categorias(mi_ruta)
        categoria_elegida = elegir_categoría(mis_categorías)
        mis_recetas = mostrar_recetas(categoria_elegida)
        mi_receta = elegir_recetas(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()
    elif menu == 5:
        mis_categorías = mostrar_categorias(mi_ruta)
        categoria_elegida = elegir_categoría(mis_categorías)
        elimar_categoria(categoria_elegida)
        volver_inicio()
    elif menu ==6:
        finalizar_programa = True
