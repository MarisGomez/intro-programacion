menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n desde | mod n desde == 0 = desde
                          | otherwise = menorDivisorDesde n (desde + 1)

menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2

esPrimo :: Integer -> Bool
esPrimo n = n == menorDivisor n -- requiere n > 1

cantidadApariciones :: [Integer] -> Integer -> Integer
cantidadApariciones [] _ = 0
cantidadApariciones (x:xs) n | x == n = 1 + cantidadApariciones xs n
                             | otherwise = cantidadApariciones xs n

numeroMasFrecuente :: [Integer] -> Integer
numeroMasFrecuente [x] = x
numeroMasFrecuente (x:y:xs) | cantidadApariciones xs x >= cantidadApariciones xs y = numeroMasFrecuente (x:xs)
                            | otherwise = numeroMasFrecuente (y:xs)

filtrarNoPrimos :: [Integer] -> [Integer]
filtrarNoPrimos [] = []
filtrarNoPrimos (x:xs) | esPrimo x = x : filtrarNoPrimos xs
                       | otherwise = filtrarNoPrimos xs

primoMasFrecuente :: [Int] -> Int
primoMasFrecuente xs = numeroMasFrecuente (filtrarNoPrimos xs)