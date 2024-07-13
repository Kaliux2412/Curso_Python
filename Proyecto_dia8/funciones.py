import numeros
from os import system
print("Bienvenido a Farmacia Guadalajara!")
print("Actualmente contamos con 3 secciones ;)")
def inicio():
    while True:
        print("""
            F - FARMACIA, 
            C - COSMETICA,
            A - ALIMENTOS""")
        try:
            eleccion = input("Escoge la letra de la sección a la que quieres ir: ").upper()
            ["A","F","C"].index(eleccion)
        except ValueError:
            print("Su elección no está dentro del rango de áreas")
        else:
            break
    system("cls")
    numeros.decorador(eleccion)


def entrega():
    while True:
        inicio()
        try:
            otro_turno = input("¿Quieres sacar otro turno? [S] para sí y [N] para no: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opción valida")
            system("cls")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break
entrega()
