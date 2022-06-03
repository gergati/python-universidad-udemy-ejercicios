# Sintaxis de range(inicio<opcional>, fin<requerido>, incremento<opcional>)

print("Ejercicio => Iterar un rango de 0 a 10 e imprimir números divisibles entre 3")
for numeros in range(11):
    if numeros % 3 == 0:
        print(numeros)

print("Ejercicio => Crear un rango de numeros de 2 a 6, e imprimelos")

lista2 = [0,1,2,3,4,5,6,7,8,9,10]
for lista2 in range(2,7):
    print(lista2)

print("Ejercicio => Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1")
rango = range(3,11,2)
for i in rango:
    print(i)

