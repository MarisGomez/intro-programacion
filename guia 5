-------------- ej 1 --------------
-- 1.1
longitud :: [Int] -> Int -- no anda cuando pongo [t] -> Integer 
longitud l | l == [] = 0
           | otherwise = 1 + longitud (tail l)

longitudPM :: [t] -> Integer
longitudPM [] = 0
longitudPM (_:xs) = 1 + longitud xs

-- 1.2
{-
problema ultimo (s: seq⟨T⟩) : T {
requiere: { |s| > 0 }
asegura: { resultado = s[|s| − 1] }
}
-}
ultimo :: [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs

-- 1.3
{-
problema principio (s: seq⟨T⟩) : seq⟨T⟩ {
requiere: { |s| > 0 }
asegura: { resultado = subseq(s, 0, |s| − 1) } 
}
subseq(s, 0, |s| − 1) s = refiere a la lista, 0 = desde donde empieza, |s| − 1 = donde termina (longitud total -1)
-}
principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x : principio xs

-- 1.4
{-
problema reverso (s: seq⟨T ⟩) : seq⟨T ⟩ {
requiere: { T rue }
asegura: { resultado tiene los mismos elementos que s pero en orden inverso.}
}
-}

reverso :: [t] -> [t]
reverso [x] = [x]
reverso xs = ultimo xs : reverso (principio xs)

-------------- ej 2 --------------
-- 2.1
{-
problema pertenece (e: T , s: seq⟨T ⟩) : B {
requiere: { T rue }
asegura: { resultado = true ↔ e ∈ s }
}
-}

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece e l | l == [] = False
              | otherwise = head l == e || pertenece e (tail l)

pertenecePM :: (Eq t) => t -> [t] -> Bool
pertenecePM _ [] = False
pertenecePM e (x:xs) = e == x || pertenecePM e xs

-- 2.2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [x] = True
todosIguales (x:xs) = x == head xs && todosIguales xs -- compara los elementos de izq a der
-- todosIguales (x:xs) = x == ultimo xs && todosIguales xs -- compara el primer elemento con el segundo recursivamente

-- 2.3
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos (x:xs) | (tail xs) == [] = True
                      | pertenece x xs = False
                      | otherwise = todosDistintos xs

-- 2.4
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos (x:xs) | (tail xs) == [] = False
                    | pertenece x xs = True
                    | otherwise = hayRepetidos xs

-- 2.5
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar e (x:xs) | e == x = xs
                | otherwise = x : quitar e xs

-- 2.6
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos e (x:xs) | e == x && not (pertenece e xs) = xs
                     | e == x && pertenece e xs = quitarTodos e xs
                     | otherwise = x : quitarTodos e xs

-- 2.7
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs) | pertenece x xs = x : quitarTodos x (eliminarRepetidos xs)
                         | otherwise = x : eliminarRepetidos xs

-- 2.8
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [x] [y] = x == y
mismosElementos (x:xs) (y:ys) | pertenece x (y:ys) && pertenece y (x:xs)  = mismosElementos xs ys
                              | otherwise = False

-- 2.9
capicua :: (Eq t) => [t] -> Bool
capicua [x] = True
capicua (x:xs) = x == ultimo xs && capicua (principio xs) -- consultar ej [1,2,3,3,2,1]

-------------- ej 3 -------------- (Listas de enteros)
-- 3.1
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

-- 3.2
productoria :: [Integer] -> Integer
productoria [] = 0
productoria (x:xs) = x * productoria xs

-- 3.3
maximo :: [Integer] -> Integer 
maximo [x] = x
maximo (x:y:xs) | x > y = maximo (x:xs)
                | otherwise = maximo (y:xs)

-- 3.4
sumarN :: Integer -> [Integer] -> [Integer]
sumarN 0 (x:xs) = (x:xs)
sumarN n [x] = [x+n]
sumarN n (x:xs) = (x+n) : sumarN n xs

-- 3.5
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:xs) = sumarN x (x:xs)

-- 3.6
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo (x:xs) = sumarN (ultimo (x:xs)) (x:xs)

-- 3.7
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | mod x 2 == 0 = x : pares xs
             | otherwise = pares xs

-- 3.8
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n [] = [] 
multiplosDeN n (x:xs) | mod n x == 0 = x : multiplosDeN n xs
                      | otherwise = multiplosDeN n xs

-- 3.9
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar x = ordenar (quitar (maximo x) x) ++ [maximo x]

-------------- ej 4 -------------- 
-- 4.1
sacarBlancosRepetidos :: [Char] -> [Char] -- no devuelve una lista ¿?
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs) | x == y && x == ' ' = sacarBlancosRepetidos (y:xs)
                               | otherwise = x : sacarBlancosRepetidos (y:xs)

-- 4.2
contarPalabras :: [Char] -> Integer
contarPalabras x = contarPalabrasSinBlancosRep (empiezaConUnBlanco (sacarBlancosRepetidos x))

contarPalabrasSinBlancosRep :: [Char] -> Integer
contarPalabrasSinBlancosRep [] = 0
contarPalabrasSinBlancosRep [x] = 1
contarPalabrasSinBlancosRep (x:xs) | x == ' ' = 1 + contarPalabrasSinBlancosRep xs
                                   | otherwise = contarPalabrasSinBlancosRep xs

empiezaConUnBlanco :: [Char] -> [Char]
empiezaConUnBlanco (x:xs) | x == ' ' = xs
                          | otherwise = x:xs


-------------- ej 6 -------------- 
type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

-- a
enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos _ [] = False
enLosContactos n [(nombre, tel)] | n == nombre = True
enLosContactos n ((nombre, tel):xs) | n == nombre = True
                                    | n /= nombre = enLosContactos n xs
                                    | otherwise = False

-- b
agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto (n,t) xs | perteneceContacto n xs = (n,t): eliminarContacto n xs
                     | otherwise = (n,t):xs

perteneceContacto :: String -> [(String, String)] -> Bool
perteneceContacto _ [] = False
perteneceContacto n ((nombre,_):xs) | n == nombre = True
                                    | otherwise = perteneceContacto n xs

-- c
eliminarContacto :: Nombre -> ContactosTel -> ContactosTel
eliminarContacto _ [] = []
eliminarContacto n ((nombre, tel):xs) | n == nombre = xs
                                      | otherwise = (nombre, tel) : eliminarContacto n xs

-------------- ej 7 -------------- 
type Identificacion = Integer
type Ubicacion = Texto
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]
type Disponibilidad = Bool

--lockers = [(100,(False,"ZD39I")),(101,(True,"JAH3I")),(103,(True,"IQSA9")),(105,(True,"QOTSA")),(109,(False,"893JJ")),(110,(False,"99292"))]

existeElLocker :: Identificacion -> MapaDeLockers -> Bool
existeElLocker _ [] = False
existeElLocker i ((iden, estado):xs) | i == iden = True
                                     | otherwise = existeElLocker i xs

ubicacionDelLocker :: Identificacion -> MapaDeLockers -> Ubicacion
ubicacionDelLocker _ [] = "no se ubica"
ubicacionDelLocker i ((iden,(dis,ubi)):xs) | i == iden = ubi
                                           | otherwise = ubicacionDelLocker i xs

estaDisponibleElLocker :: Identificacion -> MapaDeLockers -> Bool
estaDisponibleElLocker _ [] = False
estaDisponibleElLocker i ((iden,(dis,ubi)):xs) | i == iden = dis
                                               | otherwise = estaDisponibleElLocker i xs

ocuparLocker :: Identificacion ->MapaDeLockers ->MapaDeLockers
ocuparLocker _ [] = []
ocuparLocker i ((iden,(dis,ubi)):xs) | i == iden && dis = (iden,(not dis,ubi)):xs
                                     | otherwise = (iden,(dis,ubi)) : ocuparLocker i xs

