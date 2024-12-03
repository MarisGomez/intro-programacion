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
def minimo(s: list[int]) -> int:
    menor: int = s[0]
    for n in s:
        if n < menor:
            menor = n
    return menor

def maximo(s:list[int]) -> int:
    mayor: int = s[0]
    for n in s:
        if n > mayor:
            mayor = n
    return mayor

#def stock_productos(stock_cambios: list[(str, int)]) -> dict[str,(int, int)]:

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