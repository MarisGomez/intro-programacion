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

