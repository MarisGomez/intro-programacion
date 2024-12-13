-- Ejercicio 1
stockPorProducto :: [String] -> String -> Int
stockPorProducto [] _ = 0
stockPorProducto (x:xs) p | x == p = 1 + stockPorProducto xs p
                          | otherwise = stockPorProducto xs p

eliminarTodos :: (Eq t) => [t] -> t -> [t]
eliminarTodos [] _ = []
eliminarTodos (x:xs) i | x == i = eliminarTodos xs i
                       | otherwise = x : eliminarTodos xs i

generarStock :: [String] ->[(String, Int)]
generarStock [] = []
generarStock (x:xs) = (x, stockPorProducto (x:xs) x) : generarStock (eliminarTodos xs x)

-- Ejercicio 2
stockDeProducto :: [(String, Int)] -> String -> Int
stockDeProducto [] _ = 0
stockDeProducto (x:xs) p | fst x == p = snd x
                         | otherwise = stockDeProducto xs p

-- Ejercicio 3
precioPorProducto :: [(String, Float)] -> String -> Float
precioPorProducto [] _ = 0
precioPorProducto (x:xs) p | fst x == p = snd x
                           | otherwise = precioPorProducto xs p

dineroEnStock :: [(String, Int)] -> [(String, Float)] -> Float
dineroEnStock [] _ = 0
dineroEnStock ((producto,stock):xs) precios = precioPorProducto precios producto * fromIntegral stock + dineroEnStock xs precios


-- Ejercicio 4
aplicarOferta :: [(String, Int)] -> [(String, Float)] -> [(String,Float)]
aplicarOferta [] _ = []
aplicarOferta ((producto, stock):xs) precios | stock > 10 = (producto, precioPorProducto precios producto*0.80) : aplicarOferta xs precios
                                             | otherwise = (producto, precioPorProducto precios producto) : aplicarOferta xs precios

