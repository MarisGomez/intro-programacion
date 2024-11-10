import random
from queue import LifoQueue as Pila
from queue import Queue as Cola
c = Cola
p = Pila
#p.put(1) #APILAR
#elemento = p.get() #DESAPILAR
#p.empty() #VACIA? devuelvve un bool
#p.queue() #TRANSFORMA LA PILA EN UNA LISTA, no permitido

# PILAS - EJERCICIO 1
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila[int]:
    res:Pila = Pila()
    for i in range(cantidad):
        rand = random.randint(desde,hasta)
        res.put(rand)
    return res

def print_pila(p:Pila) -> None:
    contenedor: Pila = Pila()
    n:int
    while not p.empty():
        n = p.get()
        print(n)
        contenedor.put(n)
    while not contenedor.empty():
        p.put(contenedor.get())

#print_pila(generar_nros_al_azar(5,1,100))
#print(generar_nros_al_azar(5,1,100).queue) #.queue es una funcion para transformar pilas en listas, usar solo para test

# EJERCICIO 2
def cantidad_elementos(p:Pila) -> int:
    contenedor:Pila[int] = Pila()
    res:int = 0
    while not p.empty():
        res += 1
        contenedor.put(p.get())
    while not contenedor.empty():
        p.put(contenedor.get())
    return res

#pila = Pila()
#pila.put(25)
#pila.put(3)
#pila.put(9)
#pila.put(77)
#print(cantidad_elementos(pila))

# EJERCICIO 3
def buscar_el_maximo(p:Pila[int]) -> int:
    contenedor:Pila[int] = Pila()
    maximo:int = p.get()
    contenedor.put(maximo)

    while not p.empty():
        elementoActual = p.get()
        if maximo < elementoActual:
            maximo = elementoActual
        contenedor.put(elementoActual)
    while not contenedor.empty():
        p.put(contenedor.get())
    
    return maximo

# EJERCICIO 4
def buscar_nota_maxima(p:Pila[tuple[str, int]]) -> tuple[str, int]:
    contenedor:Pila[tuple[str, int]] = Pila()
    nota_maxima:tuple[str,int] = p.get()
    contenedor.put(nota_maxima)
    while not p.empty():
        elementoActual = p.get()
        contenedor.put(elementoActual)
        if nota_maxima[1] < elementoActual[1]:
            nota_maxima = elementoActual
    while not contenedor.empty():
        p.put(contenedor.get())
    return nota_maxima

#pila = Pila()
#pila.put(('juan',3))
#pila.put(('alex',9))
#pila.put(('mari',7))
#pila.put(('eze',8))
#print(buscar_nota_maxima(pila))

# EJERCICIO 6
def evaluar_expresion(expresion: str) -> float:
    tokens = expresion.split(" ")
    operadores: Pila = Pila()

    for token in tokens:
        if token in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            operadores.put(token)
        elif token in ["+", "-", "*", "/"]:
            n1 = int(operadores.get())
            n2 = int(operadores.get())
            if token == "+":
                operadores.put(n2 + n1)
            if token == "-":
                operadores.put(n2 - n1)
            if token == "*":
                operadores.put(n2 * n1)
            if token == "/":
                operadores.put(n2 / n1)
    return operadores.get()

#expresion = "3 4 + 5 * 2 -"
#print(evaluar_expresion(expresion))

# EJERCICIO 7
def intercalar(p1:Pila, p2:Pila) -> Pila:
    contenedor:Pila = Pila()
    contenedor_final:Pila = Pila()
    while not p1.empty() and not p2.empty():
        primerElem = p2.get()
        contenedor.put(primerElem)
        segundoElem = p1.get()
        contenedor.put(segundoElem)
    while not contenedor.empty():
        contenedor_final.put(contenedor.get())
    return contenedor_final


#p1 = Pila()
#p1.put(3)
#p1.put(5)
#p1.put(1)
#print_pila(p1)
#print(p1.queue)
#p2 = Pila()
#p2.put(2)
#p2.put(9)
#p2.put(12)
#print(p2.queue)
#print_pila(p2)
#print_pila(intercalar(p1,p2))

# COLAS - EJERCICIO 8
def generar_nros_al_azar2(cantidad:int, desde:int, hasta:int) -> Cola[int]:
    res:Cola = Cola()
    for i in range(cantidad):
        rand = random.randint(desde,hasta)
        res.put(rand)
    return res

def print_cola(c:Cola) -> None:
    contenedor: Cola = Cola()
    n:int
    while not c.empty():
        n = c.get()
        print(n)
        contenedor.put(n)
    while not contenedor.empty():
        c.put(contenedor.get())

#print(generar_nros_al_azar2(5,1,100).queue)
#print_cola(generar_nros_al_azar2(5,1,100))

# EJERCICIO 9
def cantidad_elementos2(c: Cola) -> int:
    contenedor:Cola[int] = Cola()
    res:int = 0
    while not c.empty():
        res += 1
        contenedor.put(c.get())
    while not contenedor.empty():
        c.put(contenedor.get())
    return res

# EJERCICIO 10
def buscar_el_maximo2(c:Cola[int]) -> int:
    contenedor:Cola[int] = Cola()
    maximo:int = c.get()
    contenedor.put(maximo)

    while not c.empty():
        elementoActual = c.get()
        if maximo < elementoActual:
            maximo = elementoActual
        contenedor.put(elementoActual)
    while not contenedor.empty():
        c.put(contenedor.get())
    
    return maximo

# EJERCICIO 11
def buscar_nota_minima(c:Cola[tuple[str, int]]) -> tuple[str, int]:
    contenedor:Cola[tuple[str, int]] = Cola()
    nota_minima:tuple[str,int] = c.get()
    contenedor.put(nota_minima)
    while not c.empty():
        elementoActual = c.get()
        contenedor.put(elementoActual)
        if nota_minima[1] > elementoActual[1]:
            nota_minima = elementoActual
    while not contenedor.empty():
        c.put(contenedor.get())
    return nota_minima

#cola = Cola()
#cola.put(('juan',3))
#cola.put(('alex',9))
#cola.put(('mari',7))
#cola.put(('eze',8))
#print(buscar_nota_minima(cola))

# EJERCICIO 12
def intercalar2(c1:Cola, c2:Cola) -> Cola:
    contenedor:Cola = Cola()
    while not c1.empty() and not c2.empty():
        primerElem = c1.get()
        contenedor.put(primerElem)
        segundoElem = c2.get()
        contenedor.put(segundoElem)
    return contenedor

#c1 = Cola()
#c1.put(3)
#c1.put(5)
#c1.put(1)
#print(c1.queue)
#c2 = Cola()
#c2.put(2)
#c2.put(9)
#c2.put(12)
#print(c2.queue)
#print_cola(intercalar2(c1,c2))

# EJERCICIO 13
def armar_secuencia_de_bingo() -> Cola[int]:
    res:Cola[int] = Cola()
    bolillero:list[int] = []
    for i in range (0,100):
        bolillero.append(i)

    random.shuffle(bolillero)
    
    i = 0
    while i < len(bolillero):
        res.put(bolillero[i])
        i += 1
    
    return res

#print(armar_secuencia_de_bingo().queue)

def jugar_carton_de_bingo(carton:list[int], bollillero:Cola[int]) -> int:
    bingo:int = 0
    jugadas:int = 0
    contenedor:Cola[int] = Cola()

    while bingo < len(carton):
        jugadas += 1
        bolita_actual = bollillero.get()
        contenedor.put(bolita_actual)
        if bolita_actual in carton:
            bingo += 1
    while not bollillero.empty():
        contenedor.put(bollillero.get())

    while not contenedor.empty():
        bollillero.put(contenedor.get())

    return jugadas

# EJERCICIO 14
def n_pacientes_urgentes(c:Cola[tuple[int, str, str]]) -> int:
    contenedor:Cola[tuple[int,str,str]] = Cola()
    pacientes_urgentes:int = 0
    while not c.empty():
        pacienteActual = c.get()
        contenedor.put(pacienteActual)
        if pacienteActual[0] <= 3:
            pacientes_urgentes += 1
    while not contenedor.empty():
        c.put(contenedor.get())
    return pacientes_urgentes

#cola = Cola()
#cola.put((3,'juan','kine'))
#cola.put((5,'alex','psico'))
#cola.put((2,'mari','gine'))
#cola.put((7,'eze','ofta'))
#print(n_pacientes_urgentes(cola))

# EJERCICIO 15
def atencion_a_clientes(c:Cola[tuple[str, int, bool, bool]]) -> Cola[tuple[str, int, bool, bool]]:
    contenedor:Cola = Cola()
    cliente_preferencial:Cola = Cola()
    cliente_prioridad:Cola = Cola()
    cliente_sin_prioridad:Cola = Cola()
    nuevo_orden:Cola = Cola()
    while not c.empty():
        clienteActual = c.get()
        contenedor.put(clienteActual)
        if clienteActual[3] == True:
            cliente_prioridad.put(clienteActual)
        elif clienteActual[2] == True:
            cliente_preferencial.put(clienteActual)
        else:
            cliente_sin_prioridad.put(clienteActual)
    while not cliente_prioridad.empty():
        nuevo_orden.put(cliente_prioridad.get())
    while not cliente_preferencial.empty():
        nuevo_orden.put(cliente_preferencial.get())
    while not cliente_sin_prioridad.empty():
        nuevo_orden.put(cliente_sin_prioridad.get())
    while not contenedor.empty(): #CONTENEDOR
        c.put(contenedor.get())
    return nuevo_orden

#c: Cola = Cola()
#c.put(["ana", 9999, True, True]) #1
#c.put(["dva", 9999, True, False]) #3
#c.put(["mercy", 9999, False, False]) #5
#c.put(["genji", 9999, False, True]) #2
#c.put(["hanzo", 9999, True, False]) #4
#c.put(["pharah", 9999, False, False]) #6
#print_cola(c)
#print_cola(atencion_a_clientes(c))

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