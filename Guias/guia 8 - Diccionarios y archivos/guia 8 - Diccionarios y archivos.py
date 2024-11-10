# DICCIONARIOS - EJERCICIO 16
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

# EJRCICIO 18
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

#print(la_palabra_mas_frecuente('ejemplo.txt'))

# ARCHIVOS - EJERCICIO 21.1
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