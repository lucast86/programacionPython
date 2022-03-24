#ejercicio9 - Lucas Trento
"""Realizar una calculadora con operaciones básicas. Se debe validar que el usuario siempre
ingrese valores numéricos."""

from operator import truediv
from time import strftime


print("\n   ---Calculadora de operaciones basicas---")
operacion = input("¿Cual es la operacion que deseas realizar:\n-->sumar\n-->restar\n-->dividir\n-->multiplicar\n  ")
encendido =True
x = 0 
y = 0

while encendido:
    if operacion == "sumar":
        total = 0
        x = float(input("Ingrese un numero: "))
        y = float(input("Ingrese un numero: "))
        total = (x+y)
        print(f"total :{total}")
        estado = str(input("Precione s para realizar otra operacion o n para apagar la calculadora: "))
        if estado == "s":    
            encendido = True
            operacion = input("¿Cual es la operacion que deseas realizar:\n-->sumar\n-->restar\n-->dividir\n-->multiplicar\n  ")
        else:
             encendido = False
    if operacion == "restar":
        total = 0
        x = float(input("Ingrese un numero: "))
        y = float(input("Ingrese un numero: "))
        total = (x-y)
        print(f"total :{total}")
        estado = str(input("Precione s para realizar otra operacion o n para apagar la calculadora: "))
        if estado == "s":    
            encendido = True
            operacion = input("¿Cual es la operacion que deseas realizar:\n-->sumar\n-->restar\n-->dividir\n-->multiplicar\n  ")
        else:
             encendido = False
    if operacion == "dividir":
        total = 0
        x = float(input("Ingrese un numero: "))
        y = float(input("Ingrese un numero: "))
        total = (x/y)
        print(f"total :{total}")
        estado = str(input("Precione s para realizar otra operacion o n para apagar la calculadora: "))
        if estado == "s":    
            encendido = True
            operacion = input("¿Cual es la operacion que deseas realizar:\n-->sumar\n-->restar\n-->dividir\n-->multiplicar\n  ")
        else:
             encendido = False
    if operacion == "multiplicar":
        total = 0
        x = float(input("Ingrese un numero: "))
        y = float(input("Ingrese un numero: "))
        total = (x*y)
        print(f"total :{total}")
        estado = str(input("Precione s para realizar otra operacion o n para apagar la calculadora: "))
        if estado == "s":    
            encendido = True
            operacion = input("¿Cual es la operacion que deseas realizar:\n-->sumar\n-->restar\n-->dividir\n-->multiplicar\n  ")
        else:
             encendido = False
    
print("APAGADO")