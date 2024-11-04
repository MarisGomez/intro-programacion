module Solucion where

type Ciudad = String
type Duracion = Float
type Vuelo = (Ciudad, Ciudad, Duracion)

type AgenciaDeViajes = [Vuelo]

-- EJERCICIO 1
vuelosValidos :: AgenciaDeViajes -> Bool
vuelosValidos [] = False
vuelosValidos [vuelo] = vueloValido vuelo
vuelosValidos (vuelo:xs) 
    | vueloValido vuelo == True && perteneceVuelo vuelo xs == True = vuelosValidos xs
    | otherwise = False

vueloValido :: Vuelo -> Bool
vueloValido (ciudad1, ciudad2, duracion) 
    | ciudad1 /= ciudad2 && duracion > 0 = True
    | otherwise = False

ciudadRepetida :: Vuelo -> Vuelo -> Bool
ciudadRepetida (origen1,destino1,_) (origen2,destino2,_) 
    | origen1 /= origen2 || destino1 /= destino2 = False
    | otherwise = True

perteneceVuelo :: Vuelo -> AgenciaDeViajes -> Bool
perteneceVuelo _ [] = True
perteneceVuelo vuelo1 (vuelo2:xs) 
    | ciudadRepetida vuelo1 vuelo2 == True = False
    | ciudadRepetida vuelo1 vuelo2 == False  = perteneceVuelo vuelo1 xs

-- EJERCICIO 2
ciudadesConectadas :: AgenciaDeViajes -> Ciudad -> [Ciudad]
ciudadesConectadas [] _ = []
ciudadesConectadas vuelos ciudad = eliminarRepetidos (perteneceCiudadEspecifica ciudad vuelos) 

ciudadEspecificaRepetida :: Ciudad -> Vuelo -> [Ciudad] -- devuelve la ciudad conectada en un vuelo especifico
ciudadEspecificaRepetida ciudadEspecifica (origen,destino,_) 
    | origen == ciudadEspecifica = [destino]
    | destino == ciudadEspecifica = [origen]
    | otherwise =  []

perteneceCiudadEspecifica :: Ciudad -> AgenciaDeViajes -> [Ciudad] -- devuelve la lista de ciudades conectadas pero pueden haber repeticiones
perteneceCiudadEspecifica _ [] = []
perteneceCiudadEspecifica ciudadEspecifica (vuelo:xs) = ciudadEspecificaRepetida ciudadEspecifica vuelo ++ perteneceCiudadEspecifica ciudadEspecifica xs

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece a xs 
    | length xs == 0 = False
    | a == head xs = True
    | otherwise = pertenece a (tail xs)

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos x xs 
    | xs == [] = []
    | x == head xs = [] ++ quitarTodos x (tail xs)
    | otherwise = [head xs] ++ quitarTodos x (tail xs)

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos [v] = [v]
eliminarRepetidos (x:xs) 
    | pertenece x xs = [x] ++ quitarTodos x (eliminarRepetidos xs)
    | otherwise = [x] ++ eliminarRepetidos xs

-- EJERCICIO 3
modernizarFlota :: AgenciaDeViajes -> AgenciaDeViajes
modernizarFlota [] = []
modernizarFlota ((origen,destino,duracion):vs) = (origen,destino,(duracion / 100)*90 ) : modernizarFlota vs

-- EJERCICIO 4
ciudadMasConectada :: AgenciaDeViajes -> Ciudad
ciudadMasConectada vuelos = masConectada vuelos (creadorLista vuelos)

creadorLista :: AgenciaDeViajes -> [Int] -- crea una lista con la cantidad de conecciones que tiene cada ciudad
creadorLista [] = []
creadorLista ((origen, destino, duracion):vs) = [length (ciudadesConectadas ((origen, destino, duracion):vs) origen)] ++ [(length(ciudadesConectadas ((origen, destino, duracion):vs) destino))] ++ creadorLista vs

masConexiones :: [Int] -> Int -- a partid de la lista devuelta por "creadorLista" encuentra el maximo
masConexiones [c] = c
masConexiones (c1:c2:cs) 
    | c1 >= c2 = masConexiones (c1:cs)
    | otherwise = masConexiones (c2:cs)

masConectada:: AgenciaDeViajes -> [Int] -> Ciudad -- relaciona la cantidad maxima de conecciones con su ciudad correspondiente
masConectada ((c1,c2,_):vs) (n1:n2:ns)
    | (masConexiones (n1:n2:ns) == n1) = c1
    | (masConexiones (n1:n2:ns) == n2) = c2
    | otherwise = masConectada vs ns

-- EJERCICIO 5
sePuedeLlegar :: AgenciaDeViajes -> Ciudad -> Ciudad -> Bool
sePuedeLlegar vuelos origen destino 
    | pertenece destino (listaDestinos vuelos origen) == True = True
    | recursionListaDestinos vuelos (listaDestinos vuelos origen) destino == True = True
    | otherwise = False

recursionListaDestinos :: AgenciaDeViajes -> [Ciudad] -> Ciudad -> Bool -- para saber si hay una posible escala
recursionListaDestinos _ [] _ = False
recursionListaDestinos vuelos (c1:cs) destino | pertenece destino (listaDestinos vuelos c1) == True = True
                                              | otherwise = recursionListaDestinos vuelos cs destino

listaDestinos :: AgenciaDeViajes -> Ciudad -> [Ciudad] -- devuelve la lista de destinos a los que puede llegar una ciudad especifica
listaDestinos [] _ = []
listaDestinos ((d1, d2, duracion):vs) ciudadEspecifica | d1 == ciudadEspecifica = [d2] ++ listaDestinos vs ciudadEspecifica
                                                       | otherwise = [] ++ listaDestinos vs ciudadEspecifica

-- EJERCICIO 6
duracionDelCaminoMasRapido :: AgenciaDeViajes -> Ciudad -> Ciudad -> Duracion
duracionDelCaminoMasRapido vuelos origen destino = duracionMasCorta (listaDuraciones vuelos origen destino)

duracionMasCorta :: [Duracion] -> Duracion -- minimo
duracionMasCorta [d] = d
duracionMasCorta (d1:d2:ds) 
    | d1 <= d2 = duracionMasCorta (d1:ds)
    | otherwise = duracionMasCorta (d2:ds)

listaDuraciones :: AgenciaDeViajes -> Ciudad -> Ciudad -> [Duracion] -- devuelve la lista de duraciones tanto de un vuelo directo como de una posible escala dado un origen y un destino
listaDuraciones vuelos origen destino 
    | pertenece destino (listaDestinos vuelos origen) == True = [duracionVuelo vuelos origen destino] ++ recursionListaDuraciones vuelos (listaDestinos vuelos origen) origen destino
    | otherwise = recursionListaDuraciones vuelos (listaDestinos vuelos origen) origen destino

recursionListaDuraciones :: AgenciaDeViajes -> [Ciudad] -> Ciudad -> Ciudad -> [Duracion] -- devuelve la lista de duraciones de las escalas dado un origen y un destino
recursionListaDuraciones _ [] _ _ = []
recursionListaDuraciones vuelos (c1:cs) origen destino 
    | pertenece destino (listaDestinos vuelos c1) == True = [(duracionVuelo vuelos origen c1) + (duracionVuelo vuelos c1 destino)] ++ recursionListaDuraciones vuelos cs origen destino
    | otherwise = recursionListaDuraciones vuelos cs origen destino

duracionVuelo :: AgenciaDeViajes -> Ciudad -> Ciudad -> Duracion -- devuelve la duracion de un vuelo directo dado un origen y un destino
duracionVuelo ((d1, d2, duracion):vs) origen destino 
    | d1 == origen && d2 == destino = duracion
    | otherwise = duracionVuelo vs origen destino


-- EJERCICIO 7
puedoVolverAOrigen :: AgenciaDeViajes -> Ciudad -> Bool
puedoVolverAOrigen [] _ = False
puedoVolverAOrigen vuelos ciudad = revisoPosiblesListasDeVuelos vuelos vuelos ciudad ciudad

revisoPosiblesListasDeVuelos :: AgenciaDeViajes -> AgenciaDeViajes -> Ciudad -> Ciudad -> Bool
revisoPosiblesListasDeVuelos [] _ _ _ = False
revisoPosiblesListasDeVuelos _ [] _ _ = False
revisoPosiblesListasDeVuelos listaInicial ((o,d,x):vs) origen destino 
    | origen == o = destino == d || revisoPosiblesListasDeVuelos (quitarTodos (o,d,x) listaInicial) (quitarTodos (o,d,x) listaInicial) d destino || revisoPosiblesListasDeVuelos (quitarTodos (o,d,x) listaInicial) vs origen destino
    | otherwise = revisoPosiblesListasDeVuelos listaInicial vs origen destino
