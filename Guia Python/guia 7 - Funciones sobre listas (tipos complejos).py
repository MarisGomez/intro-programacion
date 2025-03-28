# EJERCICIO 1.1
def pertenece (lista:list[int], i:int) -> bool:
    for n in lista:
        if i == n:
            return True
    return False

def pertenece2 (lista:list[int], i:int) -> bool:
    n: int = 0
    while n < len(lista):
        if lista[n] == i:
            return True
        n += 1
    return False

def pertenece3 (lista:list[int], i:int) -> bool:
    for n in range (0,len(lista),1):
        if lista[n] == 1:
            return True
    return False

def pertenece_aux (lista:list[int], i:int) -> bool:
    return i in lista

# EJERCICIO 1.2
def divide_a_todos (lista:list[int], n:int) -> bool:
    res:bool = False
    for e in lista:
        if n % e == 0:
            res = True
    return res

# EJERCICIO 1.3
def suma_total (lista:list[int]) -> int:
    res:int = 0
    for n in lista:
        res += n
    return res 

# EJERCICIO 1.4
def maximo (lista:list[int]) -> int:
    res:int = lista[0]
    for e in lista:
        if e > res:
            res = e
    return res

# EJERCICIO 1.5
def minimo (lista:list[int]) -> int:
    res:int = lista[0]
    for e in lista:
        if e < res:
            res = e
    return res

# EJERCICIO 1.6
def ordenar (lista:list[int]) -> bool: #DEVUELVE LA LISTA ORDENADA PERO NO ES LO PEDIDO
    lista_desordenada: list[int] = lista.copy()
    lista_ordenada: list[int] = []
    while lista_ordenada < lista_desordenada:
        lista_ordenada.append(minimo(lista_desordenada))
        lista_desordenada.remove(minimo(lista_desordenada)) # REMOVE NO ESTA ADMITIDO
    return lista_ordenada

def ordenados(Lista:list[int]) -> bool:
    for i in range(len(Lista)-1):
        if (not(Lista[i]<Lista[i+1])):
            return False
    return True

# EJERCICIO 1.7
def pos_maximo(lista:list[int]) -> int:
    if lista == []:
        return -1
    else:
        for i in range (len(lista)):
            if lista[i] == maximo(lista):
                return i
        
# EJERCICIO 1.8
def pos_minimo(lista:list[int]) -> int:
    if lista == []:
        return -1
    else:
        for i in range (len(lista)):
            if lista[i] == minimo(lista):
                return i

# EJERCICIO 1.9
def palabra_larga(palabras:list[str]) -> bool:
    for i in range (len(palabras)):
        if len(palabras[i]) > 7:
            return True
    return False

# EJERCICIO 1.10
def polindromo(palabra:str) -> bool:
    if len(palabra) == 0 or len(palabra) == 1:
        return True
    else:
        indice:int = 0
        while indice < len(palabra):
            if palabra[indice] != palabra[len(palabra) - 1 - indice]:
                return False
            indice += 1
        return True

# EJERCICIO 1.11
def consecutivos(numero:list[int]) -> bool:
    indice:int = 0
    indice2:int = 1
    contador_consecutivos:int = 0
    while indice2 < len(numero):
        if numero[indice] == numero[indice2]:
            contador_consecutivos += 1
            if contador_consecutivos == 2:
                return True
            indice += 1
            indice2 += 1
        else:
            contador_consecutivos = 0
            indice += 1
            indice2 += 1
    return False

# EJERCICIO 1.12
def pertenece_str (lista:list[str], i:str) -> bool:
    return i in lista

def vocales_distintas(palabra:str) -> bool:
    vocales:list[str] = ['a','e','i','o','u']
    vocales_palabra:list[str] = []
    for i in range(0,len(palabra)):
        if pertenece_str(vocales, palabra[i]) and not(pertenece_str(vocales_palabra, palabra[i])):
            vocales_palabra.append(palabra[i])
        
    if len(vocales_palabra) == 3:
        return True
    else:
        return False

# EJERCICIO 1.13
def sec_ordenada(s: list[int]) -> int:
    cantidad: int = 0
    indice: int
    cantidad_mayor: int = 0
    indice_mayor: int
    for i in range(len(s)):
        if i + 1 < len(s) and s[i] + 1 == s[i + 1]:
            if cantidad == 0:
                indice = i
            cantidad += 1
            if cantidad > cantidad_mayor:
                cantidad_mayor = cantidad
                indice_mayor = indice
        else:
            cantidad = 0
    return indice_mayor

print(sec_ordenada([1,2,3,0,1,2,3,4,0,1,2,3]))
print(sec_ordenada([0,1,2,0,10,11,12,13]))
print(sec_ordenada([0,1,2,3,0,1,2,3,0,1,2,3]))

# EJERCICIO 14
def cant_digitos_impares(s: list[int]) -> int:
    contador_impares: int = 0
    for numero in s:
        numero = str(numero) # cambio la variable del numero de int a str
        indice = 0
        while indice < len(numero):
            digito = int(numero[indice]) # para poder operar con el numero lo vuelvo int
            if digito % 2 != 0:
                contador_impares += 1
            indice += 1
    return contador_impares

print(cant_digitos_impares([57, 2383, 812, 246]))
print(cant_digitos_impares([22,46,88,26]))
print(cant_digitos_impares([22,46,88,26,77,54]))

#########################################################################################################
# EJERCICIO 2.1
def ceros_en_posiciones_pares (lista:list[int]):
    for n in range (0,len(lista),2):
        lista[n] = 0

#lista: list[int] = [1,2,3,4]
#ceros_en_posiciones_pares(lista)
#print(lista)

# EJERCICIO 2.2
def ceros_en_posiciones_pares2 (lista:list[int]) -> list[int]:
    res: list[int] = []
    i:int = 0
    while i < len(lista):
        if i % 2 == 0:
            res.append(0)
        else:
            res.append(lista[i])
        i += 1
    return res

# EJERCICIO 2.3
def sin_vocales(palabra:str) -> str:
    vocales:list[str] = ['a','e','i','o','u','A','E','I','O','U']
    palabra_nueva:str = ""
    for i in range(0,len(palabra)):
        if not(pertenece(vocales, palabra[i])):
            palabra_nueva += palabra[i] 
    return palabra_nueva


# EJERCICIO 2.4
def reemplaza_vocales(palabra:str) -> str:
    vocales:list[str] = ['a','e','i','o','u','A','E','I','O','U']
    palabra_nueva:str = ""
    for i in range(0,len(palabra)):
        if not(pertenece(vocales, palabra[i])):
            palabra_nueva += palabra[i]
        else:
            palabra_nueva += ' '
    return palabra_nueva

# EJERCICIO 2.5
def da_vuelta_str(palabra:str) -> str:
    palabra_nueva:str = ""
    for i in range(0,len(palabra)):
        palabra_nueva += palabra[len(palabra) - 1 - i]
    return palabra_nueva

# EJERCICIO 2.6
def eliminar_repetidos(palabra:str) -> str:
    palabra_nueva:str = ""
    for i in range(0,len(palabra)):
        if pertenece(palabra, palabra[i]) and not(pertenece(palabra_nueva,palabra[i])):
            palabra_nueva += palabra[i]
    return palabra_nueva

# EJERCICIO 3
def resultado_materia(notas:list[int]) -> int:
    contador_notas:int = 0
    for nota in notas:
        if nota >= 4:
            contador_notas += nota
        if nota < 4:
            return 3
    
    promedio = contador_notas/len(notas)

    if promedio >= 7:
        return 1
    else:
        return 2

# EJERCICIO 4
def saldo_bancario(movimientos:list[tuple[str,int]]) -> int:
    saldo:int = 0
    for movimiento in movimientos:
        if movimiento[0] == "I":
            saldo += movimiento[1]
        else:
            saldo -= movimiento[1]
    return saldo

#########################################################################################################
# EJERCICIO 5
def pertenece_a_cada_uno_version_1(s: list[int], e: int, res: list[bool]) -> None:
    res.clear()
    for i in range(len(s)):
        res.append(pertenece(s[i], e))

#print(pertenece_a_cada_uno_version_1([[4,5,6], [7,8,10], [4,4,4]], 4, [True, False, True])) #PREGUNTAR

def pertenece_a_cada_uno_version_3(s: list[int], e: int) -> list[bool]:
    res:list[bool] = []
    for i in range(len(s)):
        res.append(pertenece(s[i], e))
    return res


# EJERCICIO 6.1
def es_matriz(matriz:list[list[int]]) -> bool:
    if len(matriz) == 0 or len(matriz[0]) == 0:
        return False
    else:
        indice:int = 0
        while indice < len(matriz):
            if len(matriz[0]) != len(matriz[indice]):
                return False
            else:
                indice += 1
        return True

# EJERCICIO 6.2
def filas_ordenadas(matriz:list[list[int]], res:list[bool]) -> None:
    res.clear()
    indice = 0
    while indice < len(matriz):
        res.append(ordenados(matriz[indice]))
        indice += 1

#matriz = [[1,2,3],[4,5,6],[7,8,9],[1,2,3]]
#res = [False,False,False]
#filas_ordenadas(matriz, res)
#print(matriz, res)

# EJERCICIO 6.3
def columna(matriz:list[list[int]], c:int) -> list[int]:
    res:list[int] = []
    for fila in matriz:
        res.append(fila[c])
    return res


matriz = [[1,2,3],
          [4,5,6],
          [12,8,9]]
print(columna(matriz, 0)) # [1,4,12]
print(columna(matriz, 2)) # [3,6,9]

# EJERCICIO 6.4
def columnas_ordenadas(matriz:list[list[int]]) -> list[bool]:
    res:list[bool] = []
    indice = 0
    while indice < len(matriz):
        res.append(ordenados(columna(matriz,indice)))
        indice += 1
    return res

# EJERCICIO 6.5
def transponer(matriz:list[list[int]]) -> list[list[int]]:
    res:list[list[int]] = []
    indice:int = 0
    while indice < len(matriz):
        res.append(columna(matriz,indice))
        indice += 1
    return res

# EJERCICIO TATETI


if __name__ == '__main__':
    #print(pertenece([1,2,3,4],5))
    #print(pertenece2([1,2,3,4],2))
    #print(pertenece3([1,2,3,4],7))
    #print(suma_total([1,2,3,4,5]))
    #print(suma_total([]))
    #print(ceros_en_posiciones_pares2([1,2,3,4,5,6]))
    #print(divide_a_todos([2,4,8],2))
    #print(maximo([3,5,1,4]))
    #print(minimo([99,34,5,72]))
    #print(ordenados([1,3,5,1]))
    #print(ordenados2([1,3,5,6]))
    #print(maximo([-3,-2,-1]))
    #print(pos_maximo([-3,-2,-1]))
    #print(pos_minimo([1,4,5,-6]))
    #print(palabra_larga(["termo","gato","tener","sociologia"]))
    #print(polindromo("a"))
    #print(polindromo("anana"))
    #print(consecutivos([4,1,3,1,1,4]))
    #print(vocales_distintas("ana"))
    #print(sin_vocales("anastasia"))
    #print(reemplaza_vocales("anastasia"))
    #print(da_vuelta_str("argentina"))
    #print(eliminar_repetidos("pepinillo"))
    #print(sumatoria([4,4,1]))
    #print(resultado_materia([4,5,8,1]))
    #print(saldo_bancario([("I",2000), ("R", 20),("R", 1000),("I", 300)]))
    #print(pertenece_a_cada_uno_version_3([[4,5,6], [7,8,10], [4,4,4]], 4))
    print(es_matriz([[]]))
    print(columnas_ordenadas([[1,2,7],[4,5,6],[12,8,9]]))
    print(transponer([[1,2,7],[4,5,6],[12,8,9]]))
