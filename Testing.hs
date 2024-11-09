-- en el archivo de las funciones, importar:
module MisFunciones where -- MisFunciones: nombre del archivo

-- en el archivo del test, importar:
module TestDeMisFunciones where -- TestDeMisFunciones: nombre del archivo

import Test.HUnit
import MisFunciones

----------------ej 1----------------
-- code
fib:: Integer -> Integer
fib n | n == 0 = 0
      | n == 1 = 1
      | otherwise = fib (n-1) + fib (n-2)

-- test
runFib = runTestTT testFib

testFib = test [
    "Caso base 1: fib 0" ~: (fib 0) ~?= 0,
    "Caso base 2: fib 1" ~: (fib 1) ~?= 1,
    "Caso recursivo 1: fib 2" ~: (fib 2) ~?= 1
    ]
----------------ej 1----------------
-- code
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | mod x 2 == 0 && not (pertenecePM x (pares xs)) = x : pares xs
             | otherwise = pares xs
-- test
runPares = runTestTT testPares

--------------------------------
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | mod x 2 == 0 && not (pertenecePM x (pares xs)) = x : pares xs
             | otherwise = pares xs


generarStock :: [String] -> [(String, Int)]
generarStock [p] = [(p, 1)]
generarStock (p:ps) = (p, registrarStock p (p:ps)) : generarStock ps

registrarStock :: String -> [String] -> Int
registrarStock _ [] = 0
registrarStock p (x:xs) | p == x = 1 + registrarStock p xs
                        | otherwise = 0 + registrarStock p xs


