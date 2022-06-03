# Ejercicio => Conversion de número a texto

numero = int(input('Introduce un valor entre 1 y 3: '))
numero_texto = ""

if numero == 1:
    numero_texto = "Uno"
elif numero == 2:
    numero_texto = "Dos"
elif numero == 3:
    numero_texto = "Tres"
else:
    numero_texto = "Valor fuera de rango"

print(f'Su numero proporcionado es: {numero} - {numero_texto}')

# Ejercicio => Calcular la estación según el mes proporcionado

numero_mes = int(input('Ingrese numero del mes (1-12): '))
estacion = None
if numero_mes == 1 or numero_mes == 2 or numero_mes == 12:
    estacion = "Verano"
elif numero_mes == 3 or numero_mes == 4 or numero_mes == 5:
    estacion = "Otoño"
elif numero_mes == 6 or numero_mes == 7 or numero_mes == 8:
    estacion = "Invierno"
elif numero_mes == 9 or numero_mes == 10 or numero_mes == 11:
    estacion = "Primavera"
else:
    estacion = "Mes incorrecto"
print(f'Para el mes {numero_mes} la estacion es: {estacion}')

# Ejercicio => Etapas de vida según la edad

etapas = int(input("En que etapas de tu vida estas? (0 a 30): "))
mensaje = None

if (etapas >= 0 and etapas <= 10):
    mensaje = "La infancia es increible"
elif (etapas >= 10 and etapas <= 20):
    mensaje = "Muchos cambios y mucho estudio..."
elif (etapas >= 20 and etapas <= 30):
    mensaje = "Mucho amor y comienza el trabajo"
else:
    mensaje = "No reconocida..."
print(f'Su numero es {etapas}, entonces su etapa: {mensaje} ')

# Ejercicio => Sistema de calificaciones

calificacion = float(input("Ingrese su calificación:"))
nota = ""

if 0 < calificacion < 6:
    nota = "F, te la llevas a marzo negrito"
elif 6 == calificacion < 7:
    nota = "D, tenes que hacer un trabajito practico"
elif 7 == calificacion < 8:
    nota = "C, aprobaste de ojete"
elif 8 == calificacion < 9:
    nota = "B, me dijo tu tio que anduviste estudiando"
elif 9 == calificacion < 10:
    nota = "A, que sos? Paenza boludo"
else:
    nota = "Valor incorrecto, pone bien el numero, o saco la morocha"
print(f'Su calificacion es: {calificacion}, por lo cual su nota es: {nota}')