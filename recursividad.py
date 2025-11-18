#ejercicio 1

def factorial(n):
    if n == 0 or n == 1: 
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Ingrese un número: "))
for i in range(1, num + 1):
    print(f"Factorial de {i} = {factorial(i)}")


#ejercicio 2

def fibonacci(n):
    if n == 0:  
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


pos = int(input("Ingrese la posición de Fibonacci: "))
serie = [fibonacci(i) for i in range(pos + 1)]
print("Serie de Fibonacci:", serie)


#ejercicio 3

def potencia(base, exp):
    if exp == 0:   # caso base
        return 1
    else:
        return base * potencia(base, exp - 1)

b = int(input("Ingrese la base: "))
e = int(input("Ingrese el exponente: "))
print(f"{b}^{e} = {potencia(b, e)}")


#ejercicio 4

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(numero)
print(f"El número {numero} en binario es: {binario if binario else '0'}")


#ejercicio 5

def es_palindromo(palabra):
    if len(palabra) <= 1: 
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1]) 

pal = input("Ingrese una palabra: ")
print("¿Es palíndromo?", es_palindromo(pal))


#ejercicio 6

def suma_digitos(n):
    if n == 0:   
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)

num = int(input("Ingrese un número entero positivo: "))
print(f"Suma de dígitos de {num} = {suma_digitos(num)}")


#ejercicio 7

def contar_bloques(n):
    if n == 1: 
        return 1
    else:
        return n + contar_bloques(n - 1)

niveles = int(input("Ingrese el número de bloques en el nivel más bajo: "))
print(f"Total de bloques necesarios: {contar_bloques(niveles)}")


#ejercicio 8

def contar_digito(numero, digito):
    if numero == 0: 
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

num = int(input("Ingrese un número entero positivo: "))
dig = int(input("Ingrese el dígito a buscar (0-9): "))
print(f"El dígito {dig} aparece {contar_digito(num, dig)} veces en {num}")
