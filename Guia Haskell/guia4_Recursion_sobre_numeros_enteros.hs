factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n-1)

-------------- ej 1 --------------

fib:: Integer -> Integer
fib n | n == 0 = 0
      | n == 1 = 1
      | otherwise = fib (n-1) + fib (n-2)

fib2:: Integer -> Integer
fib2 0 = 0
fib2 1 = 1
fib2 n = fib (n-1) + fib (n-2)

-------------- ej 2 --------------
{-
problema parteEntera (x: R) : Z {
requiere: { x ≥ 0 }
asegura: { resultado ≤ x < resultado + 1 }
}
-}

parteEntera :: Float -> Integer
parteEntera n | n>=0 && n<=1 = 0
parteEntera n = 1 + parteEntera (n-1)

-------------- ej 3 --------------
{-
Especificar e implementar la funci´on esDivisible :: Integer ->Integer ->Bool que dados dos n´umeros
naturales determinar si el primero es divisible por el segundo. No est´a permitido utilizar las funciones mod ni div
-}

esDivisible :: Integer ->Integer ->Bool
esDivisible a b | (a-b) == 0 = True
                | (a-b) < 0 = False
                | otherwise = esDivisible (a-b) b

-------------- ej 4 --------------

sumaImpares :: Integer -> Integer
sumaImpares n | n == 1 = 1
              | otherwise = nesimoImpar n + sumaImpares (n-1)
        where nesimoImpar n = 2*n-1

-------------- ej 5 --------------

medioFact :: Integer -> Integer
medioFact n | n == 0 = 1
            | n == 1 = 1
            | otherwise = n * medioFact (n-2)

-------------- ej 6 --------------

ultimoDigito :: Integer -> Integer
ultimoDigito n = mod n 10

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n<10 = True
                      | otherwise = ultimoDigito n == ultimoDigito (div n 10) && todosDigitosIguales (div n 10)

-------------- ej 7 --------------
{-
problema iesimoDigito (n: Z, i: Z) : Z {
requiere: { n ≥ 0 ∧ 1 ≤ i ≤ cantDigitos(n) }
asegura: { resultado = (n div 10cantDigitos(n)−i) mod 10 }
}

problema cantDigitos (n: Z) : N {
requiere: { n ≥ 0 }
asegura: { n = 0 → resultado = 1}
asegura: { n̸ = 0 → (n div 10resultado−1 > 0 ∧ n div 10resultado = 0) }
}
-}
cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1
              | otherwise = cantDigitos (div n 10) +1

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | cantDigitos n == i = mod n 10
                 | otherwise = iesimoDigito (div n 10) i

-------------- ej 8 --------------

sumaDigitos :: Integer -> Integer
sumaDigitos n | n < 10 = n
              | otherwise = ultimoDigito n + sumaDigitos (div n 10)

-------------- ej 9 --------------

esCapicua :: Integer -> Bool
esCapicua n | mod n 10 == iesimoDigito n 1 = True
            | otherwise = False

-------------- ej 10 --------------
-- A
f1 :: Integer -> Integer
f1 0 = 1
f1 n = f1 (n-1) + 2^n

-- B
f2 :: Integer -> Integer -> Integer
f2 n q | q == 1 = n
       | n == 1 = q
       | otherwise = f2 (n-1) q + q^n

-- C
f3 :: Integer -> Integer -> Integer
f3 n q = f2 (2*n) q

-- D
--f4 :: Integer -> Integer -> Integer
--f4 n q |

-------------- ej 11 --------------

factorial2 :: Integer -> Float
factorial2 0 = 1.0
factorial2 n = fromIntegral n * factorial2 (n-1)

eAprox :: Integer -> Float
eAprox x | x == 0 = 1
         | otherwise = eAprox (x-1) + (1 / factorial2 x)

-------------- ej 12 --------------

sucA :: Integer -> Float
sucA n | n == 1 = 2
       | otherwise = 2 + (1/ sucA (n-1))

raizDe2Aprox :: Integer ->Float
raizDe2Aprox n = sucA n - 1

-------------- ej 13 --------------

sumatoriaInterna :: Integer -> Integer -> Integer
sumatoriaInterna _ 0 = 0
sumatoriaInterna n j = n^j + sumatoriaInterna n (j-1)

sumatoriaDoble :: Integer -> Integer -> Integer
sumatoriaDoble 0 _ = 0
sumatoriaDoble n m = sumatoriaDoble (n-1) m + sumatoriaInterna n m

-------------- ej 14 --------------
-- dados tres naturales q, n, m sume todas las potencias de la forma q^a+b con 1 ≤ a ≤ n y 1 ≤ b ≤ m.

sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias _ 0 _ = 0
sumaPotencias q n m = sumaPotenciasSoloM q n m + sumaPotencias q (n-1) m

sumaPotenciasSoloM :: Integer -> Integer -> Integer -> Integer
sumaPotenciasSoloM _ _ 0 = 0
sumaPotenciasSoloM q n m = q^(n+m) + sumaPotenciasSoloM q n (m-1)

-------------- ej 15 --------------
sumaRacionales :: Integer -> Integer -> Float
sumaRacionales 0 m = 0
sumaRacionales n m = sumaRacionales (n - 1) m + sumaRacionalesSoloM n m

sumaRacionalesSoloM :: Integer -> Integer -> Float
sumaRacionalesSoloM n 1 = fromIntegral n
sumaRacionalesSoloM n m = (fromIntegral n/fromIntegral m) + sumaRacionalesSoloM n (m-1)

-------------- ej 16 --------------
-- A
menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n desde | mod n desde == 0 = desde
                          | otherwise = menorDivisorDesde n (desde + 1)

-- B
esPrimo :: Integer -> Bool
esPrimo n = n == menorDivisor n -- requiere n > 1

-- C ¿?
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos a b | a == 1 || b == 1 = True
                | (mod a b == 0) || (mod b a == 0) = False
                | otherwise = esPrimo a && esPrimo b || menorDivisor a /= menorDivisor b

-- D
nEsimoPrimo :: Integer -> Integer
nEsimoPrimo n | n == 1 = 2
              | otherwise = proxPrimo (nEsimoPrimo n)

proxPrimo :: Integer -> Integer
proxPrimo p | esPrimo p = p
            | otherwise = proxPrimo (p+1)

-------------- ej 17 --------------
