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
print("Vamos a cargar las notas de las siguientes materias:\n-->Lengua\n-->Matematica\n-->Fisica\n ")
seguir=str(input("precione la letra s para seguir: \n  "))


while seguir != "s":
    seguir=str(input("letra erronea para continuar con el programa\nprecione s para seguir: \n  "))
   
#materia = materia.lower()
"""if   materia == "lengua":      carga = "lengua"
elif materia == "matematica":  carga = "matematica"
elif materia == "fisica":      carga = "fisica"
else:
    carga = 0 ,print("la materia no existe")"""
cont = 0    


while  cont !=3:
    if cont == 0:
        print("\n----Carga las nota de Lengua----\n")
        nota1Lengua=float(input("ingrese la primer nota: ")) 
        nota2Lengua=float(input("ingrese la segunda nota: ")) 
        nota3Lengua=float(input("ingrese la tercer nota: ")) 
        sumaLengua=(nota1Lengua +nota2Lengua +nota3Lengua)
        promedioLengua= sumaLengua/3
    if cont == 1:
        print("\n----Carga las nota de Matematica----\n")
        nota1Matematica=float(input("ingrese la primer nota: ")) 
        nota2Matemaica=float(input("ingrese la segunda nota: ")) 
        nota3Matematica=float(input("ingrese la tercer nota: ")) 
        sumaMatematica=(nota1Matematica +nota2Matemaica +nota3Matematica)
        promedioMatematica= sumaMatematica/3
    if cont == 2:
        print("\n----Carga las nota de Fisica----\n")
        nota1Fisica=float(input("ingrese la primer nota: ")) 
        nota2Fisica=float(input("ingrese la segunda nota: ")) 
        nota3Fisica=float(input("ingrese la tercer nota: ")) 
        sumaFisica=(nota1Fisica +nota2Fisica +nota3Fisica)
        promedioFisica= sumaFisica/3
        print("\n----PROMEDIOS----\n")
        print(f"-Promedio de Lengua es: {promedioLengua}\n-Promedio de Matematica es: {promedioMatematica}\n-Promedio de Fisica es: {promedioFisica}")  
    cont = cont + 1