
# 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Ingrese un numero: "))
print(f"Los factoriales desde 1 hasta {num}:")
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")


# 2
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Ingrese la posicion hasta la que quiere mostrar Fibonacci: "))
print("Fibonacci:")
for i in range(num):
    print(fibonacci(i), end=" ")



# 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")



# 4
def decimal_a_binario(n):
    if n == 0:
        return "0"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un numero decimal: "))
binario = decimal_a_binario(num)
print(f"El numero {num} en binario es: {binario if binario != '' else '0'}")



# 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ").lower()
print("La palabra es un palindromo" if es_palindromo(texto) else "La palabra no es palindromo")



# 6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

num = int(input("Ingrese un numero: "))
print(f"La suma de los digitos de {num} es {suma_digitos(num)}")



# 7 
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

niveles = int(input("Ingrese la cantidad de bloques de la base de la piramide: "))
print(f"Bloques necesarios para la piramide: {contar_bloques(niveles)}")


# 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

num = int(input("Ingrese un numero: "))
dig = int(input("Ingrese el digito que quiere buscar, de 0 a 9: "))
print(f"El digito {dig} aparece {contar_digito(num, dig)} veces en {num}")

