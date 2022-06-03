# Dada la siguiente tupla
#Crear una lista que solo incluya los numeros menores a 5

tupla = (13, 1, 8, 3, 2, 5, 8)
elemento = []

for tuplas in tupla:
    if tuplas < 5:
        elemento.append(tuplas)
print(elemento)