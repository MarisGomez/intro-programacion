# Ejercicio 1
#
#  problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
#    requiere: {e pertenece a s }
#    asegura: {res es la posición de la última aparición de e en s}
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,100,0,100,0,-1,-1]
#   e = 0
# se debería devolver res=7

def ultima_aparicion(s: list, e: int) -> int:
    indice:int = 0
    for i in range (0,len(s)):
        if e == s[len(s) -1 -indice]:
            return len(s) -1 -indice
        indice += 1

print(ultima_aparicion([-1,4,0,4,100,0,100,0,-1,-1],0))

# Ejercicio 2
#
#  problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
#    requiere: -
#    asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
#    asegura: {res no tiene elementos repetidos }
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,3,0,100,0,-1,-1]
#   t = [0,100,5,0,100,-1,5]
# se debería devolver res = [3,4,5] ó res = [3,5,4] ó res = [4,3,5] ó res = [4,5,3] 
# ó res = [5,3,4] ó res = [5,4,3]

#def pertenece (s: list[int], i: int) -> bool:
#    for n in s:
#        if i == n:
#            return True
#    return False

def eliminar_repetidos(s: list[int]) -> list[int]: 
    lista_nueva:list[int] = []
    for i in range(0,len(s)):
        if pertenece(s, s[i]) and not (pertenece(lista_nueva,s[i])):
            lista_nueva.append(s[i])
    return lista_nueva

def elementos_exclusivos(s: list[int], t: list[int]) -> list[int]:
    indice_s: int = 0
    indice_t: int = 0
    res: list[int] = []
    for i in range (0,len(s)):
        if not pertenece (t,s[indice_s]):
            res.append(s[indice_s])
        indice_s += 1
    for j in range (0,len(t)):
        if not pertenece(s,t[indice_t]):
            res.append(t[indice_t])
        indice_t += 1
    return eliminar_repetidos(res)

#print(elementos_exclusivos([-1,4,0,4,3,0,100,0,-1,-1],[0,100,5,0,100,-1,5]))

# OTRA FORMA
def pertenece(n, l: list) -> bool:
    pertenece = False
    for e in l:
        if n == e:
            pertenece = True
    return pertenece

def pertenece_a_ambas(e:int, l1:list, l2:list) -> bool:
    return pertenece(e,l1) and pertenece(e,l2)

def elementos_exclusivos2(s: list, t: list) -> list:
    res:list = []
    syt:list = s + t 
    for e in syt:
        if not pertenece_a_ambas(e,s,t):
            if not pertenece(e,res):
                res.append(e)
    return res

print(elementos_exclusivos2([-1,4,0,4,3,0,100,0,-1,-1],[0,100,5,0,100,-1,5]))

# Ejercicio 3
#
# Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
# en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
# en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
# palabras que tienen la misma traducción en inglés y en alemán.

#  problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
#    requiere: -
#    asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
#  }

#  Por ejemplo, dados los diccionarios
#    aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
#    inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
#  se debería devolver res=2

def contar_traducciones_iguales(ing: dict[str,str], ale: dict[str,str]) -> int:
    res:int = 0
    for traduccion in ing.items():
        if pertenece(traduccion, ale.items()):
            res += 1
    return res

aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
ingles = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
print(contar_traducciones_iguales(ingles, aleman))

# OTRA FORMA
def contar_traducciones_iguales2(ingles: dict, aleman: dict) -> int:
    res:int = 0
    for palabra in ingles.keys():
        if pertenece(palabra,aleman.keys()) and ingles[palabra] == aleman[palabra]:
            res += 1
    return res

# Ejercicio 4
#
# Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s, 
# y sus valores la cantidad de veces que cada uno de esos números aparece en s

#  problema convertir_a_diccionario (lista: seq⟨Z⟩) : dicc⟨Z,Z⟩) {
#    requiere: -
#    asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
#  }

#  Por ejemplo, dada la lista
#  lista = [-1,0,4,100,100,-1,-1]
#  se debería devolver res={-1:3, 0:1, 4:1, 100:2}
#  
# RECORDAR QUE NO IMPORTA EL ORDEN DE LAS CLAVES EN UN DICCIONARIO

def conventir_a_diccionario(s: list[int]) -> dict[int, int]:
    diccionario: dict[int, int] = {}
    for n in s:
        clave: int = n
        if clave in diccionario:
            diccionario[clave] += 1
        else:
            diccionario[clave] = 1
    return diccionario

print(conventir_a_diccionario([-1,0,4,100,100,-1,-1]))

######################################################################################################

#1) Índice de la n-ésima aparición [2 puntos]
#Implementar la función ind_nesima_aparicion que dada una secuencia de enteros s, 
#y dos enteros n y elem devuelve la posición en la cual elem aparece por n-ésima vez 
#en s. En caso de que elem aparezca menos de n veces en s, devolver -1.

#problema ind_nesima_aparicion (in s: seq⟨Z⟩, in n: Z, in elem: Z) : Z {
#  requiere: {n>0}
#  asegura: {Si el elemento aparece menos de n veces en la secuencia, res= -1 }
#  asegura: {Si el elemento aparece al menos n veces en la secuencia, s[res] = elem }
#  asegura: {Si el elemento aparece al menos n veces en la secuencia, elem aparece n-1 
#  veces en s entre las posiciones 0 y res-1 }
#}
#Por ejemplo, dadas
#s = [-1, 1, 1, 5, -7, 1, 3]
#n = 2
#elem = 1
#se debería devolver res = 2

def cantidad_apariciones(s: list, n: int) -> int:
    res: int = 0
    for i in s:
        if i == n:
            res += 1
    return res

def ind_nesima_aparicion(s: list[int], n: int, elem: int) -> int:
    indice: int = 0
    contador: int = 0
    res: int = -1

    if cantidad_apariciones(s,elem) >= n:
        while contador < n:
                if s[indice] == elem:
                     contador = contador + 1
                indice = indice + 1
                res = res + 1
    return res

print(ind_nesima_aparicion([-1, 1, 1, 5, -7, 1, 3],2,1))
print(ind_nesima_aparicion([-1,0,4,100,100,-1,-1],2,100))
print(ind_nesima_aparicion([-1,4,0,4,3,0,100,0,-1,-1],3,4))

#2) Mezclar [2 puntos]
#Implementar la función mezclar que dadas dos listas 
#s1 y s2 con igual cantidad de elementos devuelva una lista con los elementos 
#intercalados. Esto es, las posiciones pares de res tendrán los elementos de s1 
#y las posiciones impares los elementos de s2, respetando el orden original.

#problema mezclar (in s1: seq⟨Z⟩, in s2: seq⟨Z⟩) : seq⟨Z⟩ {
#  requiere: {|s1| = |s2| }
#  asegura: {|res| = 2 * |s1|}
#  asegura: {res[2*i] = s1[i] y res[2*i+1] = s2[i], para i entre 0 y |s1|-1}
#}
#TIP: realizar la iteración mediante índices y no mediante elementos

#Por ejemplo, dadas
#s1 = [1, 3, 0, 1]
#s2 = [4, 0, 2, 3]
#se debería devolver res = [1, 4, 3, 0, 0, 2, 1, 3]

def mezclar(s1: list[int], s2: list[int]) -> list[int]:
    lista_nueva: list[int] = []
    indice:int = 0
    indice1:int = 0
    indice2:int = 0
    while indice < len(s1 + s2):
        if indice % 2 == 0:
            lista_nueva.append(s1[indice1])
            indice1 += 1
            indice += 1
        else:
            lista_nueva.append(s2[indice2])
            indice2 += 1
            indice += 1
    return lista_nueva

print(mezclar([1, 3, 0, 1],[4, 0, 2, 3]))

#3) A los pingos: resultado carreras [3 puntos]
#Implementar la función frecuencia_posiciones_por_caballo que dada la lista de 
#caballos que corrieron las carreras, y el diccionario que tiene los resultados del 
#hipódromo en el formato carreras:posiciones_caballos, donde carreras es un String 
#y posiciones_caballos es una lista de strings con los nombres de los caballos, 
#genere un diccionario de caballos:#posiciones, que para cada caballo devuelva la 
#lista de cuántas veces salió en esa posición.

#Tip: para crear una lista con tantos ceros como caballos se puede utilizar la siguiente 
#sintaxis lista_ceros = [0]*len(caballos)

#problema frecuencia_posiciones_por_caballo(in caballos: seq⟨String⟩, in carreras: 
#dict⟨String,seq⟨String⟩⟩: dict⟨String,seq⟨Z⟩⟩ {
#  requiere: {caballos no tiene repetidos}
#  requiere: {Los valores del diccionario carreras son permutaciones de la lista 
#  caballos (es decir, tienen exactamente los mismos elementos que caballos, en 
#  cualquier orden posible)}
#  asegura: {res tiene como claves los elementos de caballos}
#  asegura: {El valor en res de un caballo es una lista que indica en la posición i 
#  cuántas veces salió ese caballo en la i-ésima posición.}
#}
#Por ejemplo, dados
#caballos= ["linda", "petisa", "mister", "luck" ]
#carreras= {"carrera1":["linda", "petisa", "mister", "luck"],
#           "carrera2":["petisa", "mister", "linda", "luck"]}
#se debería devolver res = {"petisa": [1,1,0,0],
#                           "mister": [0,1,1,0],
#                            "linda": [1,0,1,0],
#                             "luck": [0,0,0,2]}

def posicion(caballo: str, carrera:list) -> int:
    indice: int = 0
    for c in carrera:
        if c == caballo:
            return indice
        indice += 1

def posiciones(caballo: str, carreras: dict) -> [int]:
    lista_carreras: list = []

    for carrera in carreras.keys():
        lista_carreras.append(carreras[carrera])

    primera_carrera: list = lista_carreras[0]
    caballos: int = len(primera_carrera)
    res: list = [0] * caballos

    for lista in lista_carreras:
        res[posicion(caballo,lista)] += 1
    return res

def frecuencia_posiciones_por_caballo(caballos: list, carreras: dict) -> dict:
    res: dict = {}
    for caballo in caballos:
        res[caballo] = posiciones(caballo, carreras)
    return res

caballos= ["linda", "petisa", "mister", "luck" ]
carreras= {"carrera1":["linda", "petisa", "mister", "luck"], "carrera2":["petisa", "mister", "linda", "luck"]}
print(frecuencia_posiciones_por_caballo(caballos, carreras))

#4) Matriz capicúa [3 puntos]
#Implementar la función matriz_capicua que dada una matriz devuelve True si 
#cada una de sus filas es capicúa. Es decir, si cada fila es igual leída de 
#izquierda a derecha o de derecha a izquierda. Definimos a una secuencia de
#secuencias como matriz si todos los elemento de la primera secuencia tienen 
#la misma longitud.

#problema matriz_capicua(in m:seq⟨seq⟨Z⟩⟩ ) : Bool {
#  requiere: {todos los elementos de m tienen igual longitud (los elementos de m son secuencias)}
#  asegura: {(res = true) <=> todos los elementos de m son capicúa}
#}

#Por ejemplo, dada la matriz
#m = [[1,2,2,1],[-5,6,6,-5],[0,1,1,0]]
#se debería devolver res = true

def capicua(s: list[int]) -> bool:
    if len(s) == 0 or len(s) == 1:
        return True
    else:
        indice:int = 0
        while indice < len(s):
            if s[indice] != s[len(s) - 1 - indice]:
                return False
            indice += 1
        return True
    
def matriz_capicua(m: list[list[int]]) -> bool:
    res: bool = True
    for s in m:
        if not capicua(s):
            res = False
    return res

print(matriz_capicua([[1,2,2,1],[-5,6,6,-5],[0,1,1,0]]))

######################################################################################################