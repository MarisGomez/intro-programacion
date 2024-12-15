def generarColumnas (m: list[list[int]]) -> list[list[int]]:
    columnas: list[list[int]] = []
    indice: int = 0
    while indice < len(m[0]):
        columna = []
        for i in range(0,len(m)):
            elem = m[i][indice]
            columna.append(elem)
        indice += 1
        columnas.append(columna)
    return columnas

def es_lista_valida(fila: list[int]) -> bool:
    apariciones: list[int] = []

    for numero in fila:
        if 1 <= numero <= 9:
            if numero not in apariciones:
                apariciones.append(numero)
            else:
                return False
    return True

def esSudokuValido (m: list[list[int]]) -> bool:
    filasyColumnas: list[list[int]] = m + generarColumnas(m)
    res: bool
    for i in filasyColumnas:
        if es_lista_valida(i):
            res = True
        else:
            return False
    return res

m1 = [
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[9, 8, 7, 6, 4, 5, 3, 2, 1],
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 4, 0, 0, 0],
[0, 0, 0, 0, 6, 0, 0, 0, 0],
[0, 0, 0, 5, 0, 0, 0, 0, 0],
[0, 0, 4, 0, 0, 0, 0, 0, 0],
[0, 3, 0, 0, 0, 0, 0, 0, 0],
[2, 0, 0, 0, 0, 0, 0, 0, 0]
]
print(esSudokuValido(m1)) # True

m2 = [
[1, 2, 3, 4, 5, 6, 1, 8, 9],
[9, 8, 7, 6, 4, 5, 3, 2, 1],
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 4, 0, 0, 0],
[0, 0, 0, 0, 6, 0, 0, 0, 0],
[0, 0, 0, 5, 0, 0, 0, 0, 0],
[0, 0, 4, 0, 0, 0, 0, 0, 0],
[0, 3, 0, 0, 0, 0, 0, 0, 0],
[2, 0, 0, 0, 0, 0, 0, 0, 0]
]
print(esSudokuValido(m2)) # False
m3 = [
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[9, 8, 7, 6, 4, 5, 3, 2, 1],
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 4, 0, 0, 0],
[0, 0, 0, 0, 6, 5, 0, 0, 0],
[0, 0, 0, 5, 0, 0, 0, 0, 0],
[0, 0, 4, 0, 0, 0, 0, 0, 0],
[0, 3, 0, 0, 0, 0, 0, 0, 0],
[2, 0, 0, 0, 0, 0, 0, 0, 0]
]
print(esSudokuValido(m3)) # False

#####################################################################################################
def esPrimo(n: int) -> bool:
    divisores: list[int] = []
    indice: int = 1
    while indice <= n:
        if n % indice == 0:
            divisores.append(indice)
            indice += 1
        else:
            indice += 1
    if len(divisores) == 2:
        return True
    else:
        return False

def cantidadApariciones(s: list[int], n: int) -> int:
    contador: int = 0
    for i in s:
        if i == n:
            contador += 1
    return contador

def primerPrimo(s: list[int]) -> int:
    for n in s:
        if esPrimo(n):
            return n

def primoMasFrecuente(s: list[int]) -> int:
    res: int = primerPrimo(s)
    for n in s:
        if esPrimo(n) and cantidadApariciones(s,n) > cantidadApariciones(s,res):
            res = n
    return res

print(primoMasFrecuente([2,3,4,3,3,4,4,4,1]))