doubleMe :: Integer -> Integer
doubleMe x = x + x

---------- ej 1 -----------

f :: Integer -> Integer
f n | n == 1 = 8
    | n == 4 = 131
    | n == 16 = 16

{- otra forma 
f 1 = 8
f 4 = 131
f 16= 16 -}

g :: Integer -> Integer
g n | n == 8 = 16
    | n == 16 = 4
    | n == 131 = 1

-- h = fog, k = gof --
h :: Integer -> Integer
h n = f ( g n )
k :: Integer -> Integer
k n = g ( f n )

---------- ej 2 -----------

absoluto1 :: Integer -> Integer
absoluto1 x = abs x 

maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto x y  | abs x > abs y = abs x
                    | abs y > abs x = abs y

maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z   | x >= y && x >= z = x
                | y >= x && y >= z = y
                | otherwise = z

algunoEs0 :: Float -> Float -> Bool
algunoEs0 x y | x == 0 || y == 0 = True
              | otherwise = False

algunoEsoPM :: Float -> Float -> Bool
algunoEsoPM x y = x == 0 || y == 0

ambosSon0 :: Float -> Float -> Bool
ambosSon0 x y | x == 0 && y == 0 = True
              | otherwise = False

ambosSon0PM :: Float -> Float -> Bool
ambosSon0PM x y = x == 0 && y == 0

mismoIntervalo :: Float -> Float -> Bool --  (−∞, 3],(3, 7] y (7, ∞) --
mismoIntervalo x y = (x <= 3 && y <= 3) || ((3 < x && x <= 7) && (3 < y && y <= 7)) || (7 < x) && (7 < y)

sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | x /= y && x /= z && y /= z = x + y + z
                    | x == y && x /= z = z
                    | x == z && y /= z = y
                    | otherwise = 0

esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y | mod x y == 0 = True
                 | otherwise = False

digitoUnidades :: Integer -> Integer
digitoUnidades n = mod (abs n) 10

digitoDecenas :: Integer -> Integer
digitoDecenas n = digitoUnidades (div n 10)

---------- ej 3 -----------
{-
problema estanRelacionados (a:Z, b:Z) : Bool {
requiere: {a ̸= 0 ∧ b ̸= 0}
asegura: {(res = true) ↔ a ∗ a + a ∗ b ∗ k = 0 para alg´un k ∈ Z con k ̸= 0)}
}
-}
estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados  a b | mod a b == 0 = True
                        | otherwise = False

---------- ej 4 -----------

prodInt :: (Float, Float) -> (Float, Float) -> Float
prodInt (a, b) (c, d) = a * c + b * d 

todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor x y   | (fst x) < (fst y) && (snd x) < (snd y) = True
                | otherwise = False

todoMenor2 :: (Float, Float) -> (Float, Float) -> Bool
todoMenor2 (a,b) (c,d)  | a < c && b < d = True
                        | otherwise = False

{- la misma funcion con pattern matching-}
todoMenor3 :: (Float, Float) -> (Float, Float) -> Bool
todoMenor3 (a,b) (c,d) = a < c && b < d

distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos (a,b) (c,d) = sqrt ((c-a)^2) + ((d-b)^2)

sumaTerna :: (Int, Int, Int) -> Int
sumaTerna (a, b, c) = a + b + c

sumarSoloMultiplos :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos (a, b, c) n  | mod a n == 0 && mod b n == 0 && mod c n == 0 = a + b + c
                                | mod a n == 0 && mod b n == 0 && mod c n /= 0 = a + b
                                | mod a n == 0 && mod b n /= 0 && mod c n == 0 = a + c
                                | mod a n /= 0 && mod b n == 0 && mod c n == 0 = b + c
                                | mod a n == 0 && mod b n /= 0 && mod c n /= 0 = a
                                | mod a n /= 0 && mod b n == 0 && mod c n /= 0 = b
                                | mod a n /= 0 && mod b n /= 0 && mod c n == 0 = c
                                | otherwise = 0

posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (a, b, c)  | mod a 2 == 0 = 1
                        | mod b 2 == 0 = 2
                        | mod c 2 == 0 = 3
                        | otherwise = 4

crearPar :: a -> b -> (a, b)
crearPar a b = (a, b)

invertir :: (a, b) -> (b, a)
invertir (a, b) = (b, a)

---------- ej 5 -----------

{-
problema todosMenores (t : Z × Z × Z) : Bool {
requiere: {T rue}
asegura: {(res = true) ↔ ((f(t0) > g(t0)) ∧ (f(t1) > g(t1)) ∧ (f(t2) > g(t2)))}
}
problema f (n: Z) : Z {
requiere: {T rue}
asegura: {(n ≤ 7 → res = n
2
) ∧ (n > 7 → res = 2n − 1)}
}
problema g (n: Z) : Z {
requiere: {T rue}
asegura: {Si n es un n´umero par, entonces res = n/2, en caso contrario, res = 3n + 1}
}
-}

todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (x, y, z)  = f x > g x && f y > g y && f z > g z
    where
    f :: Integer -> Integer
    f n | n <= 7 = n^2
        | otherwise = 2*n - 1
    
    g :: Integer -> Integer
    g n | mod n 2 == 0 = div n 2
        | otherwise = 3*n + 1

---------- ej 6 -----------
{-
problema bisiesto (anio: Z) : Bool {
requiere: {True}
asegura: {res = false ↔ anio no es multiplo de 4, o anio es multiplo de 100 pero no de 400}
}
-}

type Anio = Integer
type EsBisiesto = Bool

bisiesto :: Anio -> EsBisiesto 
bisiesto a = mod a 4 == 0

---------- ej 7 -----------

absoluto :: Float -> Float
absoluto x  | x >= 0 = x
            | x <= 0 = -x

distanciaManhattan:: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (p0, p1, p2) (q0, q1, q2) = absoluto (p0 - q0) + absoluto (p1 - q1) + absoluto (p2 - q2)

---------- ej 8 -----------

{-
problema comparar (a:Z, b:Z) : Z {
requiere: {True}
asegura: {(res = 1 ↔ sumaUltimosDosDigitos(a) < sumaUltimosDosDigitos(b))}
asegura: {(res = −1 ↔ sumaUltimosDosDigitos(a) > sumaUltimosDosDigitos(b))}
asegura: {(res = 0 ↔ sumaUltimosDosDigitos(a) = sumaUltimosDosDigitos(b))}
}
problema sumaUltimosDosDigitos (x: Z) : Z {
requiere: {True}
asegura: {res = (|x| mod 10) + (⌊(|x|/10)⌋ mod 10)}
}
-}

comparar :: Int -> Int -> Int
comparar  a b   | sumaUltimosDosDigitos(a) < sumaUltimosDosDigitos(b) = 1
                | sumaUltimosDosDigitos(a) > sumaUltimosDosDigitos(b) = -1
                | otherwise = 0
        where 
        sumaUltimosDosDigitos :: Int -> Int
        sumaUltimosDosDigitos x = unidad(x) + decena(x)

        unidad :: Int -> Int
        unidad x = mod x 10
        
        decena :: Int -> Int
        decena x = unidad (div x 10)

---------- ej 9 -----------
{-
problema f1 (n:R) : R {
    requiere: {True}
    asegura: {res=1 si n es 0}
    asegura: {res=0 si no}
}
-}
f1 :: Float -> Float
f1 n | n == 0 = 1
        | otherwise = 0

{-
problema f2 (n:R) : R {
    requiere: {n es 1 o -1}
    asegura: {res=15 si n=1}
    asegura: {res=-15 si n=-1}
-}
f2 :: Float -> Float
f2 n | n == 1 = 15
        | n == -1 = -15

{-
problema f3 (n:R) : R {
    requiere: {True}
    asegura: {res=7 si n <= 9}
    asegura: {res=5 si n >= 3}
-}
f3 :: Float -> Float
f3 n | n <= 9 = 7
        | n >= 3 = 5

{-
problema f4 (x:R, y:R) : R {
    requiere: {True}
    asegura: {res es el promedio entre x e y}
-}
f4 :: Float -> Float -> Float
f4 x y = ( x + y )/2

{-
problema f5 ((x, y): R x R) : R {
    requiere: {True}
    asegura: {res es el promedio entre x e y}
-}
f5 :: ( Float , Float ) -> Float
f5 (x , y ) = ( x + y )/2

{-
problema f6 (a:R, b:Z) : R {
    requiere: {True}
    asegura: {res=True si la parte entera de x es y}
-}
f6 :: Float -> Int -> Bool
f6 a b = truncate a == b
