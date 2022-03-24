#ejercicio10 - Lucas Trento

"""Realizar un juego donde el usuario debe adivinar el número arrojado por la función random.
Solamente cuenta con 5 intentos"""

import random
numerosAleatorios = random.randrange(10)
print(numerosAleatorios)

cont = 0
numeroJugador=int(input("Elija un numero del 1 al 10. Recuerde que tiene 5 intentos para ganar \nIngrese un numero: "))

for cont in range(4):
    if numeroJugador == numerosAleatorios:
        print(f"El numero {numeroJugador} coincide con el numero aleatorio del juego que es {numerosAleatorios}\n ¡¡FELICIDADES!!!")  
        break
    elif numeroJugador != numerosAleatorios:
        print("Intente de nuevo numero equivcado")
        numeroJugador=int(input("Ingrese otro numero: "))
        cont +=1
      
if cont == 4:
        print("¡¡¡PERDIO!!!")
        print("fin")

