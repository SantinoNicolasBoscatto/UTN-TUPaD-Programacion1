# 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

# 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

# 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# 4
import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio de un circulo: "))
print(f"Area: {calcular_area_circulo(radio):.2f}")
print(f"Perimetro: {calcular_perimetro_circulo(radio):.2f}")

# 5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese una cantidad de segundos: "))
print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos):.2f} horas")

# 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

# 7
def operaciones_basicas(a, b):
    return (a+b, a-b, a*b, a/b)

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
suma, resta, mult, div = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {mult}, División: {div:.2f}")

# 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"Su IMC es: {calcular_imc(peso, altura):.2f}")

# 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese una temperatura en °C: "))
print(f"Equivale a {celsius_a_fahrenheit(celsius):.2f} °F")

# 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))
n3 = float(input("Ingrese el tercer numero: "))
print(f"El promedio es: {calcular_promedio(n1, n2, n3):.2f}")