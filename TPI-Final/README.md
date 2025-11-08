# Gestión de Países en Python

## Descripción del Programa

Este proyecto es una aplicación de consola desarrollada en **Python** para la **gestión de países** almacenados en un archivo **CSV**.  
Permite realizar operaciones como **agregar, actualizar, buscar, filtrar, ordenar y analizar estadísticas** sobre países.

El programa  utiliza estructuras de datos como **listas y diccionarios**, utiliza **funciones modulares**,  hace uso del módulo estándar `csv` para manejar archivos persistentes,  de `unicodedata` para normalizar strings, de `os` para el manejo de archivos y de `sys` para finalizar de forma controlada el programa.


## Instrucciones de Uso

1. **Ejecutar el programa:**  
   Tener instalado Python 3.x o superior.  
   Guarde el script principal (`Ejercicio.py`) y el archivo `paises.csv` en la misma carpeta.  
   Luego ejecute el programa con:
   'python Ejercicio.py'

2. **Archivo CSV:**  
   El archivo base se llama `paises.csv` y debe tener las siguientes cabeceras: nombre,poblacion,superficie,continente. 
   Si el archivo no existe, el programa lo creará automáticamente cuando se agregue el primer país.

3. **Menú principal:**  
   Al iniciar, se mostrará un menú con las siguientes opciones:

   1. Agregar un país
   2. Actualizar población y superficie
   3. Buscar países por nombre
   4. Filtrar países por continente
   5. Filtrar por rango de población
   6. Filtrar por rango de superficie
   7. Ordenar países
   8. Mostrar estadísticas
   9. Mostrar todos los países
   0. Salir

   Debe seleccionar alguna de estas, si no tiene ningun archivo CSV se recomienda primero la opcion cargar pais.


4. **Instrucciones de uso detalladas**
   1. Agregar un país

   Permite incorporar un nuevo país al archivo paises.csv.
   El programa solicitará los siguientes datos:

   Nombre del país (texto)
   Población (número entero)
   Superficie en km² (número entero)
   Continente (texto)

   El sistema verifica que el país no exista ya en la base de datos para evitar duplicados, tambien que el nombre no sea una cadena de espacios.
   Una vez confirmado, el nuevo país se guarda automáticamente en el archivo CSV y se muestra un mensaje de éxito.

   2. Actualizar población y superficie

   Permite modificar los datos de población y superficie de un país.
   El usuario debe ingresar el nombre exacto del país a actualizar.
   Si se encuentra, el programa ofrecerá la posibilidad de actualizar su población y/o superficie.
   Finalmente, los cambios se guardan automáticamente en el archivo CSV.

   3. Buscar países por nombre

   Permite buscar países ingresando todo o parte del nombre.
   El sistema mostrará los resultados coincidentes con sus respectivos datos (nombre, población, superficie y continente).
   Si no se encuentra ninguna coincidencia, se ofrecerá al usuario la opción de realizar otra búsqueda.

   4. Filtrar países por continente

   Muestra únicamente los países pertenecientes a un continente específico.
   El usuario deberá ingresar el nombre del continente (por ejemplo: América, Europa, Asia, etc.). 
   Si el continente ingresado es invalido se lo volvera a pedir (dando la opcion de salir tambien).
   El programa listará solo los países que coincidan.

   5. Filtrar por rango de población

   Permite ver los países cuya población se encuentra dentro de un rango determinado.
   El usuario debe ingresar un mínimo y un máximo de población.
   El programa mostrará todos los países que cumplan con esa condición.

   6. Filtrar por rango de superficie

   Funciona de manera similar al filtro por población, pero aplicado a la superficie.
   El usuario indica un valor mínimo y máximo, y el sistema muestra los países dentro de ese rango.

   7. Ordenar países

   Ordena la lista de países según distintos criterios.
   El usuario puede elegir el campo de ordenamiento:

   Nombre
   Población
   Superficie

   Además, puede seleccionar el sentido del ordenamiento (A–Z / Z–A o ascendente / descendente).
   Una vez ordenados, los países se muestran en pantalla en el nuevo orden.

   8. Mostrar estadísticas

   Calcula y muestra información general sobre los países cargados:

   País con mayor y menor población
   Promedio de población
   Promedio de superficie (km²)
   Cantidad de países por continente

   9. Mostrar todos los países

   Muestra una tabla completa con todos los países cargados en el archivo CSV, incluyendo:

   Nombre
   Población
   Superficie en km²
   Continente


   0. Salir del programa

   Finaliza la ejecución del programa .


5. **Funcionamiento a tener en cuenta:**  
   - El programa valida todas las entradas del usuario para evitar ingreso de data erronea.  
   - Los datos se normalizan para evitar errores por mayúsculas, tildes o espacios. 
   - Los países se guardan automáticamente en el CSV después agregar o modificarlos.  
    



## Ejemplos de Entrada y Salida

**Ejemplo 1: Agregar un país**
```
--- Agregar país ---
Nombre: Argentina
Ingrese la población: 46000000
Ingrese la superficie en km²: 2780400
Ingrese un continente: América
Argentina fue agregado y guardado correctamente.
```



**Ejemplo 2: Buscar país**
```
--- Buscar país ---
Ingrese el nombre de un país o un nombre parcial: Argen
Se encontraron 1 país(es):
Nombre                         Población    Superficie   Continente
---------------------------------------------------------------------------
Argentina                        46000000     2780400 km²   América
```



**Ejemplo 3: Estadísticas**
```
--- Estadísticas ---
País con mayor población: China --- (1400000000)
País con menor población: Paraguay --- (720000)
Promedio de población: 232527500.00
Promedio de superficie en km²: 2861455.00

Cantidad de países por continente:
  - América: 4
  - Asia: 1
  - Europa: 3
  
```



**Ejemplo 4: Actualizar pais**
```
--- Actualizar país ---
Ingrese el nombre exacto del país a actualizar: Argentina
Actualizando datos de Argentina

Desea actualizar la poblacion de Argentina? S para si y cualquier otro valor para no: S
Nueva población: 48500000

Desea actualizar la superficie de Argentina? S para si y cualquier otro valor para no: N
Actualización realizada con éxito.

```

**Ejemplo 5: Imprimir todos los paises**
```
--- Mostrar todos los países ---
Nombre                         Población    Superficie   Continente
---------------------------------------------------------------------------
Uruguay                           3500000      176215 km²   América
Brasil                          212000000     8516000 km²   América
Paraguay                           720000      406752 km²   América
España                            48000000      505990 km²   Europa
Alemania                          83000000      357588 km²   Europa
Francia                           67000000      551695 km²   Europa
China                           1400000000     9597000 km²   Asia
Argentina                        48500000     2780400 km²   América
```



**Ejemplo 6: Ordenar paises de la Z-A**
```
--- Ordenar países ---
1. Por Nombre (A-Z)
2. Por Nombre descendente (Z-A)
3. Población (ascendente)
4. Población (descendente)
5. Superficie (ascendente)
6. Superficie (descendente)
Elegir opción: 2

Nombre                         Población    Superficie   Continente
---------------------------------------------------------------------------
Uruguay                           3500000      176215 km²   América
Paraguay                           720000      406752 km²   América
Francia                           67000000      551695 km²   Europa
España                            48000000      505990 km²   Europa
China                           1400000000     9597000 km²   Asia
Brasil                          212000000     8516000 km²   América
Argentina                        46000000     2780400 km²   América
Alemania                          83000000      357588 km²   Europa
```



## Participación de los Integrantes

- **Santino Boscatto:** Desarrollo de las funciones principales (agregar, actualizar, buscar, filtrar, ordenar), validaciones de datos y manejo de archivos CSV.  
- **Matías Rodríguez:** Diseño previo al codigo, estadísticas y documentación (marco teórico, README, flujo de operaciones).



---
## Tecnologías Utilizadas
- **Lenguaje:** Python 3.12  
- **Librerías estándar:**  
  - `csv` → lectura/escritura de archivos CSV  
  - `os` → manejo de archivos y validaciones  
  - `unicodedata` → normalización de texto  
  - `sys` →  finalizar la ejecución del programa de forma controlada
