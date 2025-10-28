# ejercicio 1
with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,350.0,15\n")
    archivo.write("Goma,80.0,50\n")

# ejercicio 2
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# ejercicio 3
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

nuevo = input("Ingrese nuevo producto (nombre,precio,cantidad): ")

with open("productos.txt", "a") as archivo:
    archivo.write(nuevo + "\n")

# ejercicio 4
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {"nombre": nombre,"precio": float(precio),"cantidad": int(cantidad)}
        productos.append(producto)

for p in productos:
    print(p)

# ejercicio 5
nombre_buscar = input("Ingrese el nombre del producto a buscar: ")

encontrado = False
for p in productos:
    if p["nombre"].lower() == nombre_buscar.lower():
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("Producto no encontrado.")

# ejercicio 6
with open("productos.txt", "w") as archivo:
    for p in productos:
        linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
        archivo.write(linea)
