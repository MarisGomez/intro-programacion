from queue import LifoQueue as Pila
from queue import Queue as Cola
c = Cola
p = Pila

# 1) Fila en ExactaBank (1 puntos)

# problema reordenar_cola_priorizando_vips(in filaClientes: Cola<String x String>): Cola <String> {
# requiere: {La longitud de los valores de la primera componente de las tuplas de la cola filaClientes es mayor a 0}
# requiere: {Los valores de la segunda componente de las tuplas de la cola filaClientes son "comun" o "vip"}
# requiere: {No hay dos tuplas en filaClientes que tengan la primera componente iguales entre sí}
# asegura: {todo valor de res aparece como primera componente de alguna tupla de filaClientes}
# asegura: {|res| = |filaCliente|}
# asegura: {res no tiene elementos repetidos}
# asegura: {No hay ningun cliente "comun" antes que un "vip" en res}
# asegura: {Para todo cliente c1 y cliente c2 de tipo "comun" perteneceientes a filaClientes si c1 aparece antes que c2 en
# filaClientes entonces el nombre de c1 aparece antes que el nombre de c2 en res}
# asegura: {Para todo cliente c1 y cliente c2 de tipo "vip" perteneceintes a filaClientes si c1 aparece antes que c2 en filaClientes
# entonces el nombre de c1 aparece antes que el nombre de c2 en res}
# }


def reordenar_cola_priorizando_vips(filaClientes: Cola[str, str]) -> Cola[str]:
    fila_vip: Cola = Cola()
    fila_comun: Cola = Cola()
    nuevo_orden: Cola = Cola()
    contenedor: Cola = Cola()
    while not filaClientes.empty():
        clienteActual = filaClientes.get()
        contenedor.put(clienteActual)
        if clienteActual[1] == "vip":
            fila_vip.put(clienteActual[0])
        elif clienteActual[1] == "comun":
            fila_comun.put(clienteActual[0])
    while not contenedor.empty(): # restauro la cola original
        filaClientes.put(contenedor.get())

    while not fila_vip.empty():
        nuevo_orden.put(fila_vip.get())
    while not fila_comun.empty():
        nuevo_orden.put(fila_comun.get())

    return nuevo_orden

filaClientes: Cola = Cola()
filaClientes.put(("juan", "vip")) #1
filaClientes.put(("ana", "vip")) #2
filaClientes.put(("seba", "comun")) #5
filaClientes.put(("rodo", "vip")) #3
filaClientes.put(("alejo", "comun")) #6
filaClientes.put(("leo", "comun")) #7
filaClientes.put(("vale", "vip")) #4
print(reordenar_cola_priorizando_vips(filaClientes).queue)
print(filaClientes.queue)

# 4) Cuántos palíndromos sufijos (2 puntos)

# Decimos que una palabra es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda. Se nos pide
# programar en python la siguiente función:

# problema cuantos_sufijos_son_palindromos(in texto:String) : Z{
# requiere: -
# asegura: {res es igual a la cantidad de palíndromos que hay en el conjunto de sufijos de texto}
# }

# Nota: un sufijo es una subsecuencia de texto que va desde una posición cualquiera hasta el final de la palabra. Ej: "Diego",
# el conjunto de sufijos es: "Diego", "iego", "ego", "go", "o". Para este ejercicio no consideramos a "" como sufijo de ningún
# texto.

def es_polindromo(palabra: str) -> bool:
    res: bool
    indice:int = 0
    while indice < len(palabra):
        if palabra[indice] != palabra[len(palabra) - 1 - indice]:
            return False
        indice += 1
    res = True
    return res

def sacar_primera_letra(palabra: str) -> str:
    palabra_nueva: str = ""
    for i in range(1,len(palabra)):
        palabra_nueva += palabra[i]
    return palabra_nueva

def cuantos_sufijos_son_palindromos(texto: str) -> int:
    res: int = 0
    while len(texto) > 0:
        if es_polindromo(texto):
            res += 1
            texto = sacar_primera_letra(texto)
        else:
            texto = sacar_primera_letra(texto)
    return res

print(cuantos_sufijos_son_palindromos("anana"))

######################################################################################################
# 1) Códigos filtrados [2 puntos]

# Se pide implementar una función que, dada una secuencia de enteros, cada uno representando un código 
# de barras de un producto, cree y devuelva una nueva lista que contenga únicamente aquellos números de 
# la lista original cuyos últimos tres dígitos formen un número primo (por ejemplo, 101, 002 y 011).

# Nota: un número primo es aquel que solo es divisible por si mismo y por 1. Algunos ejemplos de hasta 
# tres dígitos son 2, 3, 4, 101, 103, 107, etc.

# problema filtrar_codigos_primos(in codigos_barra: seq<Z>) : seq<Z> {
# requiere: {Todos los enteros de codigos_barra tienen, por lo menos, 3 dígitos}
# requiere: {No hay elementos repetidos en codigos_barra}
# asegura: {los últimos 3 dígitos de cada uno de los elementos de res forman un número primo}
# asegura: {Todos los elementos de codigos_barra cuyos últimos 3 dígitos forman un número primo 
# están en res}
# asegura: {Todos los elementos de res están en codigos_barra}
# }

def ultimos_tres_numeros(n: int) -> int:
    num: str = str(n)
    while len(num) > 3:
        num = sacar_primera_letra(num)
    numero = int(num)
    return numero

def divisores(n: int) -> list[int]:
    res: list[int] = []
    indice: int = 1
    while indice <= n:
        if n % indice == 0:
            res.append(indice)
            indice += 1
        else:
            indice += 1
    return res

def es_primo(n: int) -> bool:
    res: bool = False
    if len(divisores(n)) == 2:
        res = True
    return res

def filtrar_codigos_primos(codigos_barra: list[int]) -> list[int]:
    res: list[int] = []
    for i in range(0,len(codigos_barra)):
        elem = codigos_barra[i]
        if es_primo(ultimos_tres_numeros(elem)):
            res.append(elem)
    return res

print(filtrar_codigos_primos([101, 38435028, 4742019, 95472986]))

# 2) Cambios de stock de stock_productos [2 puntos]

# Se pide implementar una función que reciba una lista de tuplas, donde cada tupla contiene el nombre de 
# un producto y su stock en ese momento. La función debe procesar esta lista y devolver un diccionario 
# que tenga como clave el nombre del producto y como valor una tupla con su mínimo y máximo stock histórico
# registrado.

# problema stock_productos(in stock_cambios: seq<<String X Z>>): dict<String, <Z X Z>>{
# requiere: {Todos los elementos de stock_cambios están formados por un string no vacío y un entero >= 0}
# asegura: {res tiene como claves solo los primeros elementos de las tuplas de stock_cambios (o sea, un
# producto)}
# asegura: {res tiene como claves todos los primeros elementos de las tuplas de stock_cambios}
# asegura: {El valor en res de un producto es una tupla de cantidades. Su primer elemento es la menor 
# cantidad de ese producto en stock_cambios y como segundo valor el mayor}
# }
def stock_productos(stock_cambios: list[(str, int)]) -> dict[str,(int, int)]:
    diccionario: dict[str, (int, int)] = {}
    for producto in stock_cambios:
        clave = producto[0]
        if clave not in diccionario.keys():
            minimo = producto[1]
            maximo = producto[1]
        else:
            if producto[1] < minimo:
                minimo = producto[1]
            elif producto[1] > maximo:
                maximo = producto[1]
        diccionario[clave] = (minimo, maximo)
    return diccionario

sc1 = [("galletita", 12),("galletita", 10),("galletita", 1),("hueso",120),("hueso",3),("hueso",10)] #{"galletita":(1,12), "hueso":(3,120)}
print(stock_productos(sc1))

######################################################################################################
#1) Gestión de notas de estudiantes [2 puntos]

#En una escuela llamada "Academia Futura", se desea desarrollar un programa para gestionar las notas de los 
#estudiantes por materia. El programa debe procesar una lista de tuplas donde cada tupla contiene el nombre de un estudiante, el nombre de una materia 
#y la nota final obtenida por el estudiante en esa materia.

#Se pide implementar una función en python, que respete la siguiente especificación:

#problema gestion_notas (in notas_estudiante_materia: seq⟨(String x String x Z)) : dict⟨String, seq⟨(String x Z)⟩⟩ {
#  requiere: { Las primeras componentes de notas_estudiante_materia tienen longitud mayor estricto a cero}
#  requiere: { Las segundas componentes de notas_estudiante_materia tienen longitud mayor estricto a cero}
#  requiere: { Las terceras componentes de notas_estudiante_materia están entre 1 y 10, ambos inclusive }
#  requiere: { No hay 2 tuplas en notas_estudiante_materia que tengan la primera y segunda componente iguales (mismo estudiante y misma materia) }
#  asegura: {res tiene como claves solo los primeros elementos de las tuplas de notas_estudiante_materia (o sea, un estudiante)}
#  asegura: {El valor en res de un estudiante es una lista de tuplas donde cada tupla contiene como primera componente el nombre de la materia y como 
#            segunda componente la nota obtenida por el estudiante en esa materia según notas_estudiante_materia}
#  asegura: { Para toda clave (estudiante) en res, en su valor (lista de tuplas) no hay 2 tuplas que tengan la misma primera componente (materia) }
#}

def gestion_notas(notas_estudiante_materia: list[tuple[str, str, int]]) -> dict[str, list[tuple[str,int]]]:
    diccionario: dict[str, list[tuple[str,int]]] = {}
    for nota in notas_estudiante_materia:
        clave = nota[0]
        if clave not in diccionario.keys():
            diccionario[clave] = [(nota[1], nota[2])]
        else:
            diccionario[clave].append((nota[1], nota[2]))
    return diccionario

n1 = [('Juan', 'Geografía', 5),('Ana', 'Matemática', 9),('Lucas', 'Lengua y Literatura', 6),('Ana', 'Lengua y Literatura', 4),('Juan', 'Matemática', 5)]
print(gestion_notas(n1))

#2) Cantidad dígitos pares [2 puntos]
#Se pide implementar una función en Python llamada cantidad_digitos_pares que respete la siguiente especificación:

#problema cantidad_digitos_pares (in numeros: seq⟨Z⟩) : Z {
#  requiere:{Todos los elementos de numeros son mayores iguales a 0}
#  asegura: {res es la cantidad total de digitos pares que aparecen en cada uno de los elementos de numeros}
#}
#Por ejemplo, si la lista de números es [5434, 42, 811, 3139], entonces el resultado esperado sería 5 (los dígitos pares son 4, 4, 4, 2, y 8).

def cantidad_digitos_pares(numeros:list[int]) -> int:
    res: int = 0
    for n in numeros:
        numero = str(n)
        for i in range(0,len(numero)):
            num = int(numero[i])
            if num % 2 == 0:
                res += 1
    return res

print(cantidad_digitos_pares([5434, 42, 811, 3139]))
print(cantidad_digitos_pares([111, 351, 997]))

#3) Priorizar cola de paquetes [2 puntos]
#En una empresa de logística, se manejan paquetes que llegan a una bodega y deben ser procesados para su posterior distribución. Cada paquete está 
#representado por una tupla (id_paquete, peso), donde id_paquete es un identificador único del paquete y peso representa el peso del paquete en kilogramos.

#Se pide implementar una función en Python llamada reordenar_cola_primero_pesados que respete la siguiente especificación:

#problema reordenar_cola_primero_pesados(in paquetes: Cola⟨(String x Z)⟩, in umbral:Z): Cola⟨(String x Z)⟩{
#  requiere: {no hay repetidos en las primeras componentes (Ids) de paquetes}
#  requiere: {todos las segundas componentes (pesos) de paquetes son mayores estricto a cero}
#  requiere: {umbral es mayor o igual a cero}
#  asegura: {los elementos de res son exactamente los mismos que los elementos de paquetes}
#  asegura: {|res| = |paquetes|}
#  asegura: {no hay un elemento en res, cuyo peso sea menor o igual que el umbral, que aparezca primero que otro elemento en res cuyo peso sea mayor que 
#            el umbral)}
#  asegura: {Para todo paquete p1 y paquete p2 cuyos pesos son menores o iguales que el umbral y pertenecen a paquetes si p1 aparece primero que p2 en 
#            paquetes entonces p1 aparece primero que p2 en res}
#  asegura: {Para todo paquete p1 y paquete p2 cuyos pesos son mayores que el umbral y pertenecen a paquetes si p1 aparece primero que p2 en paquetes entonces 
#            p1 aparece primero que p2 en res}
#}

def reordenar_cola_primero_pesados(paquetes: Cola[tuple[str,int]], umbral:int) -> Cola[tuple[str,int]]:
    res: Cola = Cola()
    debajo_umbral: Cola = Cola()
    contenedor: Cola = Cola()
    while not paquetes.empty():
        paquete = paquetes.get()
        contenedor.put(paquete)
        if paquete[1] > umbral:
            res.put(paquete)
        else:
            debajo_umbral.put(paquete)
    while not debajo_umbral.empty():
        paquete_chico = debajo_umbral.get()
        res.put(paquete_chico)
    while not contenedor.empty():
        paquetes.put(contenedor.get())
    return res

c1: Cola[tuple[str,int]] = Cola()
c1.put(('A', 40))
c1.put(('B', 10))
c1.put(('C', 39))
c1.put(('D', 41))
print(reordenar_cola_primero_pesados(c1,39).queue) #([('A', 40), ('D', 41), ('B', 10), ('C', 39)])

#4) Matriz pseudo ordenada [2 puntos]
#Se desea verificar si una matriz está pseudo ordenada por columnas. Esto es que el mínimo de cada columna sea menor estricto que el mínimo de la columna siguiente

#Para ello se pide desarrollar una función en Python que implemente esta idea respetando la siguiente especificación:

#matriz_pseudo_ordenada (in matriz: seq⟨seq⟨Z⟩⟩): Bool {
#  requiere: {|matriz| > 0}
#  requiere: {|matriz[0]| > 0}
#  requiere: {todos los elementos de matriz tienen la misma longitud}
#  asegura: {res es igual a True <=> para todo 0<=i<|matriz[0]|-1, el mínimo de la columna i de matriz < el mínimo de la columna i + 1 de matriz }
#}

def minimo(s: list[int]) -> int:
    menor: int = s[0]
    for i in s:
        if i < menor:
            menor = i
    return menor

def crear_columnas(matriz: list[list[int]]) -> list[list[int]]:
    res: list[list[int]] = []
    indice: int = 0
    while indice < len(matriz[0]):
        columna = []
        for i in range(0,len(matriz)):
            elem = matriz[i][indice]
            columna.append(elem)
        indice += 1
        res.append(columna)
    return res

def matriz_pseudo_ordenada(matriz: list[list[int]]) -> bool:
    lista_minimos: list[int] = []
    columnas = crear_columnas(matriz)
    for c in columnas:
        lista_minimos.append(minimo(c))
    
    res: bool = True
    for i in range(0,len(lista_minimos)-1):
        if not (lista_minimos[i] < lista_minimos[i+1]):
            res = False
    return res

m1 = [[1, 3, 5, 5],
      [2, 1, 6, 7],
      [0, 2, 4, 8]]
print(matriz_pseudo_ordenada(m1))
m2 = [[0, 3, 5],
      [2, 2, 6],
      [0, 4, 4],
      [3, 5, 2]]
print(matriz_pseudo_ordenada(m2))
m4 = [[5, 6, 8, 10]]
print(matriz_pseudo_ordenada(m4))
m5 = [[1],
      [2],
      [6],
      [3]]
print(matriz_pseudo_ordenada(m5))
m6 = [[1]]
print(matriz_pseudo_ordenada(m6))

###################################################################################################### PARCIAL DESAPROB
# Ejercicio 1
def maximo(s: list[int]) -> int:
    maximo: int = s[0]
    for n in s:
        if n > maximo:
            maximo = n
    return maximo

def sumatoria_hasta(s: list[int], n: int) -> int:
    sumatoria: int = 0
    for e in s:
        if not(e == n):
            sumatoria += e
        else:
            break
    return sumatoria

def subsecuencia_mas_larga(v: list[int]) -> tuple[int,int]:
    cantidad: int = 1
    lista_aux: list[int] = []
    res: tuple[int, int] = []
    for i in range(len(v)-1):
        if v[i] == (v[i + 1] - 1) or v[i] == (v[i + 1] + 1):
            cantidad += 1
        else:
            lista_aux.append(cantidad)
            cantidad = 1
    for n in lista_aux:
        if n == maximo(lista_aux):
            res = [n, sumatoria_hasta(lista_aux,n)]
    return res

print(subsecuencia_mas_larga([-10, 2,1,2,1, 1,2,1,2]))

# Ejercicio 2
def mejor_resultado_por_examen(examen: list[bool]) -> int:
    contador_true: int = 0
    contador_false: int = 0
    for punto in examen:
        if punto == True:
            contador_true += 1
        else:
            contador_false += 1
    res: int = 0
    if contador_true == contador_false:
        res = len(examen)
    elif contador_true < contador_false:
        res = int(len(examen)/2) + contador_true
    else:
        res = int(len(examen)/2) + contador_false
    return res

def mejor_resultado_de_ana(examenes: Cola[list[bool]]) -> list[int]:
    res: list[int] = []
    contenedor: Cola = Cola()
    while not examenes.empty():
        examenActual = examenes.get()
        res.append(mejor_resultado_por_examen(examenActual))
        contenedor.put(examenActual)
    while not contenedor.empty():
        examenes.put(contenedor.get())
    return res

# Ejercicio 3
def cambiar_matriz(A: list[list[int]]) -> None:
    maximo_elemento: int = len(A) * len(A[0])
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = (A[i][j] % maximo_elemento) + 1

matriz = [[3,4,1],[2,5,0],[7,6,9]]
cambiar_matriz(matriz)
print(matriz)

# Ejercicio 4
def pertenece(s:list, n) -> bool:
    for i in s:
        if i == n:
            return True
    return False

def cantidad_vocales_por_palabra(palabra: str) -> int:
    vocales: list[str] = ['a','e','i','o','u','A','E','I','O','U']
    contador: int = 0
    for letra in palabra:
        if pertenece(vocales,letra):
            contador += 1
    return contador

def separar_texto_por_palabra(texto: str) -> list[str]:
    texto_aux: str = texto + ' '
    palabra: str = ''
    texto_separado: list[str] = []
    for letra in texto_aux:
        if letra != ' ':
            palabra += letra
        else:
            texto_separado.append(palabra)
            palabra = ''
    return texto_separado

def palabras_por_vocales(texto: str) -> dict[int, int]:
    res: dict[int, int] = {}
    palabras = separar_texto_por_palabra(texto)
    for palabra in palabras:
        clave = cantidad_vocales_por_palabra(palabra)
        if clave in res:
            res[clave] += 1
        else:
            res[clave] = 1
    return res

print(palabras_por_vocales("hola como estas hoy"))

