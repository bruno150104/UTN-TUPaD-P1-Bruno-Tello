
# ejercicio 1
for i in range(101):
    print(i)

# ejercicio 2
numero = input("Ingrese un número entero: ")
print("Cantidad de dígitos:", len(numero))

# ejercicio 3
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))
suma = 0
for i in range(inicio + 1, fin):
    suma += i
print("La suma es:", suma)

# ejercicio 4
total = 0
while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break
    total += num
print("Total acumulado:", total)

# ejercicio 5
import random
objetivo = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivine el número (entre 0 y 9): "))
    intentos += 1
    if intento == objetivo:
        break
print("¡Correcto! Lo adivinaste en", intentos, "intentos.")

# ejercicio 6
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# ejercicio 7
limite = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(limite + 1):
    suma += i
print("La suma es:", suma)

# ejercicio 8
pares = impares = positivos = negativos = 0
for _ in range(100):
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num >= 0:
        positivos += 1
    else:
        negativos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# ejercicio 9
suma = 0
for _ in range(100):
    num = int(input("Ingrese un número entero: "))
    suma += num
media = suma / 100
print("La media es:", media)

# ejercicio 10
numero = input("Ingrese un número: ")
invertido = numero[::-1]
print("Número invertido:", invertido)


