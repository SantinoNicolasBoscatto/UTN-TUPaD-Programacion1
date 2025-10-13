# 1
import os
archivo = "productos.txt"

if not os.path.exists(archivo):
    with open(archivo, "w") as f:
        f.write("Lapicera,120.5,30\n")
        f.write("Cuaderno,250.0,50\n")
        f.write("Mochila,1500.0,10\n")
else:
    print("El archivo ya existe. Se usaran los datos existentes.")


# 2
with open("productos.txt", "r") as f:
    for linea in f:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


# 3
nuevo_nombre = input("Ingrese el nombre del nuevo producto: ")
nuevo_precio = input("Ingrese el precio: ")
nueva_cantidad = input("Ingrese la cantidad: ")

with open("productos.txt", "a") as f:
    f.write(f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n")


# 4
productos = []

with open("productos.txt", "r") as f:
    for linea in f:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

print(productos)


# 5
buscar_nombre = input("Ingrese el nombre del producto a buscar: ")
encontrado = False

for p in productos:
    if p["nombre"].lower() == buscar_nombre.lower():
        print(f"Producto encontrado: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("Producto no encontrado.")


# 6
with open("productos.txt", "w") as f:
    for p in productos:
        f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
