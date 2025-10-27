# ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

# ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

# ejercicio 3
solo_frutas = list(precios_frutas.keys())
print(solo_frutas)

# ejercicio 4
agenda_telefonica = {}
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    agenda_telefonica[nombre] = numero

consulta = input("¿Qué contacto querés consultar?: ")
if consulta in agenda_telefonica:
    print(f"El número de {consulta} es {agenda_telefonica[consulta]}")
else:
    print("Ese contacto no está en la agenda.")

# ejercicio 5
frase = input("Ingresá una frase: ").lower()
palabras = frase.split()
palabras_unicas = set(palabras)
frecuencia = {}

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Frecuencia de cada palabra:", frecuencia)

# ejercicio 6
alumnos = {}
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Ingresá la nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre} tiene un promedio de {promedio:.2f}")

# ejercicio 7
parcial1 = {101, 102, 103, 104}
parcial2 = {103, 104, 105, 106}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# ejercicio 8
stock_productos = {}

producto = input("Ingresá el nombre del producto a consultar: ")
if producto in stock_productos:
    print(f"Stock de {producto}: {stock_productos[producto]}")
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    stock_productos[producto] += agregar
else:
    nuevo_stock = int(input(f"{producto} no existe. ¿Cuántas unidades querés agregar?: "))
    stock_productos[producto] = nuevo_stock

print("Stock actualizado:", stock_productos)

# ejercicio 9
agenda_eventos = {('Lunes', '10:00'): 'Reunión de equipo',('Martes', '14:00'): 'Clase de programación',('Viernes', '18:00'): 'Entrega de TP'}

dia = input("Ingresá el día: ")
hora = input("Ingresá la hora (formato HH:MM): ")
evento = agenda_eventos.get((dia, hora), "No hay actividad programada.")
print(f"Actividad en {dia} a las {hora}: {evento}")

# ejercicio 10
paises_capitales = {'Argentina': 'Buenos Aires','Chile': 'Santiago','Brasil': 'Brasilia','Uruguay': 'Montevideo'}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print(capitales_paises)
