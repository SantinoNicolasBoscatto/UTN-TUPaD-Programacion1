# 1
precios_frutas = {
    'Banana': 1200,
    'Anana': 2500,
    'Melon': 3000,
    'Uva': 1450
}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario con las nuevas frutas:")
print(precios_frutas)

# 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

print("Diccionario con los nuevos precios:")
print(precios_frutas)

# 3
lista_frutas = list(precios_frutas.keys())

print("Lista de frutas:")
print(lista_frutas)


# 4
contactos = {}

for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i + 1}: ")
    numero = input(f"Ingrese el numero del contacto {nombre}: ")
    contactos[nombre] = numero 

print("Todos tus contactos:")
print(contactos)

consulta = input("Ingrese el nombre del contacto que desea buscar: ").capitalize()
for nombre in contactos:
    if nombre.capitalize() == consulta:
        print(f"El numero de {nombre} es: {contactos[nombre]}")
        break
else:
    print(f"No se encontro ningun contacto con el nombre '{consulta}'.")


# 5
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Palabras unicas:", palabras_unicas)
print("Recuento de palabras:", recuento)


# 6
alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno numero {i + 1}: ")
    print(f"Ingrese las 3 notas de {nombre}:")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    alumnos[nombre] = (n1, n2, n3)

print("Promedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")


# 7
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

ambos_parciales = parcial1 & parcial2
solo_un_parcial = parcial1 ^ parcial2
al_menos_un_parcial = parcial1 | parcial2

print("Aprobaron ambos:", ambos_parciales)
print("Aprobaron solo un parcial:", solo_un_parcial)
print("Aprobaron al menos un parcial:", al_menos_un_parcial)


# 8
stock = {
    "Manzanas": 50,
    "Bananas": 30,
    "Naranjas": 100
}

producto = input("Ingrese el nombre del producto que quiere consultar: ")
if producto in stock:
    print(f"El stock actual de {producto} es {stock[producto]}")
    opcion = input("Desea agregar stock a este producto? (s/n): ")
    if opcion.lower() == "s":
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        stock[producto] += cantidad
        print(f"Nuevo stock de {producto} es {stock[producto]}")
else:
    print("Producto no encontrado.")
    opcion = input("Desea agregarlo al sistema? (s/n): ")
    if opcion.lower() == "s":
        cantidad = int(input("Ingrese la cantidad inicial de stock: "))
        stock[producto] = cantidad
        print(f"El producto {producto} fue agregado con {cantidad} unidades de stock.")

print("Stock final:")
print(stock)


# 9
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

print("Agenda actual:")
for clave, evento in agenda.items():
    print(f"{clave}: {evento}")

dia = input("Ingrese el dia: ").lower()
hora = input("Ingrese la hora: ")

if (dia, hora) in agenda:
    print(f"A ese hora tenes un evento programado: {agenda[(dia, hora)]}")
else:
    print("No hay ningun evento programado para esa fecha y hora")


# 10 
paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago"
}

capitales = {}
for pais, capital in paises.items():
    capitales[capital] = pais

print("Diccionario original (país → capital):")
print(paises)

print("---------")

print("Diccionario invertido (capital → país):")
print(capitales)