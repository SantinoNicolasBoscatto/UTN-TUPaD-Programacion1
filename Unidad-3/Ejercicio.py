# 1)
edad = int(input("Ingrese su edad: "))
if (edad > 18):
    print("Usted es mayor de edad")
else:
    print("Usted no es mayor de edad")



# 2)
nota = int(input("Ingrese su nota: "))
if (nota >= 6):
    print("Aprobado")
else: 
    print("Desaprobado")


# 3)
numero = int(input("Ingrese un numero par: "))
if(numero % 2 == 0):
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# 4) 
edad = int(input("Ingrese su edad: "))
if(edad < 12):
    print("Pertenece a la categoria de niño")
elif(edad >= 12 and edad < 18):
    print("Pertenece a la categoria de adolescente")
elif(edad >= 18 and edad < 30):
    print("Pertenece a la categoria de Adulto Joven")
else:
    print("Pertenece a la categoria de Adulto")


# 5)
password = input("Ingrese una contraseña entre 8 y 14 caracteres: ")
if(len(password) >= 8 and len(password) <= 14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")



# 6) 
from statistics import mode, median, mean
import random 

numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
moda = mode(numeros_aleatorios)
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
if(media > mediana and mediana > moda):
    print("Sesgo Positivo")
elif(media < mediana and mediana < moda):
    print("Sesgo Negativo")
else:
    print("Sin Sesgo")


# 7)
cadena = input("Ingrese una frase o palabra: ")
if(cadena[-1].lower() in "aeiou"):
    cadena += "!"
print(cadena)


# 8)
nombre = input("Ingrese su nombre: ")
opcion = int(input("Elija 1 para todo su nombre en mayuscula, 2 para todo su nombre en minuscula y 3 para tener solo la primer letra mayuscula: "))
if(opcion == 1):
    print(nombre.upper())
elif(opcion == 2):
    print(nombre.lower())
else:
    print(nombre.title())


# 9)
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")



# 10)
hemisferio = input("Ingrese su hemisferio, N/S: ")
mes = int(input("Ingrese el mes del año en el que esta: "))
dia = int(input("Ingrese el dia del mes en el que esta: "))

if(hemisferio.upper() == "N"):
    if((mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia < 21)):
        print("Invierno")
    elif((mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia < 21)):
        print("Primavera")
    elif((mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia < 21)):
        print("Verano")
    else:
        print("Otoño")
else:
    if((mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia < 21)):
        print("Verano")
    elif((mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia < 21)):
        print("Otoño")
    elif((mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia < 21)):
        print("Invierno")
    else:
        print("Primavera")