"""
Crear una funcion para sumar los valores recibidos de tipo numerico,
utilizando argumentos variables *args como parametros de la funcion
y regresar como resultado la suma de todos los valores pasados como argumentos
"""

def sumar_valores(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado
print(sumar_valores(2,4,5,6))

"""
Crear una funcion para multiplicar los valores recibidos de tipo numerico,
utilizando argumentos variables *args como parametros de la funcion
y regresar como resultado la multiplicar de todos los valores pasados como argumentos
"""

def multiplicar_valores(*args):
    resultado = 1
    for valor in args:
        resultado *= valor
    return resultado
print(multiplicar_valores(3,5))

"""
Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas.
Puede ser cualquier valor positivo
"""
def imprimir_numero_recursivo(numero):
    if numero >= 1:
        print(numero)
        imprimir_numero_recursivo(numero - 1)
    elif numero == 0:
        return
    elif numero < 0:
        print("Valor incorrecto")
imprimir_numero_recursivo(5)

"""
Ejercicio => calculadora de impuestos
Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
"""
def calcular_total_pago(pago_sin_impuesto,impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

pago_sin_impuesto = float(input("Ingrese el monto: "))
impuesto = float(input("Ingrese el monto del impuesto: "))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'Pago con impuesto: {pago_con_impuesto}')

"""
Ejercicio => Convertidor de Temperatura
Realizar dos funciones para convertir de grados celsius a fahrrenheit y viceversa
"""
def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

celsius = float(input("Proporcione su valor en celsius: "))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F: {resultado:.2f}')

fahrenheit = float(input("Proporcione su valor en Fahrenheit: "))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C: {resultado:.2f}')