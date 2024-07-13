"""Problemas Practicos"""
#Problema 1:
def devolver_distintos(int1,int2,int3):
    valores = [int1,int2,int3]
    suma = int1+int2+int3

    if suma > 15:
        return f" Tu valor maximo es {max(valores)}"
    elif suma < 10:
        return f" Tu valor minimo es {min(valores)}"
    if suma >= 10 and suma <= 15:
        valores.sort()
        return f" Tu valor medio es {valores[1]}"
print(devolver_distintos(4,3,5))

#Problema 2:

def ordenar_char(palabra):
    combertir = list(set(palabra))
    combertir.sort()
    return combertir
print(ordenar_char("cascabeles"))

# Problema 3:
def cero_repetido(*args):
    contador = 0
    for n in args:
        if contador +1 == len(args):
            return False
        elif args[contador] == 0 and args[contador+1] == 0:
            return True
        else:
            contador +=1
    return False

print(cero_repetido(0,4,3,0,5,0,1,3,0))

#Problema 4

def contar_primos(num):
    for i in range(1,num+1):
        if i >1:
            count = 0
            j = 2
            while j<i and count == 0:
                prueba = i%j
                if prueba == 0:
                    count=count+1
                j=j+1
            if count ==0:
                e = print(i,end=", ")
    return e
print(contar_primos(100))