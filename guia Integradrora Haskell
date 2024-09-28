-- EJ 1
{-
problema generarStock (productos: seq⟨String⟩) : seq⟨String × Z⟩ {
requiere: {True}
asegura: { La longitud de res es igual a la cantidad de productos distintos que hay en productos}
asegura: {Para cada producto que pertenece a productos existe un i tal que 0 ≤ i < |res| y res[i]0=producto y
res[i]1 es igual a la cantidad de veces que aparece producto en productos}
}
-}

productos :: [String] ->[(String, Int)]
productos [] = []
productos [x] = [(x, 1)]
productos (x:xs) = (x, cantApariciones x (x:xs)) : productos (quitarTodos x xs)

pertenece :: String -> [String] -> Bool
pertenece _ [] = False
pertenece p (x:xs) | p == x = True
                   | otherwise = pertenece p xs

quitarTodos :: String -> [String] -> [String]
quitarTodos _ [] = []
quitarTodos p (x:xs) | p == x && not (pertenece p xs) = xs
                     | p == x && pertenece p xs = quitarTodos p xs
                     | otherwise = x : quitarTodos p xs

cantApariciones :: String -> [String] -> Int
cantApariciones _ [] = 0
cantApariciones p (x:xs) | p == x = 1 + cantApariciones p xs
                         | otherwise = 0 + cantApariciones p xs

-- EJ 2
stockDeProducto :: [(String, Int)] -> String -> Int
stockDeProducto [] _ = 0
stockDeProducto ((producto, stock):xs) p | p == producto = stock
                                         | otherwise = stockDeProducto xs p

-- EJ 3
{-
problema dineroEnStock (stock: seq⟨String × Z⟩, precios: seq⟨String × R⟩ ) : R {
requiere: {No hay productos repetidos en stock}
requiere: {No hay productos repetidos en precios}
requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero}
requiere: {Todas las precios (segundas componentes) de precios son mayores a cero}
requiere: {Todo producto de stock aparece en la lista de precios}
asegura: {res es igual a la suma de los precios de todos los productos que est´an en stock multiplicado por la cantidad
de cada producto que hay en stock}
}
-}
dineroEnStock :: [(String, Int)] -> [(String, Float)] -> Float
dineroEnStock [] _ = 0
dineroEnStock ((producto, stock):xs) precios = precioProducto producto precios * fromIntegral (stockDeProducto ((producto, stock):xs) producto ) + dineroEnStock xs precios

precioProducto :: String -> [(String,Float)] -> Float
precioProducto producto ((p, precio):xs) |producto == p = precio
                                         |otherwise = precioProducto producto xs

-- EJ 4
aplicarOferta :: [(String, Int)] ->[(String, Float)] ->[(String,Float)]
aplicarOferta [] _ = []
aplicarOferta ((producto, stock):xs) precios | (stockDeProducto ((producto, stock):xs) producto) > 10 = (producto, precioProducto producto precios * 0.8) : aplicarOferta xs precios
                                             | otherwise = (producto, precioProducto producto precios) : aplicarOferta xs precios
