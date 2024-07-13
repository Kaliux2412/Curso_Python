def farmacia():
    for n in range (1,501):
        yield f"\tTurno: F-{n}"
def cosmeticos():
    for n in range (1,501):
        yield f"\tTurno: C-{n}"
def alimentos():
    for n in range (1,501):
        yield f"\tTurno: A-{n}"

a = alimentos()
c = cosmeticos()
f = farmacia()

def decorador(funcion):
    print("Su turno es: ")
    if funcion == "F":
        print(next(f))
    elif funcion == "C":
        print(next(c))
    else:
        print(next(a))
    print("Espere, en un momento será atendido")
