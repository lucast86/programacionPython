#ejercicio1 - Lucas Trento
"""Desarrollar un programa que le pida al alumno todas las materias que está cursando (al menos
4) y luego se le debe pedir las respectivas notas de los 3 parciales de las asignaturas
ingresadas. Por último el programa debe calcular el promedio de las evaluaciones y definir por
cada una de ellas:
 Si la materia tiene como promedio un 8 o más: Materia promocionada.
 Si la materia tiene como promedio una nota menor a 8 pero mayor o igual a 6: Materia
aprobada.
 Si la materia tiene como promedio una nota menor que 6: Materia desaprobada."""


print("         ---Bienvenido---        ")
print("Vamos a cargar las notas de las siguientes materias:\n1-->Lengua\n2-->Matematica\n3-->Fisica\n4-->Quimica\n")

seguir=str(input("precione la letra s para seguir:  "))
while seguir != "s":
    seguir=str(input("letra erronea para continuar con el programa\nprecione s para seguir: \n  "))

cont = 0   
materias = 0    
notasLengua = []
notasMatematicas = []
notasFisica = []
notasQuimica = []

while  materias !=4:
    if materias == 0:
        print("\n----Carga las nota de Lengua----\n")
        for cont in range(4):
            notasLengua.append(int(input("Ingrese las notas de lengua: ")))
            cont += 1
        sumaLengua = sum(notasLengua)
        promedioLengua = sumaLengua/4

    if materias == 1:
        print("\n----Carga las nota de Matematica----\n")
        for cont in range(4):
            notasMatematicas.append(int(input("Ingrese las notas de Matematica: ")))
            cont += 1
        sumaMatematica = sum(notasMatematicas)
        promedioMatematica = sumaMatematica/4
         
    if materias == 2:
        print("\n----Carga las nota de Fisica----\n")
        for cont in range(4):
            notasFisica.append(int(input("Ingrese las notas de Fisica: ")))
            cont += 1
        sumaFisica = sum(notasFisica)
        promedioFisica = sumaFisica/4
         
    if materias == 3:
        print("\n----Carga las nota de  Quimica----\n")
        for cont in range(4):
            notasQuimica.append(int(input("Ingrese las notas de Quimica: ")))
            cont += 1
        sumaQuimica = sum(notasQuimica)
        promedioQuimica= sumaQuimica/4

    materias +=1

seguir=str(input("\nprecione la letra s para seguir:   "))
while seguir != "s":
    seguir=str(input("letra erronea para continuar con el programa\nprecione s para seguir: \n  "))

print("\n----PROMEDIOS----\n")
print(f"-Promedio de Lengua es: {promedioLengua}") 
print(f"-Promedio de Matematica es: {promedioMatematica}") 
print(f"-Promedio de Fisica es: {promedioFisica}")  
print(f"-Promedio de Quimica es: {promedioQuimica}")

seguir=str(input("\nprecione la letra s para seguir:   "))
while seguir != "s":
    seguir=str(input("letra erronea para continuar con el programa\nprecione s para seguir: \n  "))

print("\n----Materias Promocionadas, Aprobadas o Desaprobadas----\n")
if promedioLengua >= 8:
    print("--Lengua esta Promocionada FELECITACIONES")
elif promedioLengua < 8 and promedioLengua >= 6:
    print("--Lengua esta aprobada")
elif promedioLengua < 6:
    print("--Lengua esta desaprobada")

if promedioMatematica >= 8:
    print("--Matematica esta Promocionada FELECITACIONES")
elif promedioMatematica < 8 and promedioMatematica >= 6:
    print("--Matematica esta aprobada")
elif promedioMatematica < 6:
    print("--Matematica esta desaprobada")

if promedioFisica >= 8:
    print("--Fisica esta Promocionada FELECITACIONES")
elif promedioFisica < 8 and promedioFisica >= 6:
    print("--Fisica esta aprobada")
elif promedioFisica < 6:
    print("--Fisica esta desaprobada")

if promedioQuimica >= 8:
    print("--Quimica esta Promocionada FELECITACIONES")
elif promedioQuimica < 8 and promedioQuimica >= 6:
    print("--Quimica esta aprobada")
elif promedioQuimica < 6:
    print("--Quimica esta desaprobada")

print("\nFINN")