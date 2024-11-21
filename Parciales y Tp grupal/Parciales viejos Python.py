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
#Guido y Marcela son dos estudiantes de IP, nervioses con el parcial de Python. 
#Con el objetivo de tener un rato antes del parcial para preguntarse algunas dudas 
#deciden encontrarse en el colectivo y viajar juntes. 
#Para poder coordinar de forma exacta en qué colectivo se tienen que subir, 
#Marcela usa sus habilidades de programación aprendidas en IP para acceder de forma 
#poco legítima a la base de datos de colectivos de todas las empresas. 
#Con esto, arma una lista de todos los colectivos que van a pasar por la parada de
#Guido alrededor del horario acordado y le indica a Guido que se tiene que subir en 
#el 3er colectivo de la línea 34. Por desgracia, Guido se olvida sus lentes antes 
#de salir y no es capaz de distinguir a qué línea pertenece cada colectivo que 
#llega a la parada. Por lo que solo puede contar cantidad total de colectivos que 
#pasan.
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

def ind_nesima_aparicion(s: list, n: int, elem: int) -> int:
    res: int = 0
    for i in range (0, len(s)):
        