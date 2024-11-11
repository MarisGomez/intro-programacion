import math

# EJERCICIO 1.1
def imprimir_hola_mundo ():
    print("Hola Mundo")

# EJERCICIO 1.2
def imprimir_un_verso ():
    print("I give her all my love, \nThat's all i do.") #\n se utuliza para bajar una linea

# EJERCICIO 1.3
def raiz_de_2():
    res: float = round (math.sqrt(2),4)
    return res

# EJERCICIO 1.5
def perimetro ():
    res : float = 2 * math.pi
    return res

################################################################################################################################
# EJERCICIO 2.1
def imprimir_saludo (nombre:str) -> str:
    print ("Hola " + str(nombre))

# EJERCICIO 2.2
def raiz_cuadrada_numero (numero:int) -> float:
    return math.sqrt(numero)

# EJERCICIO 2.3
def fahrenheit_a_celsius (temp_far:float) -> float:
    return ((temp_far - 32)*5)/9

# EJERCICIO 2.4
def imprimir_dos_veces (estribillo: str) -> str:
    print (2 * estribillo)

# EJERCICIO 2.5
def es_multiplo_de (x: int, y:int) -> bool:
    return x % y == 0

# EJERCICIO 2.6
def es_par (numero:int) -> bool:
    return es_multiplo_de (numero,2)

# EJERCICIO 2.7
def cantidad_de_pizzas(comensales:int, min_cant_de_porciones:int) -> int:
    return round((comensales * min_cant_de_porciones)/8)
    
################################################################################################################################
# EJERCICIO 3.1
def alguno_es_0(numero1:float, numero2:float) -> bool:
    return numero1==0 or numero2==0 

# EJERCICIO 3.2
def ambos_son_0(numero1:float, numero2:float) -> bool:
    return numero1==0 and numero2==0

# EJERCICIO 3.3
def es_nombre_largo (nombre: str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8

# EJERCICIO 3.4
def es_bisiesto(año:int) -> bool:
    return es_multiplo_de(año,400) or (es_multiplo_de(año,4) and not(es_multiplo_de(año,100)))

################################################################################################################################
# EJERCICIO 4
def peso_pino (altura_en_metros:float) -> float:
    centimetros = altura_en_metros*100
    if altura_en_metros <= 3:
        return centimetros * 3
    else:
        return 900 + (centimetros-300) * 2

def es_peso_util (peso: float) -> bool:
    peso_min = 400
    peso_max = 1000
    return peso >= peso_min and peso <= peso_max

def sirve_pino (altura_en_metros:float) -> bool:
    return es_peso_util(peso_pino(altura_en_metros))

################################################################################################################################
# EJERCICIO 5.1
def devolver_el_doble_si_es_par(numero:int) -> int:
    if numero % 2 == 0:
        return numero * 2
    else:
        return numero
    
# EJERCICIO 5.2
def devolver_valor_si_es_par_sino_el_que_sigue(numero:int) -> int:
    if numero % 2 == 0:
        return numero
    else:
        return numero + 1

# EJERCICIO 5.3
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:int) -> int:
    if numero % 9 == 0:
        return numero * 3
    elif numero % 3 == 0:
        return numero * 2
    else:
        return numero

# EJERCICIO 5.4
def lindo_nombre(nombre:str) -> str:
    if len(nombre) >= 5:
        print("Tu nombre tiene muchas letras!")
    else:
        print("Tu nombre tiene menos de 5 caracteres")

# EJERCICIO 5.5
def elRango(numero:float) -> str:
    if numero < 10:
        print("Menor a 10")
    elif numero >= 10 and numero <= 20:
        print("Entre 10 y 20")
    else:
        print("Mayor a 20")

def vacaciones_o_trabajar (sexo:str, edad:int) -> str:
    if (sexo == "F" and edad >= 60) or (sexo == "M" and edad >= 65) or edad < 18:
        print("Andá de vacaciones")
    else:
        print("Te toca trabajar")

################################################################################################################################
# EJERCICIO 6.1 
def imprimir_numeros () -> None:
    inicio: int = 1
    fin: int = 10
    while inicio <= fin:
        print (inicio)
        inicio += 1

def imprimir_numeros2 () -> None:
    for n in range (1,11,1):
        print (n)

# EJERCICIO 6.2
def imprimir_pares () -> None:
    inicio: int = 10
    fin: int = 40
    while inicio <= fin:
        if inicio % 2 == 0:
            print (inicio)
        inicio += 1

def imprimir_pares2() -> None:
    for n in range (10,41,1):
        if n % 2 == 0:
            print(n)

# EJERCICIO 6.3
def eco () -> None:
    inicio: int = 1
    fin: int = 10
    while inicio <= fin:
        print ("eco")
        inicio += 1

def eco2 () -> None:
    for n in range (0,10,1):
        print("eco")

# EJERCICIO 6.4
def despegar (n:int) -> None:
    while n >= 0:
        print (n)
        n -= 1
    print ("Despegue!")

def despegar2 (n:int) -> None:
    for i in range (n,0,-1):
        print(i)
    print ("Despegue")

# EJERCICIO 6.5
def viaje_en_el_tiempo (año_partida:int, año_llegada:int) -> None:
    while año_partida > año_llegada:
        año_partida -= 1
        print("Viajó un año al pasado, estamos en el año:", año_partida)

def viaje_en_el_tiempo2 (año_partida:int, año_llegada:int) -> None:
    for n in range (año_partida,año_llegada,-1):
        print("Viajó un año al pasado, estamos en el año:", n)

# EJERCICIO 6.6
def viaje_aristoteles (año_partida: int) -> None:
    while año_partida >= 384:
        año_partida -= 20
        if año_partida >= 384:
            print("Viajó 20 años al pasado, estamos en el año:", año_partida)
        else:
            print("¡Si viajo más atrás nos conoceremos a Atistóteles!")

def viaje_aristoteles2 (año_partida: int) -> None:
    for n in range (año_partida,-384,-20):
        print("Viajó 20 años al pasado, estamos en el año:", n)
    print("¡Si viajo más atrás nos conoceremos a Atistóteles!")

if __name__ == '__main__':
    # EJERCICIO 1
    #imprimir_hola_mundo()
    #imprimir_un_verso()
    #print(raiz_de_2())
    #print(perimetro())
    # EJERCICIO 2
    #imprimir_saludo ("Pepito")
    #print(raiz_cuadrada_numero(10))
    #print (fahrenheit_a_celsius(100))
    #imprimir_dos_veces("Es lo malo de ser bueno en este mundo cruel \n")
    #print(es_multiplo_de(4,2))
    #print(es_par(10))
    #print(cantidad_de_pizzas(5,3))
    # EJERCICIO 3
    #print(alguno_es_0(2,0))
    #print(ambos_son_0(0,0))
    #print(es_nombre_largo("Lu"))
    #print(es_nombre_largo("Joni"))
    #print(es_nombre_largo("Guadalupe"))
    #print(es_bisiesto(2024))
    #print(peso_pino(5))
    #print(es_peso_util(700))
    #print(sirve_pino(2))
    #print(devolver_el_doble_si_es_par(2))
    #print(devolver_valor_si_es_par_sino_el_que_sigue(2))
    #print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(18))
    #lindo_nombre("susana")
    #elRango(9)
    #vacaciones_o_trabajar("F",19)
    #imprimir_numeros()
    #imprimir_pares()
    #imprimir_pares2()
    #eco()
    #despegar(10)
    #viaje_en_el_tiempo (2024,2020)
    #viaje_en_el_tiempo2 (2024,2020)
    viaje_aristoteles2 (2024)


# para abrir una "terminal" en python:
# en la carpeta del archivo ejecutar "python3" en la terminal, luego "impoort (nombre del archivo)"
# ctrl + D para salir
