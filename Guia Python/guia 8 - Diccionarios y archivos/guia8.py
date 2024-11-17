import math
from queue import LifoQueue as Pila
from queue import Queue as Cola

# DICCIONARIOS - EJERCICIO 16
"""
with open("ejemplo.txt") as archivo:
    def agrupar_por_longitud(nombre_archivo:str) -> dict[int,int]:
        archivo = open(nombre_archivo, 'r')
        diccionario: dict[int,int] = dict() #otra forma de crear un diccionario vacio : {}
        for linea in archivo.readlines():
            palabras:list[str] = linea.split() #crea una lista con cada palabra sin espacios
        for palabra in palabras:
            clave:int = len(palabra)
            if clave in diccionario: # este in es sobre diccionario, se puede usar
                diccionario[clave] += 1
            else:
                diccionario[clave] = 1
        archivo.close()
        return diccionario

print(agrupar_por_longitud('ejemplo.txt'))
"""
# EJERCICIO 17
def calcular_promedio_por_estudiante(notas: list[tuple[str, float]]) -> dict[str, float]:
    res: dict[str, float] = {}
    for nota in notas:
        prom: float = calcular_promedio(nota[0], notas)
        res[nota[0]] = prom #agrego al diccionario nombreEstudiante : promedio de sus notas
        
    return res

def calcular_promedio(estudiante: str, notas: list[tuple[str, float]]) -> float:
    cant_notas: int = 0
    suma_notas: int = 0
   
    for nota in notas:
        if nota[0] == estudiante:
            cant_notas += 1
            suma_notas += nota[1]

    return suma_notas/cant_notas


notas = [["P1", 3], ["P2", 5],["P1", 6], ["P3", 10],["P3", 10], ["P1", 6]]
print(calcular_promedio_por_estudiante(notas))


"""
# EJRCICIO 18
with open("ejemplo.txt") as archivo:
    def la_palabra_mas_frecuente(nombre_archivo:str) -> str:
        archivo = open(nombre_archivo, 'r')
        diccionario:dict[str,int] = dict() # las claves son palabras y los valores la frecuencia
        for linea in archivo.readlines():
            palabras:list[str] = linea.split() #crea una lista con cada palabra sin espacios
            for palabra in palabras:
                clave:int = palabra
                if clave in diccionario: # este in es sobre diccionario, se puede usar
                    diccionario[clave] += 1
                else:
                    diccionario[clave] = 1
        max_palabra:int = ''
        max_apariciones:int = 0
        for clave in diccionario:
            valor_actual:int = diccionario[clave]
            if valor_actual > max_apariciones:
                max_palabra = clave
                max_apariciones = valor_actual
        archivo.close()
        return max_palabra

print(la_palabra_mas_frecuente('ejemplo.txt'))
"""
#EJERCICIO 19
#historiales: historial de navegacion para cada usuario. Las claves del diccionario seran los nombres de usuario y los valores seran pilas.
def visitar_sitio(historiales: dict[str, Pila[str]], usuario: str, sitio: str) -> None:
    if usuario in historiales.keys():
        historiales[usuario].put(sitio)
    else:
        historiales[usuario] = Pila()
        historiales[usuario].put(sitio)


def navegar_atras(historiales: dict[str, Pila[str]], usuario: str) -> None:
    ultimo_sitio = historiales[usuario].get()
    sitio_anterior = historiales[usuario].get()
    historiales[usuario].put(ultimo_sitio)
    historiales[usuario].put(sitio_anterior)

historiales = {}
visitar_sitio(historiales, "Usuario1", "google.com")
visitar_sitio(historiales, "Usuario1", "facebook.com")
print(historiales['Usuario1'].queue)
navegar_atras(historiales, "Usuario1")
print(historiales['Usuario1'].queue)
visitar_sitio(historiales, "Usuario2", "youtube.com")
print(historiales['Usuario2'].queue)

# EJERCICIO 20
def agregar_producto(inventario:dict[str, dict[str, float | int]], nombre:str, precio:float, cantidad:int) -> None:
    if nombre not in inventario.keys():
        inventario_aux = {
            "precio": precio,
            "cantidad": cantidad,
    }
        inventario[nombre] = inventario_aux

def actualizar_stock(inventario:dict[str, dict[str, float | int]], nombre:str, cantidad:int) -> None:
    if nombre in inventario.keys():
        inventario[nombre]['cantidad'] = cantidad

def actualizar_precios(inventario:dict[str, dict[str, float | int]], nombre:str, precio:float) -> None:
    if nombre in inventario.keys():
        inventario[nombre]['precio'] = precio

def calcular_valor_inventario(inventario:dict[str, dict[str, float | int]]) -> float:
    precio:float = 0
    for nombre in inventario.values():
        precio += nombre['precio'] * nombre['cantidad']
    return precio

inventario = {}
agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantalon", 30.0, 30)
print(inventario)
actualizar_stock(inventario, "Camisa", 10)
actualizar_precios(inventario, "Pantalon", 30.9)
print(inventario)
valor_total = calcular_valor_inventario(inventario)
print("Valor total del inventario:", valor_total) # Deberıa imprimir 2100.0

"""
# ARCHIVOS - EJERCICIO 21.1
with open("hola.txt") as archivo:
    def contar_lineas(nombre_archivo:str) -> int:
        contador:int = 0
        archivo = open(nombre_archivo, 'r') #read
        for linea in archivo.readlines(): #devuelve una lista con cada salto de linea
            contador += 1
        archivo.close()
        return contador

    print(contar_lineas('hola.txt'))

# EJERCICIO 22
def clonar_sin_comentarios(nombre_archivo_entrada:str, nombre_archivo_salida:str) -> None:
    archivo_entrada = open(nombre_archivo_entrada, 'r') 
    archivo_salida = open(nombre_archivo_salida, 'w') #escritura
    for linea in archivo_entrada.readlines():
        if linea.strip()[0] != '#': #STRIP NO ESTA ADMITIDO
            archivo_salida.write(linea)
    archivo_entrada.close
    archivo_salida.close

#def eliminar_espacios() #HACER

clonar_sin_comentarios('hola.txt','chau.txt')
"""