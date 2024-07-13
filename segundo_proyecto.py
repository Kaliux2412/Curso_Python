"""Proyecto calculador de COMISIONES (FÁCIL)"""

print("Bienvenido a la calculadora de comisiones, añade la info solicitada...")
nombre = input("¿Cúal es tu nombre?: ")
ventas = float(input("¿Cuánto haz vendido en este mes?: "))

porcentaje = ventas *(13/100)

comision = round(porcentaje, 2)

print(f"De acuedo {nombre}, este mes lograste obtener ${comision} en tus comisiones!")