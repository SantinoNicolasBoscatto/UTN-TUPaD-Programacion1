# 1)
for i in range (101):
    print(i)


# 2)
numero = int(input("Ingrese un numero entero: "))
if numero == 0:
    cantidad_digitos = 1
else:
    cantidad_digitos = 0
numero = abs(numero)
while numero > 0:
    numero = numero // 10
    cantidad_digitos += 1
print(f"El numero tiene {cantidad_digitos} digito(s).")


# 3)
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
suma_total = 0

for i in range(n1+1, n2):
    suma_total += i

print(f"La suma total es: {suma_total}")


# 4) 
suma_total = 0
while True:
    numero = int(input("Ingrese un numero entero, o 0 para terminar y mostrar la suma total: "))
    if numero == 0:
        break
    suma_total += numero
print(f"La suma total acumulada es: {suma_total}")


# 5)
import random
random_number = random.randint(0, 9)
intentos = 0
numero = int(input("Adivine el numero aleatorio entre el 0 y 9: "))
while True:
    intentos += 1
    if numero == random_number:
        break
    else: 
        numero = int(input("Ese no es! vuelva a intentarlo: "))
print(f"Correcto! El numero era {random_number}. Le tomo {intentos} intentos adivinarlo!")    


# 6) 
for i in range (100, -1, -2):
    print(i)



# 7)
num = int(input("Ingrese un numero positivo y se sumeran todos los numeros comprendidos entre el 0 y el ingresado: "))
suma_total = 0
for i in range(0, num+1):
    suma_total += i
print(f"La suma es: {suma_total}")


# 8) 
contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0
for i in range(10):
    num = int(input("Ingrese un numero: "))
    
    if num % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
    
    if num > 0:
        contador_positivos += 1
    elif num < 0:
        contador_negativos += 1
print(f"Hubo: {contador_pares} pares, {contador_impares} impares, {contador_positivos} positivos y {contador_negativos} negativos")


# 9)
media = 0
numeros_ingresados = 10
for i in range(numeros_ingresados):
    media += int(input("Ingrese un numero: "))
media = media / numeros_ingresados

print(f"La media de los numeros ingresados es: {media:.2f}")


# 10)
numero = int(input("Ingrese un numero entero: "))
signo = 1
invertido = 0

if numero < 0:
    signo = -1
    numero = abs(numero)

while numero != 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

invertido *= signo
print(f"El numero invertido es: {invertido}")