--------------------------------------------------------------------------------------- 2023 TEMA 1
-- EJ 1
votosEnBlanco :: [(String, String)] -> [Int] -> Int -> Int
votosEnBlanco xs v vTotales = vTotales - sumaVotos v

-- auxiliar ej 1
sumaVotos :: [Int] -> Int
sumaVotos [] = 0
sumaVotos (x:xs) = x + sumaVotos xs

-- EJ 2
formulasValidas :: [(String,String)] -> Bool
formulasValidas [] = True
formulasValidas ((presi,vice):xs) | presi == vice = False
                                  | perteneceADupla presi xs || perteneceADupla vice xs = False
                                  | otherwise = formulasValidas xs

-- auxiliar ej 2
perteneceADupla :: String -> [(String, String)] -> Bool
perteneceADupla _ [] = False
perteneceADupla e ((x,y):xs) | e == x || e == y = True
                             | otherwise = perteneceADupla e xs

-- EJ 3
porcentajeDeVotos :: String -> [(String,String)] -> [Int] -> Float
porcentajeDeVotos presi formulas votos = division (cantVotosPorPresi presi formulas votos * 100) (sumaVotos votos) 

-- auxiliar ej 3
cantVotosPorPresi :: String -> [(String,String)] -> [Int] -> Int
cantVotosPorPresi presi ((p,v):xs) (votos:ys) | presi == p = votos
                                              | otherwise = cantVotosPorPresi presi xs ys

division :: Int -> Int -> Float
division a b = (fromIntegral a)/(fromIntegral b)

-- EJ 4
proximoPresidente :: [(String,String)] -> [Int] -> String
proximoPresidente formulas votos = fst (nElem (iesimoLugar (maximo votos) votos) formulas)

-- auxiliar ej 4
maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:xs) | x > y = maximo (x:xs)
                | otherwise = maximo (y:xs)

iesimoLugar :: (Eq t) => t -> [t] -> Int
iesimoLugar _ [] = 0
iesimoLugar i (x:xs) | i == x = 1
                     | otherwise = 1 + iesimoLugar i xs

nElem :: Int -> [t] -> t
nElem n (x:xs) | n == 1 = x
               | n /= 1 = nElem (n-1) xs 

--------------------------------------------------------------------------------------- 2023 TEMA 2
-- EJ 1
atajaronSuplentes :: [(String, String)] -> [Int] -> Int -> Int
atajaronSuplentes equipos goles totalGoles = totalGoles - sumatoria goles

-- auxiliar ej 1
sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

-- EJ 2
equiposValidos :: [(String, String)] -> Bool
equiposValidos [] = True
equiposValidos ((equipo, arquero):xs) | equipo == arquero = False
                                      | perteneceADupla equipo xs || perteneceADupla arquero xs = False
                                      | otherwise =  equiposValidos xs

-- auxiliar ej 2
perteneceADupla :: String -> [(String, String)] -> Bool
perteneceADupla _ [] = False
perteneceADupla x ((a,b):xs) | x == a || x == b = True
                             | otherwise = perteneceADupla x xs

-- EJ 3
porcentajeDeGoles :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeGoles _ _ [] = 0
porcentajeDeGoles nombre equipos goles = division (cantGolesPorArquero nombre equipos goles * 100) (sumatoria goles)

-- auxiliar ej 3
cantGolesPorArquero :: String -> [(String, String)] -> [Int] -> Int
cantGolesPorArquero nombre ((equipo,arquero):xs) (goles:gs) | nombre == arquero = goles
                                                            | otherwise = cantGolesPorArquero nombre xs gs

division :: Int -> Int -> Float
division a b = fromIntegral a / fromIntegral b

-- EJ 4
vallaMenosVencida :: [(String, String)] -> [Int] -> String
vallaMenosVencida equipos goles = snd (nElem (iesimoLugar (minimo goles) goles) equipos)

-- auxiliar ej 4
minimo :: [Int] -> Int
minimo [x] = x
minimo (x:y:xs) | x < y = minimo (x:xs)
                | otherwise = minimo (y:xs)

iesimoLugar :: (Eq t) => t -> [t] -> Int
iesimoLugar _ [] = 0
iesimoLugar i (x:xs) | i == x = 1
                     | otherwise = 1 + iesimoLugar i xs

nElem :: Int -> [t] -> t
nElem n [x] = x
nElem n (x:xs) | n == 1 = x
               | otherwise = nElem (n-1) xs

--------------------------------------------------------------------------------------- 2024 TEMA 1
-- EJ 1
aproboMasDeNMaterias :: [(String, [Int])] -> String -> Int -> Bool
aproboMasDeNMaterias [] _ _ = False
aproboMasDeNMaterias ((alumno, notas):xs) nombre n | nombre == alumno && notasAprobadas notas >= n = True
                                                   | nombre == alumno && notasAprobadas notas < n = False
                                                   | otherwise = aproboMasDeNMaterias xs nombre n

-- auxiliar ej 1
notasAprobadas :: [Int] -> Int
notasAprobadas [] = 0
notasAprobadas (x:xs) | x >= 4 = 1 + notasAprobadas xs
                      | otherwise = notasAprobadas xs

-- [("juan", [1,4,6,2]),("juana",[10,8,4,7]),("keiner",[2,6,8,4])]

-- EJ 2
buenosAlumnos :: [(String, [Int])] -> [String]
buenosAlumnos [] = []
buenosAlumnos ((alumno, notas):xs) | buenAlumno (alumno, notas) = alumno : buenosAlumnos xs
                                   | otherwise = buenosAlumnos xs

-- auxiliar ej 2
buenAlumno :: (String, [Int]) -> Bool
buenAlumno (alumno, notas) | longitud notas == notasAprobadas notas && promedioNotas notas >= 8 = True
                           | otherwise = False

promedioNotas :: [Int] -> Float
promedioNotas [] = 0
promedioNotas notas = division (sumatoria notas) (longitud notas)

longitud :: [Int] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

division :: Int -> Int -> Float
division a b = (fromIntegral a)/(fromIntegral b)

-- EJ 3
mejorPromedio:: [(String, [Int])] -> String
mejorPromedio [(alumno, notas)] = alumno
mejorPromedio ((alumno, notas):(alumno1, notas1):xs) | promedioNotas notas >= promedioNotas notas1 = mejorPromedio ((alumno, notas):xs)
                                                     | otherwise = mejorPromedio ((alumno1, notas1):xs)

-- EJ 4
seGraduoConHonores :: [(String, [Int])] -> Int -> String -> Bool
seGraduoConHonores [] materias nombre = False
seGraduoConHonores ((alumno, notas):xs) materias nombre 
    | nombre == alumno && aproboMasDeNMaterias ((alumno, notas):xs) nombre (materias-1) && pertenece nombre (buenosAlumnos ((alumno, notas):xs)) && promedioDelMejorPromedio ((alumno, notas):xs) - promedioNotas notas < 1  = True
    | otherwise = seGraduoConHonores xs materias nombre


-- auxiliar ej 4
pertenece :: String -> [String] -> Bool
pertenece _ [] = False
pertenece n (x:xs) | n == x = True
                   | otherwise = pertenece n xs

promedioDelMejorPromedio :: [(String, [Int])] -> Float
promedioDelMejorPromedio ((alumno, notas):xs) | alumno == mejorPromedio ((alumno, notas):xs) = promedioNotas notas
                                              | otherwise = promedioDelMejorPromedio xs

--------------------------------------------------------------------------------------- SIMULACRO
--module SolucionT2 where
-- ej 1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs) | e == x = True
                   | otherwise = pertenece e xs

relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((usuario1, usuario2):xs) | usuario1 == usuario2 = False
                                            | pertenece (usuario1, usuario2) xs || pertenece (usuario2, usuario1) xs = False
                                            | otherwise = relacionesValidas xs
-- ej 2
quitarTodos :: String -> [String] -> [String]
quitarTodos _ [] = []
quitarTodos e (x:xs) | e == x && not (pertenece e xs) = xs
                     | e == x && pertenece e xs = quitarTodos e xs
                     | otherwise = x : quitarTodos e xs

eliminarRepetidos :: [String] -> [String]
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs) | pertenece x xs = x : quitarTodos x (eliminarRepetidos xs)
                         | otherwise = x : eliminarRepetidos xs


personasAux :: [(String, String)] -> [String]
personasAux [] = []
personasAux ((usuario1, usuario2):xs) | relacionesValidas ((usuario1, usuario2):xs) == True = usuario1 : usuario2 : personasAux xs

personas :: [(String, String)] -> [String]
personas [] = []
personas xs = eliminarRepetidos (personasAux xs)

-- ej 3
perteneceDupla :: String -> (String, String) -> Bool
perteneceDupla e (a,b) | e == a || e == b = True
                       | otherwise = False

amigosDeAux :: String -> [(String, String)] -> [(String, String)]
amigosDeAux usuario [] = []
amigosDeAux usuario [x] | perteneceDupla usuario x = [x]
amigosDeAux usuario (x:xs) | perteneceDupla usuario x = x : amigosDeAux usuario xs
                           | otherwise = amigosDeAux usuario xs

amigosDe :: String -> [(String, String)] -> [String]
amigosDe _ [] = []
amigosDe usuario xs = quitarTodos usuario (personas (amigosDeAux usuario xs))

-- ej 4
masRepetido :: [String] -> String 
masRepetido [x] = x
masRepetido (x:y:xs) | cantidadDeApariciones x xs > cantidadDeApariciones y xs = masRepetido (x:xs)
                     | cantidadDeApariciones y xs > cantidadDeApariciones x xs = masRepetido (y:xs)
                     | otherwise = masRepetido (x:xs)

cantidadDeApariciones :: String -> [String] -> Int
cantidadDeApariciones _ [] = 0
cantidadDeApariciones e (x:xs) | e == x = 1 + cantidadDeApariciones e xs
                               | otherwise = 0 + cantidadDeApariciones e xs

personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos [] = "yo"
personaConMasAmigos xs = masRepetido (personasAux xs)
------------------------------------------------------------------------------------------------ TEST
main = runTestTT tests

tests = test [
	-- "nombre" ~: (funcion parametros) ~?= resultado_esperado
	"componentes repetidas" ~: (relacionesValidas [("ana", "ana")]) ~?= False,
	"tupla repetida" ~: (relacionesValidas [("ana", "pedro"), ("ana", "pedro")]) ~?= False,
	"tupla repetida invertida" ~: (relacionesValidas [("ana", "pedro"), ("pedro", "ana")]) ~?= False,
	"todas diferentes" ~: (relacionesValidas [("ana", "pedro"), ("ana", "carlos")]) ~?= True
	]

-- -- Ejemplos

-- usuario1 = "Juan"
-- usuario2 = "Natalia"
-- usuario3 = "Pedro"

-- relacion1_2 = (usuario1, usuario2)
-- relacion1_1 = (usuario1, usuario1)
-- relacion1_3 = (usuario1, usuario3)


-- -- FUNCIONES PARA TESTING, NO BORRAR
-- -- expectAny permite saber si el elemenot que devuelve la función es alguno de los esperados
-- expectAny actual expected = elem actual expected ~? ("expected any of: " ++ show expected ++ "\n but got: " ++ show actual)


-- -- sonIguales permite ver que dos listas sean iguales si no importa el orden
-- quitar :: (Eq t) => t -> [t] -> [t]
-- -- requiere x pertenece a y
-- quitar x (y:ys)
-- | x == y = ys
-- | otherwise = y : quitar x ys

-- incluido :: (Eq t) => [t] -> [t] -> Bool
-- incluido [] l = True
-- incluido (x:c) l = elem x l && incluido c (quitar x l)

-- sonIguales :: (Eq t) => [t] -> [t] -> Bool
-- sonIguales xs ys = incluido xs ys && incluido ys xs