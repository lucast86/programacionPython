#ejercicio5 - Lucas Trento
"""Escribe un programa que pida 3 números e imprima el mayor de los tres.."""

numeros = []
cont = 0
for cont in range(3):
            numeros.append(int(input("Ingrese un numero: ")))
            cont += 1

numeros.sort()
print("el mayor es: ", numeros.pop(2))