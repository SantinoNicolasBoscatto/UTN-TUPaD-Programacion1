import csv
import os
import unicodedata
import sys

CSV_HEADERS = ["nombre", "poblacion", "superficie", "continente"]
ARCHIVO_CSV = 'paises.csv'
CONTINENTES_VALIDOS = ["América", "Europa", "Asia", "África", "Oceanía", "Antártida"]

# --------------------------- FUNCIONES AUXILIARES DE VALIDACION ---------------------------

# Recibe un string y busca normalizar mediante Unicode.
def normalizar_texto(texto=""):
    texto = texto.strip().lower()
    texto = ''.join(
        valor for valor in unicodedata.normalize('NFD', texto)
        if unicodedata.category(valor) != 'Mn'
    )
    return texto

CONTINENTES_NORMALIZADOS = [normalizar_texto(continente) for continente in CONTINENTES_VALIDOS]


# Evalua un valor, si este valor es un INT devuelve un Booleano, verificando si ese INT es un entero positivo o 0. Si no es un INT devuelve falso directamente.
def es_entero_positivo_cero(valor):
    try:
        valor_int = int(valor)
        return valor_int >= 0
    except Exception:
        return False


# Se recibe un valor (se espera un numero), se lo normaliza y evaluamos si es un entero positivo. Si no lo es mostramos msg de error y repetimos.
# Si es un positivo o 0 evaluamos que se no se permita el 0 y que el valor no sea 0, si pasa esta repetimos, sino devolvemos el INT positivo.
def leer_entero(valor_entrante, permitir_valor_cero=True):
    while True:
        valor = input(valor_entrante).strip()
        if es_entero_positivo_cero(valor):
            valor_int = int(valor)
            if (not permitir_valor_cero) and valor_int == 0:
                print("El valor ingresado no puede ser 0, debe ser un entero positivo. Intente de nuevo.")
                continue
            return valor_int
        
        if permitir_valor_cero : print("Entrada inválida. Ingrese un número entero no negativo.")
        else: print("Entrada inválida. Ingrese un número entero positivo.")


def validar_opcion_seguir(key):
    key_normalizada = key.strip().lower()
    if key_normalizada == 's': return True
    return False


# Validacion para saber si un usuario desea seguir buscando algo en un modulo, msg personalizable.
def seguir_buscando(msg='Desea seguir buscando otro pais? S para si y cualquier otro valor para no: '):
    key = input(msg)
    return validar_opcion_seguir(key)




# --------------------------- FUNCIONES PARA EL MANEJO DE CSV ---------------------------


def cargar_paises(archivo_base):
    # Recibimos el nombre del .CSV, declaramos una lista vacia, si el archivo base no existe notificaremos y devolveremos la lista vacia.
    paises = []
    if not os.path.exists(archivo_base):
        print(f"Archivo '{archivo_base}' no existe. Se creará uno nuevo al agregar un pais.")
        return paises

    # Abrimos el archivo y lo leemos, si no tiene cabecera avisaremos y retornaremos el lista vacia, si no contaremos los campos de la cabecera, los cuales deben ser 4. Si no 
    # es asi marcamos el error y devolvemos la lista.
    try:
        with open(archivo_base, newline='', encoding='utf-8') as archivo_read:
            reader = csv.reader(archivo_read)
            try:
                header = next(reader)
            except StopIteration:
                print("El CSV esta vacío.")
                return paises

            header = [h.strip() for h in header]
            if len(header) < 4:
                print("Error: El CSV no tiene suficientes columnas (se esperan: nombre,poblacion,superficie,continente).")
                return paises

            # Extraemos el index de cada campo de la cabecera, salta un error si el campo no existe en la cabecera y retornamos la lista.
            try:
                index_nombre = header.index('nombre')
                index_poblacion = header.index('poblacion')
                index_superficie = header.index('superficie')
                index_continente = header.index('continente')
            except ValueError:
                print("Error: El CSV debe contener las cabeceras: nombre,poblacion,superficie,continente")
                return paises

            linea_numero = 1
            # Vamos a iterar cada fila del CSV, empezando por la 2 (salteamos la cabecera). Verificamos que al menos una fila tiene contenido y que esa fila tenga las 
            # columnas/campos esperados.
            for row in reader:
                linea_numero += 1
                if not any(cell.strip() for cell in row):
                    continue
                if index_continente >= len(row):
                    print(f"Advertencia: la fila {linea_numero} tiene menos columnas de las esperadas. Se ignorara.")
                    continue

                # Extraigo la data usando los indices y normalizandola borrando espacios
                nombre = row[index_nombre].strip()
                poblacion = row[index_poblacion].strip()
                superficie = row[index_superficie].strip()
                continente = row[index_continente].strip()


                # Validamos que no haya campos vacios y que los campos numericos sean validos (no haya valores negativos), si hay un error se saltea la fila
                if not nombre or not poblacion or not superficie or not continente:
                    print(f"Advertencia: fila {linea_numero} contiene campos vacíos. Se ignorara.")
                    continue

                if not es_entero_positivo_cero(poblacion) or not es_entero_positivo_cero(superficie):
                    print(f"Advertencia: fila {linea_numero} tiene un formato numérico inválido. Se ignorara.")
                    continue

                # Creo un diccionario con los datos y lo agrego a la lista de paises.       
                pais = {
                    'nombre': nombre,
                    'poblacion': int(poblacion),
                    'superficie': int(superficie),
                    'continente': continente
                }
                paises.append(pais)
        return paises
    except UnicodeDecodeError:
        sys.exit("El archivo CSV no se encuentra en UTF-8, por favor corrija este archivo y reintente abrir el programa.")

# Funcion para guardar los paises en el CSV, recibe una lista de paises y el nombre del .CSV. Abre el archivo en modo escritura, creamos el writer, escribimos las cabeceras (constante global) e iteramos los paises para escribir linea por linea en el CSV. Si todo fue OK se devuelve True, si hubo algun error y salto una excepcion False.
def guardar_paises(paises, archivo_base):
    try:
        with open(archivo_base, 'w', newline='', encoding='utf-8') as archivo_read:
            writer = csv.writer(archivo_read)
            writer.writerow(CSV_HEADERS)
            for pais in paises:
                writer.writerow([pais['nombre'], str(pais['poblacion']), str(pais['superficie']), pais['continente']])
            return True
    except Exception:
        return False





# --------------------------- FUNCIONES AUXILIARES DE PAISES ---------------------------


# Recibe la lista de paises y el nombre del pais a comprobar existencia. Normalizo el nombre y busco la lista el pais (normalizando los nombres tambien)
# Si existe devuelve el index y si no un -1
def existe_pais(paises, nombre):
    nombre_normalizado = normalizar_texto(nombre)
    for index, pais in enumerate(paises):
        if normalizar_texto(pais['nombre']) == nombre_normalizado:
            return index
    return -1


def hay_paises(paises, msg):
    bandera_paises = len(paises) > 0
    if not bandera_paises:
        print(msg)
    return bandera_paises





# --------------------------- FUNCIONES PRINCIPALES DE PAISES ---------------------------


# Recibe la lista, el primer ciclo pide el nombre del pais, verifica que no este vacio (en caso de estarlo muestra el error y repite el ciclo) y si ese pais existe (si existe
# sale de la funcion, avisando que existe). Si esta todo ok rompe el while.
def agregar_pais(paises, archivo_csv):
    print('\n--- Agregar país ---')
    while True:
        nombre = input('Nombre: ').strip()
        if not nombre:
            print('El nombre no puede estar vacío. Intente de nuevo.')
            continue
        if existe_pais(paises, nombre) >= 0:
            print('Ya existe un país con ese nombre. Use el modulo de actualizar si quiere modificarlo.')
            return
        break

    # Valido que poblacion y superficie sean enteros mayores a 0. 
    poblacion = leer_entero('Ingrese la población: ', False)
    superficie = leer_entero('Ingrese la superficie en km²: ', False)

    while True:
        continente = input('Ingrese un continente: ').strip()
        if not continente:
            print('El continente no puede estar vacío.')
            continue

        continente_normalizado = normalizar_texto(continente)
        bandera = False
        for index, continente_base_normalizado in enumerate(CONTINENTES_NORMALIZADOS):
            if continente_base_normalizado == continente_normalizado:
                continente = CONTINENTES_VALIDOS[index]
                bandera = True
                break
        
        if not bandera: 
            print(f"Error: '{continente}' no es un continente válido.")
            print(f"Continentes válidos: {', '.join(CONTINENTES_VALIDOS)}\n")
            continue

        break

    # Si todos los datos estan OK los guardo en un diccionario y agrego este a la lista de paises.
    pais = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }
    paises.append(pais)
    resultado = guardar_paises(paises, archivo_csv)
    if resultado: print(f"{nombre} fue agregado y guardado correctamente.")
    else: print(f"Error: Un error desconocido impidio guardar el pais {nombre}, revise los datos ingresados e intente nuevamente.")
    

# Recibe la lista de paises y el CSV, se pide el nombre del pais a actualizar (exacto) y verificamos si existe. 
def actualizar_pais(paises,  archivo_csv):
    print('\n--- Actualizar país ---')
    if not hay_paises(paises, 'No hay paises cargados en el CSV. Por favor cargue un pais al menos antes de intentar actualizarlos.'): 
        return

    while True:
        nombre = input('Ingrese el nombre exacto del país a actualizar: ').strip()
        index = existe_pais(paises, nombre)

        # Si no existe preguntamos si quiere buscar otro, si es asi repetimos ciclo y si no retornamos.
        if index < 0:
            print('No se encontró un país con ese nombre exacto.')
            if seguir_buscando(): continue
            return


        print(f"Actualizando datos de {paises[index]['nombre']}\n")
        if seguir_buscando(f"Desea actualizar la poblacion de {paises[index]['nombre']}? S para si y cualquier otro valor para no: "):
            poblacion = leer_entero('Nueva población: ', False)
            paises[index]['poblacion'] = poblacion
        
        if seguir_buscando(f"\nDesea actualizar la superficie de {paises[index]['nombre']}? S para si y cualquier otro valor para no: "):
            superficie = leer_entero('Nueva superficie en km²: ', False)
            paises[index]['superficie'] = superficie


        # Guardo y lanzo un MSG de la operacion, luego rompo.
        resultado = guardar_paises(paises, archivo_csv)
        if resultado: print('Actualización realizada con éxito.')
        else: print(f"Error: Un error desconocido impidio actualizar el pais {nombre}, revise los datos ingresados e intente nuevamente.")

        break


# Recibimos la lista de paises, hacemos la verificacion de que no este buscando un vacio.
def buscar_pais(paises):
    print('\n--- Buscar país ---')
    if not hay_paises(paises, 'No hay paises cargados en el CSV. Por favor cargue un pais al menos antes de buscar.'): 
        return


    while True:
        nombre = input('Ingrese el nombre de un pais o un nombre parcial: ').strip()
        if not nombre:
            print('El nombre esta vacío. ')
            if seguir_buscando(): continue
            return
        break
    
    # Normalizamos la entrada y la buscamos en los paises normalizados. Se manda un msg segun el resultado
    nombre_normalizado = normalizar_texto(nombre)
    encontrados = [
        pais for pais in paises
        if nombre_normalizado in normalizar_texto(pais['nombre'])
    ]
    if not encontrados:
        print('No se encontraron países que coincidan con la búsqueda.')
        return
    print(f"Se encontraron {len(encontrados)} país(es):")
    imprimir_paises(encontrados)


# Recibimos la lista de paises, hacemos la verificacion de que no este buscando un vacio.
def filtrar_por_continente(paises):
    print('\n--- Filtrar por continente ---')
    if not hay_paises(paises, 'No hay paises cargados en el CSV. Por favor cargue un pais al menos antes de querer filtrar.'): 
        return

    while True:
        continente = input('Ingrese el nombre del continente por el que desea buscar, debe ser el nombre exacto: ')

        if not continente:
            print('Ingreso un continente vacio.')
            if seguir_buscando('Desea filtrar por otro continente? S para si y cualquier otro valor para no: '):
                continue
            return
        
        # Normalizamos la entrada y la buscamos en la lista de continentes normalizados.
        continente_normalizado = normalizar_texto(continente)
        if continente_normalizado not in CONTINENTES_NORMALIZADOS:
            print(f"Error: '{continente}' no es un continente válido.")
            print(f"Continentes válidos: {', '.join(CONTINENTES_VALIDOS)}\n")
            if seguir_buscando('Desea filtrar por otro continente? S para si y cualquier otro valor para no: '): 
                continue
            return
        break
    
    # Si el continente normalizado existe, extraigo el index y lo uso para optener el contienente original sin normalizar
    index = CONTINENTES_NORMALIZADOS.index(continente_normalizado)
    continente_real = CONTINENTES_VALIDOS[index]

    # Si coincide entre si los continentes normalizados los agrego a resultado y mostramos los resultados por pantalla.
    resultado = [
        pais for pais in paises
        if normalizar_texto(pais['continente']) == continente_normalizado
    ]

    if not resultado:
        print(f'No hay países registrados del continente "{continente_real}".')
        return

    print(f'\nPaíses del continente "{continente_real}":')
    imprimir_paises(resultado)


# Recibimos la lista de paises
def filtrar_por_rango_poblacion(paises):
    print('\n--- Filtrar por rango de población ---')
    if not hay_paises(paises, 'No hay paises cargados en el CSV. Por favor cargue un pais al menos antes de querer filtrar.'): 
        return
    
    # Pedimos los rangos y verificamos que sean validos
    while True:
        min_p = leer_entero('Población mínima: ', False)
        max_p = leer_entero('Población máxima: ', False)
        if max_p < min_p:
            print('Rango inválido: el máximo es menor que el mínimo.')         
            if seguir_buscando('Desea seguir buscando con otro rango? S para si y cualquier otro valor para no: '): 
                continue
            return
            
        # Guardamos en resultado los paises que cumplan con la condicion
        resultado = [pais for pais in paises if min_p <= pais['poblacion'] <= max_p]
        if not resultado:
            print('No se encontraron países dentro del rango de población indicado.')
            return
        imprimir_paises(resultado)
        break


# Similar a la logica de poblacion
def filtrar_por_rango_superficie(paises):
    print('\n--- Filtrar por rango de superficie ---')

    if not hay_paises(paises, 'No hay paises cargados en el CSV. Por favor cargue un pais al menos antes de querer filtrar.'): 
        return
    

    while True:
        min_s = leer_entero('Superficie mínima en km²: ', False)
        max_s = leer_entero('Superficie máxima en km²: ', False)
        if max_s < min_s:
            print('Rango inválido: el máximo es menor que el mínimo.')
            if seguir_buscando('Desea seguir buscando con otro rango? S para si y cualquier otro valor para no: '): 
                continue
            return
        
        resultado = [pais for pais in paises if min_s <= pais['superficie'] <= max_s]
        if not resultado:
            print('No se encontraron países dentro del rango de superficie indicado.')
            return
        imprimir_paises(resultado)
        break


# Recibimos la lista de paises y mostramos las opciones al usuario (Antes verificamos que hayan paises).
def ordenar_paises(paises):
    print('\n--- Ordenar países ---')

    if not hay_paises(paises, 'No hay paises cargados en el CSV. Por favor cargue paises antes de querer ordenarlos.'): 
        return
    
    while True:
        print('\n1. Por Nombre (A-Z)')
        print('2. Por Nombre descendente (Z-A)')
        print('3. Población (ascendente)')
        print('4. Población (descendente)')
        print('5. Superficie (ascendente)')
        print('6. Superficie (descendente)')

        # Estas funciones se usaran para ordenar, son auxiliares que devuelven el valor a usar como criterio de ordenamiento.
        # La usaremos con sorted para comparar paises y realizar los ordenamientos
        def clave_nombre(pais):
            return pais['nombre'].lower()
        def clave_poblacion(pais):
            return pais['poblacion']
        def clave_superficie(pais):
            return pais['superficie']

        # Pedimos al usuario una opcion
        opcion = input('Elegir opción: ').strip()
        match opcion:
            case '1':
                resultados = sorted(paises, key=clave_nombre)
            case '2':
                resultados = sorted(paises, key=clave_nombre, reverse=True)
            case '3':
                resultados = sorted(paises, key=clave_poblacion)
            case '4':
                resultados = sorted(paises, key=clave_poblacion, reverse=True)
            case '5':
                resultados = sorted(paises, key=clave_superficie)
            case '6':
                resultados = sorted(paises, key=clave_superficie, reverse=True)
            case _:
                print('\nOpción inválida.')
                if seguir_buscando('Desea ingresar otra opcion? S para si y cualquier otro valor para no: '): continue
                return

        imprimir_paises(resultados)
        break


# Se recibe la lista de paises, se verifica que no este vacia.
def mostrar_estadisticas(paises):
    print('\n--- Estadísticas ---')
    if not hay_paises(paises, 'No hay paises cargados en el CSV. Por favor cargue un pais al menos antes de mostrar las estadisticas.'): 
        return

    # Funcion que se usara para sacar la poblacion maxima y minima 
    def clave_poblacion(pais):
        return pais['poblacion']
    mayor = max(paises, key=clave_poblacion)
    menor = min(paises, key=clave_poblacion)

    # Sumamos todas las poblaciones de todos los paises y luego lo dividimos por la cantidad de paises para sacar el promedio (idem para superficie).
    total_poblacion = sum(pais['poblacion'] for pais in paises)
    total_superficie = sum(pais['superficie'] for pais in paises)
    promedio_poblacion = total_poblacion / len(paises)
    promedio_superficie = total_superficie / len(paises)

    # Creo un diccionario para el conteo de paises por continente. Extraigo el nombre del continente y con .get(key, 0) busco si ya existe el continente en el DIC, 
    # si no existe inicio el value en 0 y luego (independientemente exista o no) le sumo 1.
    conteo_continente = {}
    for pais in paises:
        key = pais['continente'].strip()
        conteo_continente[key] = conteo_continente.get(key, 0) + 1

    # Muestro las estadisticas
    print(f"País con mayor población: {mayor['nombre']} --- ({mayor['poblacion']})")
    print(f"País con menor población: {menor['nombre']} --- ({menor['poblacion']})")
    print(f"Promedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie en km²: {promedio_superficie:.2f}")

    print('\nCantidad de países por continente:')
    for continente, cantidad in sorted(conteo_continente.items()):
        print(f"  - {continente}: {cantidad}")


def imprimir_paises(paises):
    if not hay_paises(paises, 'No hay paises que mostrar.'): 
        return
    print('\n{:<30} {:>12} {:>12}   {:<15}'.format('Nombre', 'Población', 'Superficie', 'Continente'))
    print('-' * 75)
    for pais in paises:
        print('{:<30} {:>12} {:>12}   {:<15}'.format(
            pais['nombre'], str(pais['poblacion']), f"{pais['superficie']} km²", pais['continente']))
    print()




# --------------------------- MENU Y BLOQUE MAIN ---------------------------

def menu_principal(paises, archivo_csv):
    while True:
        print('\n===== GESTION DE PAISES =====')
        print('1. Agregar un país')
        print('2. Actualizar poblacion y superficie de un pais')
        print('3. Buscar paises por nombre')
        print('4. Filtrar paises por continente')
        print('5. Filtrar paises por rango de población')
        print('6. Filtrar paises por rango de superficie')
        print('7. Ordenar países')
        print('8. Mostrar estadísticas')
        print('9. Mostrar todos los países')
        print('0. Salir')

        opcion = input('\nSeleccione una opción: ').strip()

        match opcion:
            case '1':
                agregar_pais(paises, archivo_csv)
            case '2':
                actualizar_pais(paises, archivo_csv)
            case '3':
                buscar_pais(paises)
            case '4':
                filtrar_por_continente(paises)
            case '5':
                filtrar_por_rango_poblacion(paises)
            case '6':
                filtrar_por_rango_superficie(paises)
            case '7':
                ordenar_paises(paises)
            case '8':
                mostrar_estadisticas(paises)
            case '9':
                imprimir_paises(paises)
            case '0':
                print('Saliendo...')
                break
            case _:
                print('Opción inválida. Intente nuevamente.')


def main(archivo_csv):
    paises = cargar_paises(archivo_csv)
    print(f"Se cargaron {len(paises)} país/es desde '{archivo_csv}'.")
    menu_principal(paises, archivo_csv)

try:
    main(ARCHIVO_CSV)
except KeyboardInterrupt:
    print('\nInterrumpido por el usuario. Saliendo...')
