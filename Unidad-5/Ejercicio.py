#1
notas_lista = [10,8,7,5,8,9,10,10,4,7]
print("Lista de notas: ")
for nota in notas_lista:
    print(nota)
print(f"El promedio de las notas es: {sum(notas_lista)/len(notas_lista)}")
print(f"La nota mas alta es: {max(notas_lista)}. La nota mas baja es: {min(notas_lista)}")
    

#2
productos = []
for i in range(5):
    producto = input("Ingrese un producto: ")
    productos.append(producto)

productos.sort()
for producto in productos:
    print(producto)

producto_eliminar = input("Ingrese el producto que desea eliminar: ")
if producto_eliminar in productos:
    productos.remove(producto_eliminar)
else:
    print("Ese producto no está en la lista.")

print("Lista actualizada: ")
for producto in productos:
    print(producto)


#3
import random
numeros = []
for i in range(15):
    random_n = random.randint(1, 100)
    numeros.append(random_n)

input(f"Lista generada: {numeros}. Enter para continuar ")

pares = []
impares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"La lista de pares tiene: {len(pares)} numero/s")
for par in pares:
    print(par)

print(f"La lista de impares tiene: {len(impares)} numero/s")
for impar in impares:
    print(impar)


#4
datos = [1,3,5,3,7,1,9,5,3]
datos_unicos = []
for dato in datos:
    if dato not in datos_unicos:
        datos_unicos.append(dato) 

print("Lista sin datos repetidos: ")
for dato_unico in datos_unicos:
    print(dato_unico)


#5
estudiantes = ["Juan", "Jose", "Pedro", "Enzo", "Jeremias", "Simon", "Alfredo", "Gabriel"]
option = input("Quiere agregar o eliminar algun estudiante a la lista? Para agregar ingrese A y para eliminar E: ")
if option.upper() == "A":
    nombre = input("Indique el nombre del alumno que quiere agregar: ")
    estudiantes.append(nombre)
elif option.upper() == "E":
    nombre = input("Indique el nombre del alumno que quiere eliminar: ")
    if nombre in estudiantes:
        estudiantes.remove(nombre)
    else:
        print("Ese nombre no está en la lista.")
else:
    print("Ingreso una opcion invalida")


print("Lista de alumnos: ")
for est in estudiantes: 
    print(est)


#6 
lista = [1, 2, 3, 4, 5, 6, 7]
lista = [lista[-1]] + lista[:-1]
print(lista)



#7
temperaturas = [
    [11, 24],
    [13, 26],
    [11, 22],
    [14, 28],
    [10, 20],
    [9, 21],
    [15, 28]
]
promedio_minimos = 0
promedio_maximos = 0
max_amplitud_termica = 0
contador = 0
dia = 1

for i in temperaturas:
    contador += 1
    promedio_minimos += i[0]
    promedio_maximos += i[1]
    if max_amplitud_termica < i[1] - i[0]:
        max_amplitud_termica = i[1] - i[0]
        dia = contador

promedio_maximos = promedio_maximos / 7
promedio_minimos = promedio_minimos / 7

print(f"Promedio de maximos: {promedio_maximos:.2f}")
print(f"Promedio de minimos: {promedio_minimos:.2f}")
print(f"El dia numero {dia} se registro la mayor amplitud termica, que fue de {max_amplitud_termica}º")


#8
estudiantes_notas = [
    [8,7,9],
    [9,9,10],
    [8,4,6],
    [8,9,8],
    [10,10,7]
]
contador = 0

for estudiante_notas in estudiantes_notas:
    contador += 1
    promedio_alumno = 0
    for nota in estudiante_notas:
        promedio_alumno += nota
    promedio_alumno = promedio_alumno / 3
    print(f"El promedio del estudiante numero {contador} es: {promedio_alumno:.2f}")

print()

materias = len(estudiantes_notas[0])
for i in range(materias):
    promedio_materia = 0
    for estudiante in estudiantes_notas:
        promedio_materia += estudiante[i]
    promedio_materia = promedio_materia / len(estudiantes_notas)
    print(f"El promedio de la materia {i + 1} es: {promedio_materia:.2f}")


#9
ta_te_ti = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]
contador = 0

# Cada jugador tendrá 3 turnos
while contador < 3: 
    contador += 1

    # Turno jugador uno
    while True:
        jugador_uno_entrada = input("Jugador uno, ingrese la posición donde quiere colocar la X (formato: fila columna, del 0 al 2): ")
        fila, columna = map(int, jugador_uno_entrada.split(" "))
        if ta_te_ti[fila][columna] == "-":
            ta_te_ti[fila][columna] = "X"
            break
        else:
            print("Casilla ocupada. Intente otra posición.")

    for fila_tablero in ta_te_ti:
        print(" ".join(fila_tablero))

    # Turno jugador dos
    while True:
        jugador_dos_entrada = input("Jugador dos, ingrese la posición donde quiere colocar la O (formato: fila columna, del 0 al 2): ")
        fila, columna = map(int, jugador_dos_entrada.split(" "))
        if ta_te_ti[fila][columna] == "-":
            ta_te_ti[fila][columna] = "O"
            break
        else:
            print("Casilla ocupada. Intente otra posición.")

    for fila_tablero in ta_te_ti:
        print(" ".join(fila_tablero))

#10
dias_productos = [
    [12, 15, 9, 20, 18, 14, 10], 
    [8,  11, 13, 17, 16, 12, 9],
    [20, 22, 18, 25, 24, 19, 21],
    [5,  7,  6,  8,  9,  10, 6]
]
contador = 0
mas_vendido_ventas = 0
mas_vendido = 1
for dias_producto in dias_productos:
    contador += 1
    total_ventas = 0
    for producto in dias_producto:
        total_ventas += producto
    print(f"El producto numero {contador} vendio: {total_ventas}")
    if total_ventas > mas_vendido_ventas:
        mas_vendido = contador
        mas_vendido_ventas = total_ventas


numero_dias = len(dias_productos[0])
mas_vendido_ventas_dia = 0
mas_vendido_dia = 1
for i in range(7):
    total_ventas_dia = 0
    for dias_producto in dias_productos:
        total_ventas_dia += dias_producto[i]

    if total_ventas_dia > mas_vendido_ventas_dia:
        mas_vendido_ventas_dia = total_ventas_dia
        mas_vendido_dia = i+1

print()
print(f"El producto mas vendido fue el producto numero {mas_vendido}, con {mas_vendido_ventas} ventas")
print()
print(f"El de la semana que mas se vendio fue dia {mas_vendido_dia}, con {mas_vendido_ventas_dia} ventas")
print()
