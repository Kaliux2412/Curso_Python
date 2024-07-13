"""PROYECTO ANALIZADOR DE TEXTOS (FACIL-MEDIA)"""

print("Bienvenido al analizador de textos;)")
texto = input("Pega el texto que quieras analizar aquí: ")
texto = texto.lower()
print("Ahora escoge 3 letras distintas (las que quieras)")
letras = input("3 letras: ")
letras = list(letras)
def llamarletras():
    letras.sort()
    aparacion_letra1 = texto.count(letras[0])
    aparacion_letra2 = texto.count(letras[1])
    aparacion_letra3 = texto.count(letras[2])
    l1 = letras[0]
    l2 = letras[1]
    l3 = letras[2]
    print(f"La cantidad de veces que apareció '{l1}', '{l2}' y '{l3}' fue: \n \t'{l1}' : \t{aparacion_letra1}, \n \t'{l2}' : \t{aparacion_letra2}, \n \t'{l3}' : \t{aparacion_letra3}.")

if len(letras) == 3:
    llamarletras()

else:
    letras = input("Escoge solo 3 letras: ")
    letras = list(letras)
    llamarletras()

texto = texto.split()

print(f"Muy bien, ahora sobre tu texto encontramos que tiene un largo de: \n\t{len(texto)} palabras.")
texto = texto.__str__()

primer_letra = texto[2]
if texto[len(texto)-3] == ".":
    ultima_letra = texto[len(texto) - 4]
else:
    ultima_letra = texto[len(texto) - 3]


print(f"Ahora hablemos de principio a fin, la primer letra de tu texto es:\n\t'{primer_letra}' y la última es: '{ultima_letra}'.")

texto = list(texto)
largo = len(texto)-2
texto = texto[2:largo]

texto = "".join(texto)

for n in range(2, len(texto)-1):
    texto = list(texto)
    if texto.__contains__(",") :
        texto.remove(",")
    if texto.__contains__("'"):
        texto.remove("'")
texto = "".join(texto)
areves = texto[::-1]

print(f"Tu texto al revés se vería así: \n\t{areves}")