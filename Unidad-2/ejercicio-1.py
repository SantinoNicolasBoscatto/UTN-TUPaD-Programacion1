# 1)
print("Hola Mundo!")

# 2)
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3)
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4)
import math
radio = float(input("Ingrese el radio de un circulo: "))
area = math.pi * pow(radio, 2)
perimetro = 2 * math.pi * radio
print(f"El Area del circulo es: {area:.2f} --- El Perimetro del circulo es: {perimetro:.2f}")


# 5)
segundos = int(input("Ingrese una cantidad de segundos y se devolvera a cuantas horas equivale: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a Hora/s {horas}")


# 6)
numeroTabla = int(input("Ingrese la tabla de multiplicar deseada: "))
for i in range(1, 11):
    print(f"{numeroTabla} X {i} = {numeroTabla * i}")


#7)
num1 = int(input("Ingrese un numero entero distinto de 0: "))
num2 = int(input("Ingrese un segundo entero distinto de 0: "))

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicacion: {num1 * num2}")
print(f"Division: {num1 / num2}")


#8)
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
imc = peso / pow(altura, 2)
print(f"Su indice de masa corporal: {imc:.3f}")

#9)
celsius = float(input("Ingrese una tempuratura en grados Cº: "))
fahrenheit = 9/5 * celsius + 32
print(f"{celsius} grados Cº son {fahrenheit} grados Fº")


#10)
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los 3 numeros es: {promedio:.2f}")