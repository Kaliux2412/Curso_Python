"""PROYECTO DEL DÍA 4: ADIVINA EL NÚMERO (MEDIA)"""
from random import *
print("Bienvenido a 'Adivina el Número', el cual es un juego en donde tendrás que adivinar en que número estoy pensado")
empezar = input("¿Estas isto?: ")
if empezar == "no" or empezar == "No":
    print("Esta bien nos vemos otro día :(")
if empezar == "Si" or empezar == "si":
    print("Perfectooo!!! Ahora intentarás adivinar el número, para erso tendrás 8 intentos")
    nombre = input("COMENCEMOS! Dime, ¿cuál es tu nombre?: ")
    print(f"Muy bien, {nombre}, te daré una pista, estoy pensando en un número entre el 1 y 100")
    n = 1
    numero = randint(1,101)
    while n < 8:
        intento = int(input(f"{nombre}, ¿Cuál crees que es el número? "))
        if intento not in range(1,101):
            print(f"{intento} no esta en el rango de números que estoy pensando")

        else:
            if intento > numero:
                print(f"Incorrecto ;D, el número que estoy pensando es MENOR que {intento}")
                n+=1

            if intento < numero:
                print(f"Incorrecto ;D, el número que estoy pensando es MAYOR que {intento}")
                n += 1
        if intento == numero:
            print(f"Felicidades {nombre}!!! Haz adivinado mi número ('{numero}'), te tomó {n} intentos")
            break
    if n == 8:
        print(f"Lo siento :(, se te acabaron los intentos el número en el que estaba pensando era: {numero}")

else:
    print("Responde si o no ")


r = "hola"
