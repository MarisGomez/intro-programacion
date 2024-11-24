from queue import LifoQueue as Pila
from queue import Queue as Cola
c = Cola
p = Pila
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

def posiciones(caballo: str, carreras: dict) -> list[int]:
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
#1) Alerta Enfermedades Infecciosas (3 puntos)
#Necesitamos detectar la aparición de posibles epidemias. Para esto contamos con un lista de enfermedades infecciosas y los registros de atención por guardia dados por una lista expedientes. 
#Cada expediente es una tupla con ID paciente y enfermedad que motivó la atención. Debemos devolver un diccionario cuya clave son las enfermedades infecciosas y su valor es la proporción de pacientes que se atendieron por esa enfermedad. 
#En este diccionario deben aparecer solo aquellas enfermedades infecciosas cuya proporción supere cierto umbral.

#problema alarma_epidemiologica (registros: seq⟨ZxString⟩, infecciosas: seq⟨String⟩, umbral: R) : dict⟨String,R⟩ {
#  requiere: {0 < umbral < 1}
#  asegura: {claves de res pertenecen a infecciosas}
#  asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa enfermedad sobre el total de registros es mayor o igual al umbral, entonces res[enfermedad] = porcentaje}
#  asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de e pacientes que se atendieron por esa enfermedad sobre el total de registros es menor que el umbral, entonces enfermedad no aparece en res}
#}

def proporcion_infeccion(enfermedad: str, registros: list[tuple[int, str]]) -> float:
    pacientes_totales: int = len(registros)
    infectados_por_enfermedad: int = 0
    for expediente in registros:
        if expediente[1] == enfermedad:
            infectados_por_enfermedad += 1
    porcentaje: float = (infectados_por_enfermedad/pacientes_totales)
    return porcentaje

def alarma_epidemiologica(registros: list[tuple[int, str]], infecciosas: list[str], umbral: float) -> dict[str, float]:
    res: dict[str, float] = {}
    for enfermedad in infecciosas:
        if not pertenece(enfermedad, res):
            if proporcion_infeccion(enfermedad, registros) >= umbral:
                res[enfermedad] = proporcion_infeccion(enfermedad, registros)
    return res

registros = [["juan","viruela"],["lucas","covid"],["alex","gripe"],["laura","covid"],["pablo","covid"]]
infecciosas = ["viruela","covid","gripe"]
print(proporcion_infeccion("covid", registros))
print(alarma_epidemiologica(registros,infecciosas,0.5))

#2) Orden de atención (1 punto)
#Desde el Hospital Fernandez nos pidieron solucionar una serie de problemas relacionados con la información que maneja sobre los pacientes y el personal de salud. 
#En primer lugar debemos resolver en qué orden se deben atender los pacientes que llegan a la guardia. 
#En enfermería, hay una primera instancia que clasifica en dos colas a los pacientes: una urgente y otra postergable (esto se llama hacer triage). 
#A partir de dichas colas que contienen la identificación del paciente, se pide devolver una nueva cola según la siguiente especificación.

#problema orden_de_atencion ( in urgentes: cola⟨Z⟩, in postergables: cola⟨Z⟩) : cola⟨Z⟩ {
#  requiere: {no hay elementos repetidos en urgentes}
#  requiere: {no hay elementos repetidos en postergables}
#  requiere: {la intersección entre postergables y urgentes es vacía}
#  requiere: {|postergables| = |urgentes|}
#  asegura: {no hay repetidos en res }
#  asegura: {res es permutación de la concatenación de urgentes y postergables}
#  asegura: {Si urgentes no es vacía, en tope de res hay un elemento de urgentes}
#  asegura: {En res no hay dos seguidos de urgentes}
#  asegura: {En res no hay dos seguidos de postergables}
#  asegura: {Para todo c1 y c2 de tipo "urgente" pertenecientes a urgentes si c1 aparece antes que c2 en urgentes entonces c1 aparece antes que c2 en res}
#  asegura: {Para todo c1 y c2 de tipo "postergable" pertenecientes a postergables si c1 aparece antes que c2 en postergables entonces c1 aparece antes que c2 en res}

def orden_de_atencion(urgentes:Cola[int], postergables:Cola[int]) -> Cola[int]:
    orden_final: Cola = Cola()
    contenedor_urg: Cola = Cola()
    contenedor_pos: Cola = Cola()
    while not urgentes.empty() and not postergables.empty():
        orden_final.put(urgentes.get())
        orden_final.put(postergables.get())
        contenedor_urg.put(urgentes.get())
        contenedor_pos.put(postergables.get())
    while not contenedor_urg.empty() and not contenedor_pos.empty():
        urgentes.put(contenedor_urg.get())
        postergables.put(contenedor_pos.get())
    return orden_final

#3) Camas ocupadas en el hospital (2 puntos)
#Queremos saber qué porcentaje de ocupación de camas hay en el hospital. El hospital se representa por una matriz en donde las filas son los pisos, y las columnas son las camas. 
#Los valores de la matriz son booleanos que indican si la cama está ocupada o no. Si el valor es verdadero (True) indica que la cama está ocupada. 
#Se nos pide programar en Python una función que devuelve una secuencia de enteros, indicando la proporción de camas ocupadas en cada piso.

#problema nivel_de_ocupacion(camas_por_piso:seq⟨seq⟨Bool⟩⟩) : seq⟨R⟩ {
#  requiere: {Todos los pisos tienen la misma cantidad de camas.}
#  requiere: {Hay por lo menos 1 piso en el hospital.}
#  requiere: {Hay por lo menos una cama por piso.}
#  asegura: {|res| = |camas|}
#  asegura: {Para todo 0<= i < |res| se cumple que res[i] es igual a la cantidad de camas ocupadas del piso i dividido el total de camas del piso i)}
#}

def proporcion_ocupacion_fila(camas_por_piso: list[bool]) -> float:
    camas_ocupadas: int = 0
    camas_totales: int = len(camas_por_piso)
    for cama in range(0,len(camas_por_piso)):
        if camas_por_piso[cama] == True:
            camas_ocupadas += 1
    res = (camas_ocupadas/camas_totales) 
    return res

def nivel_de_ocupacion(camas_por_piso: list[list[bool]]) -> list[float]:
    res: list[float] = []
    for piso in camas_por_piso:
        res.append(proporcion_ocupacion_fila(piso))
    return res

print(nivel_de_ocupacion([[True,False,False,False],[True,False,False,True],[False,False,False,False]]))

# OTRA FORMA
def nivel_de_ocupacion2(camas_por_piso:list[list[bool]]) -> list[float]:
    res : list[float] = []
    contador : int = 0
    cantidad_camas = len(camas_por_piso)
    for fila in range(0,len(camas_por_piso)) : 
        for elem in range(0,len(camas_por_piso)):
            if camas_por_piso[fila][elem] == True:
                contador += 1
        res.append(contador/cantidad_camas)
        contador = 0
    return res

#4) Quiénes trabajaron más? (2 puntos)
#Dado un diccionario con la cantidad de horas trabajadas por empleado, en donde la clave es el ID del empleado y el valor es una lista de las horas trabajadas por día, 
#queremos saber quienes trabajaron más para darles un premio. Se deberá buscar la o las claves para la cual se tiene el máximo valor de cantidad total de horas, y devolverlas en una lista.

#problema empleados_del_mes(horas:dicc⟨Z,seq⟨Z⟩⟩) : seq⟨Z⟩ {
#  requiere: {No hay valores en horas que sean listas vacías}
#  asegura: {Si ID pertence a res entonces ID pertence a las claves de horas}
#  asegura: {Si ID pertenece a res, la suma de sus valores de horas es el máximo de la suma de elementos de horas de todos los otros IDs}
#  asegura: {Para todo ID de claves de horas, si la suma de sus valores es el máximo de la suma de elementos de horas de los otros IDs, entonces ID pertences a res}
#}

def sumatoria(s:list[int]) -> int:
    res: int = 0
    for n in s:
        res += n
    return res

def maximo (s:list[int])-> int : 
    mayor : int = 0
    for num in s : 
        if num > mayor:
            mayor = num
    return mayor

def pos_mayor(s:list[int]) -> list[int] : 
    mayor : int = maximo(s)
    res : list[int] = []
    for i in range(0,len(s)): 
        if s[i] == mayor: 
            res.append(i)
    return res

def empleados_del_mes(horas:dict[int, list[int]]) -> list[int]:
    lista_trabajadores: list[int] = []
    horas_por_trabajador: list[int] = []
    res: list[int] = []
    for ids in horas.keys():
        lista_trabajadores.append(ids)
        horas_por_trabajador.append(sumatoria(horas[ids]))
    mas_horas = pos_mayor(horas_por_trabajador)
    for i in range(0,len(mas_horas)):
        res.append(lista_trabajadores[mas_horas[i]])
    return res

horas = {111:[5,3,7],112:[9,8,8],113:[3,5,4],114:[2,5,1]}
print(empleados_del_mes(horas))

######################################################################################################
#1) Promedio de salidas [2 puntos]

#Dado un diccionario donde la clave es el nombre de cada amigo y el valor es una lista de los tiempos (en minutos) registrados para cada sala de escape en Capital,
#escribir una función en Python que devuelva un diccionario. En este nuevo diccionario, las claves deben ser los nombres de los amigos y los valores deben ser tuplas 
#que indiquen la cantidad de salas de las que cada persona logró salir y el promedio de los tiempos de salida (solo considerando las salas de las que lograron salir)

#problema promedio_de_salidas (in registro: dict⟨String, seq⟨Z⟩⟩) : dict⟨String, ⟨Z x R⟩⟩ {
#  requiere: {registro tiene por lo menos un integrante}
#  requiere: {Todos los integrantes de registro tiene por lo menos un tiempo}
#  requiere: {Todos los valores de registro tiene la misma longitud}
#  requiere: {Todos los tiempos de los valores de registro están entre 0 y 61 inclusive}
#  asegura: {res tiene las mismas claves que registro}
#  asegura: {El primer elemento de la tupla de res para un integrante, es la cantidad de salas con tiempo mayor estricto a 0 y menor estricto a 61 que figuran en sus valores de registro}
#  asegura: {El segundo elemento de la tupla de res para un integrante, si la cantidad de salas de las que salió es mayor a 0: es el promedio de salas con tiempo mayor estricto a 0 y menor estricto a 61 que figuran en sus valores de registro; sino es 0.0}
#}

def promedio_de_salidas(registro: dict[str, list[int]]) -> dict[str, tuple[int,float]]:
    res: dict[str, tuple[int,float]] = {}
    for amigo in registro.keys():
        sumatoria: int = 0
        salas_completadas: int = 0
        for tiempo in registro[amigo]:
            if 0 < tiempo < 61:
                sumatoria += tiempo
                salas_completadas += 1
        res[amigo] = [salas_completadas, sumatoria/salas_completadas]
    return res

registros = {"pepe":[10,60,20],"juan":[30,25,30],"laura":[60,15,0]}
print(promedio_de_salidas(registros))

#2) Tiempo más rápido [1 punto]

#Dada una lista con los tiempos (en minutos) registrados para cada sala de escape de Capital, 
#escribir una función en Python que devuelva la posición (índice) en la cual se encuentra el tiempo más rápido,
#excluyendo las salas en las que no haya salido (0 o mayor a 60).

#problema tiempo_mas_rapido (in tiempos_salas: seq⟨Z⟩): Z {
#  requiere: {Hay por lo menos un elemento en tiempos_salas entre 1 y 60 inclusive}
#  requiere: {Todos los tiempos en tiempos_salas están entre 0 y 61 inclusive}
#  asegura: {res es la posición de la sala en tiempos_salas de la que más rápido se salió (en caso que haya más de una, devolver la primera, osea la de menor índice)}
#}

def tiempo_mas_rapido (tiempos_salas: list[int])-> int:
    res:int = 0
    tiempoMasRapido:int = 61
    i:int = 0
    while i < len(tiempos_salas):
        if tiempos_salas[i] < tiempoMasRapido and tiempos_salas[i] > 0 and tiempos_salas[i] < 61:
            tiempoMasRapido = tiempos_salas[i]
            res = i
            i += 1
        else:
            i += 1
    return res

print(tiempo_mas_rapido([62,-3,5]))

#3) Racha más larga [3 puntos]

#Dada una lista con los tiempos (en minutos) registrados para cada sala de escape a la que fue una persona, 
#escribir una función en Python que devuelva una tupla con el índice de inicio y el índice de fin de la subsecuencia más larga de salidas exitosas de salas de escape consecutivas.

#problema racha_mas_larga (in tiempos: seq⟨Z⟩): ⟨Z x Z⟩ {
#  requiere: {Hay por lo menos un elemento en tiempos entre 1 y 60 inclusive}
#  requiere: {Todos los tiempos en tiempos están entre 0 y 61 inclusive}
#  asegura: {En la primera posición de res está la posición (índice de la lista) de la sala que inicia la racha más larga}
#  asegura: {En la segunda posición de res está la posición (índice de la lista) de la sala que finaliza la racha más larga}
#  asegura: {El elemento de la primer posición de res en tiempos es mayor estricto 0 y menor estricto que 61}
#  asegura: {El elemento de la segunda posición de res en tiempos es mayor estricto 0 y menor estricto que 61}
#  asegura: {La primera posición de res es menor o igual a la segunda posición de res }
#  asegura: {No hay valores iguales a 0 o a 61 en tiempos entre la primer posición de res y la segunda posición de res}
#  asegura: {No hay otra subsecuencia de salidas exitosas, en tiempos, de mayor longitud que la que está entre la primer posición de res y la segunda posición de res}
#  asegura: {Si hay dos o más subsecuencias de salidas exitosas de mayor longitud en tiempos, res debe contener la primera de ellas.}
#}

def racha_mas_larga(tiempos: list[int]) -> tuple[int, int]:
    pos_inicial: int = 0
    pos_final: int = 0
    res: tuple[int, int] = []
    i: int = 0
    while i < len(tiempos):
        if 0 < tiempos[i] < 61 and pos_inicial == 0:
            pos_inicial = i
        i += 1
    i2 = pos_inicial
    while i2 < len(tiempos):
        if 0 < tiempos[i2] < 61:
            pos_final = i2
        else:
            break
        i2 += 1
    res = [pos_inicial, pos_final]
    return res

print(racha_mas_larga([0,30,23,45,62,15]))

#4) Escape en solitario [2 puntos]

#Dada una matriz donde las columnas representan a cada amigo y las filas representan las salas de escape, 
#y los valores son los tiempos (en minutos) registrados para cada sala (0 si no fueron, 61 si no salieron, y un número entre 1 y 60 si salieron), 
#escribir una función en Python que devuelva los índices de todas las filas (que representan las salas) en las cuales el primer, 
#segundo y cuarto amigo no fueron (0), pero el tercero sí fue (independientemente de si salió o no).

#problema escape_en_solitario (in amigos_por_salas: seq⟨seq⟨Z⟩⟩): seq⟨Z⟩ {
#  requiere: {Hay por lo menos una sala en amigos_por_salas}
#  requiere: {Hay 4 amigos en amigos_por_salas}
#  requiere: {Todos los tiempos en cada sala de amigos_por_salas están entre 0 y 61 inclusive}
#  asegura: {La longitud de res es menor igual que la longitud de amigos_por_salas}
#  asegura: {Por cada sala en amigos_por_salas cuyo primer, segundo y cuarto valor sea 0, y el tercer valor sea distinto de 0, la posición de dicha sala en amigos_por_salas debe aparecer res}
#  asegura: {Para todo i pertenciente a res se cumple que el primer, segundo y cuarto valor de amigos_por_salas[i] es 0, y el tercer valor es distinto de 0}
#}

def espcape_en_solitario(amigos_por_salas: list[list[int]]) -> list[int]:
    res:list[int] = []
    cantSalas:int = len(amigos_por_salas)
    for i in range(cantSalas):
        sala = amigos_por_salas[i]
        if sala[0] == sala[1] == sala[3] == 0 and sala[2] > 0:
            res.append(i)
    return res

######################################################################################################
# 1) Acomodar [2 puntos]

# No está permitido utilizar las funciones sort() y reverse().

# problema acomodar (in s: seq<String>) : seq<String> {
#     requiere: { Todos los elementos de s son o bien "LLA" o bien "UP"}
#     asegura: {|res| = |s|}
#     asegura: { Todos los elementos de res son o bien "LLA" o bien "UP"}
#     asegura: {res contiene la misma cantidad de elementos "UP" que s}
#     asegura: {res contiene todas las apariciones de "UP" antes de las
#     apariciones de "LLA"}
# }
# Por ejemplo, dada
# s = ["LLA", "UP", "LLA", "LLA", "UP"]
# se debería devolver res = ["UP", "UP", "LLA", "LLA", "LLA"]

def acomodar(s: list[str]) -> list[str]:
    lista_up: list[str] = []
    lista_lla: list[str] = []
    lista_ordenada: list[str] = []
    for boleta in s:
        if boleta == "UP":
            lista_up.append(boleta)
        else:
            lista_lla.append(boleta)
    lista_ordenada += lista_up
    lista_ordenada += lista_lla
    return lista_ordenada

print(acomodar(["LLA", "LLA", "LLA", "UP", "UP", "LLA", "UP"]))

# 2) Posición umbral [2 puntos]

# Implementar la función pos_umbral, que dada una secuencia de enteros (puede
# haber negativos) devuelve la posición en la cual se supera el valor de umbral,
# teniendo en cuenta sólo los elementos positivos. Se debe devolver -1 si el
# umbral no se supera en ningún momento

# problema pos_umbral (in s: seq<Z>, in u: Z) : Z {
#     requiere: {u ≥ 0}
#     asegura: {res=-1 si el umbral no se supera en ningún momento }
#     asegura: {Si el umbral se supera en algún momento, res es la primera
#     posición tal que la sumatoria de los primeros res+1 elementos
#     (considerando solo aquellos que son positivos) es estrictamente mayor que
#     el umbral u }
# Por ejemplo, dadas
# s = [1,-2,0,5,-7,3]
# u = 5
# se debería devolver res = 3

def pos_umbral(s: list[int], u: int) -> int:
    indice: int = 0
    suma: int = 0
    while indice < len(s): # recorro la lista con un while
        if s[indice] >= 0: # el numero en la lista debe ser positivo
            suma += s[indice]
            if suma > u:
                return indice # me devuelve el indice del numero que, luego de la suma, supera el umbral
        indice += 1
    return -1

print(pos_umbral([1,-2,0,5,-7,3],5))

# 3) Columnas repetidas [3 puntos]
# Implementar la función columnas_repetidas, que dada una matriz no vacía de m
# columnas (con m par y m ≥ 2) devuelve True si las primeras m/2 columnas son
# iguales que las últimas m/2 columnas. Definimos a una secuencia de secuencias
# como matriz si todos los elementos de la primera secuencia tienen la misma
# longitud.

# problema columnas_repetidas(in mat:seq<seq<Z>>) : Bool {
#     requiere: {|mat| > 0}
#     requiere: {todos los elementos de mat tienen igual longitud m, con m > 0
#     (los elementos de mat son secuencias)}
#     requiere: {todos los elementos de mat tienen longitud par (la cantidad de
#     columnas de la matriz es par)}
#     asegura: {(res = true) <=> las primeras m/2 columnas de mat son iguales a
#     las últimas m/2 columnas}
# }

# Por ejemplo, dada la matriz
# m = [[1,2,1,2],
#      [-5,6,-5,6],
#      [0,1,0,1]]
# se debería devolver res = true
# TIP: para dividir un número entero x por 2 y obtener como resultado un número
# entero puede utilizarse la siguiente instrucción: int(x/2)

def columnas_repetidas(mat: list[list[int]]) -> bool:
    longitud_fila: int = len(mat[0])
    mitad: int = int(len(mat[0])/2)
    indice: int = 0
    otro_indice: int = 0   # hago un indice paralelo para cada elemento correspondiente a [n, n, n, n]
    indice_opuesto: int = mitad

    while indice < len(mat):
        while indice_opuesto < longitud_fila:
            if mat[indice][otro_indice] == mat[indice][indice_opuesto]:
                otro_indice += 1
                indice_opuesto += 1
            else:
                return False
        indice += 1
        indice_opuesto = mitad # restauro indice_opuesto
        otro_indice = 0 # restauro otro_indice
    return True

print(columnas_repetidas([[1,2,1,2],[-5,6,-5,6],[0,1,0,1]]))


# 4) Rugby 4 naciones [3 puntos]
# Implementar la función cuenta_posiciones_por_nacion que dada la lista de
# naciones que compiten en el torneo, y el diccionario que tiene los resultados
# de los torneos anuales en el formato año:posiciones_naciones, donde año es un
# número entero y posiciones_naciones es una lista de strings con los nombres de
# las naciones, genere un diccionario de naciones:#posiciones, que para cada
# Nación devuelva la lista de cuántas veces salió en esa posición.

# Tip: para crear una lista con tantos ceros como naciones se puede utilizar la
# siguiente sintaxis lista_ceros = [0]*len(naciones)

# problema cuenta_posiciones_por_nacion(in naciones: seq<String>, in torneos:
# dict<Z,seq<String>>: dict<String,seq<Z>> {
#     requiere: {naciones no tiene elementos repetidos}
#     requiere: {Los valores del diccionario torneos son permutaciones de la
#     lista naciones (es decir, tienen exactamente los mismos elementos que
#     naciones, en cualquier orden posible)}
#     asegura: {res tiene como claves los elementos de naciones}
#     asegura: {El valor en res de una nación es una lista de |naciones|
#     elementos que indica en la posición i cuántas veces salió esa nación en la
#     i-ésima posición.}
# }
# Por ejemplo, dados
# naciones= ["arg", "aus", "nz", "sud"]
# torneos= {2023:["nz", "sud", "arg", "aus"], 2022:["nz", "sud", "aus", "arg"]}
# se debería devolver res = {"arg": [0,0,1,1], "aus": [0,0,1,1], "nz": [2,0,0,0],
# "sud": [0,2,0,0]}

def cuenta_posiciones_por_nacion(naciones: list[str], torneos: dict[int, list[str]]) -> dict[str, list[int]]:
    posicion: dict = {}
    for nacion in naciones:
        posicion[nacion] = [0] * len(naciones) # agrego al diccionario posicion una clave de la nacion y una lista de 0 con |naciones|
    for epoca in torneos.keys(): # veo las claves de torneos
        for i in range(len(torneos[epoca])): # len(torneos[epoca]) = veo la longitud de las posiciones de las naciones  
            posicion[torneos[epoca][i]][i] += 1 # busco cada pais con [torneos[epoca][i]], y en esa posicion sumo 1 a la lista de 0 
    return posicion

naciones = ["arg", "aus", "nz", "sud"]
torneos = {2023:["nz", "sud", "arg", "aus"], 2022:["nz", "sud", "aus", "arg"]}
print(cuenta_posiciones_por_nacion(naciones, torneos))