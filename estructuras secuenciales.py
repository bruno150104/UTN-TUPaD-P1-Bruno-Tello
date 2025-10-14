#ejercicio 1
print("hola mundo")

#ejercicio 2
print("ingresa tu nombre")

nombre= input("ingresa tu nombre")
print("hola", nombre)

#ejercicio 3
nombre=input("ingresa tu nombre")
apellido=input("ingresa tu apellido")
edad=input("ingresa tu edad")
residencia=input("ingresa tu lugar de residencia")
print("Soy", nombre, apellido, "tengo", edad, "y vivo en",residencia)

#ejercicio 4 
radio=float( input("ingrese el valor del radio de un circulo"))
resultado= 3.14  *radio*radio
print("el valor del radio del circulo es de", resultado)

#ejercicio 5
segundos=float(input("ingrese una cantidad de segundos"))
resultado= segundos/3600
print("equivale a",resultado,"horas")

#ejercicio 6
numero=input("ingrese un numero")
print=(f"tabla de multiplicar del {numero}")
for i in range(1,11):
    print(f"{numero}*{i}={numero*i}")

#ejercicio 7
num1 = int(input("Ingresa el primer número entero (distinto de 0): "))
num2 = int(input("Ingresa el segundo número entero (distinto de 0): "))
if num1 == 0 or num2 == 0:
    print("Ambos números deben ser distintos de 0. Inténtalo de nuevo.")
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"\nResultados:")
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division:.2f}")

#ejercicio 8
peso = float(input("Por favor, ingresa tu peso en kilogramos: "))
altura = float(input("Por favor, ingresa tu altura en metros: "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

#ejercicio 9
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"La temperatura equivalente en grados Fahrenheit es: {fahrenheit:.2f}")

#ejercicio 10
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los números ingresados es: {promedio}")