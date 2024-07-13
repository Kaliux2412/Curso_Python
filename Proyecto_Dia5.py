"""Juego del Ahorcado: El proyecto consistirá en hacer uso de varias
funciones y su interacción entre ellas. (MEDIA)"""

from random import *
from os import system
palabras = ["chocolate", "playa","universidad","computadora","libros", "amable","quehacer","vestido","sabores","olores","paises","hermanos",
            "zapatos","electricidad","hospitales","recomendado","carretera","aniversario","mantenimiento","herramientas"
            ,"restaurante","parrillada","mariscos","hamburguesa","pasteles","helados","comunidad"]
nombre = input("Escribe tu nombre: ")
print(f"Bienvenido al juego del Ahorcado {nombre}!")
vidas = 9
print(f"Aquí deberás de adivinar la palabra preguntandome si contiene alguna letra del abecedario\nAdemás cuentas solo con {vidas} vidas.\nSi la letra que dices no se encuentra en la palabra que escoja, "
      f"\nperderás una vida y así hasta que ganes adivinando la palabra o pierdas todas tus vidas")
iniciar = input("Estás list@?: ")
validar  = 0
while validar == 0:
    if iniciar == "si" or iniciar == "Si":
        validar = 1
        palabra_secreta = choice(palabras)
        palabra_oculta = []
        pista = randint(1, len(palabra_secreta) - 1)
        pista2 = randint(1, len(palabra_secreta) - 1)
        for n in palabra_secreta:
            if palabra_secreta.index(n) == pista or palabra_secreta.index(n) == pista2:
                palabra_oculta.append(n)
            else:
                palabra_oculta.append("_")
        def vidas_palabra():
            print(f"Vidas: {vidas} ♥")

        vidas_palabra()
        print(f"\t\tAdivina la palabra oculta: \n\t\t{palabra_oculta}")
    else:
        iniciar = input("Estas listo?: ")
while 9 >= vidas > 0:
    intento = input("Escribe una letra que creas que este en esta palabra:")
    def intentos(letra):
        letras = []
        if len(letra) <= 1:
            letras.append(letra)
            return letras
        else:
            return letras

    if len(intentos(intento)) == 1 and intentos(intento) is not int:
        intento_letras = intentos(intento)
        def validar(letras):
            if len(letras) == 0:
                intento = input("Escribe una letra que creas que este en esta palabra:")
                intentos(intento)
            else:
                corregir = []
                for l in letras:
                    if l in palabra_secreta:
                        corregir.append("correcto")
                        corregir.append(l)

                    else:
                        corregir.append("incorrecto")
                        corregir.append(l)
                        vidas_palabra()
                return corregir
        verificar = validar(intento_letras)
        if verificar[0] == "correcto":
            system("cls")
            print(f"Eso es CORRECTO la letra (''{verificar[1].upper()}'') está en la palabra")
            def añadir_letra(letra):
                for n in range(0,len(palabra_secreta)):
                    if palabra_secreta[n] == letra:
                        palabra_oculta[n] = letra
                        vidas_palabra()
                        print(f"\t\tAdivina la palabra oculta: \n\t\t{palabra_oculta}")
                    else:
                        pass
            añadir_letra(verificar[1])

        else:
            system("cls")
            print(f"Eso es INCORRECTO la letra (''{verificar[1]}'') NO está en la palabra")
            vidas -=1
            vidas_palabra()
            print(f"\t\tAdivina la palabra oculta: \n\t\t{palabra_oculta}")
        if "_" not in palabra_oculta and vidas >0:
            print(f"\nFELICIDADESSS!!! Adivinaste la palabra '{palabra_secreta}', haz GANADO!")
            vidas = 0
        else:
            pass
        if vidas == 0 and "_" in palabra_oculta:
            print(f"Lo siento haz perdido te quedaste sin vidas :(, la palabra era: ''{palabra_secreta.upper()}''")
    else:
        print("Solo debes escoger UNA letra")



