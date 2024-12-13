-- Ejercicio 1
{-
problema generarStock (productos: seq⟨String⟩) : seq⟨String × Z⟩ {
requiere: {True}
asegura: { La longitud de res es igual a la cantidad de productos distintos que hay en productos}
asegura: {Para cada producto que pertenece a productos existe un i tal que 0 ≤ i < |res| y res[i]0=producto y
res[i]1 es igual a la cantidad de veces que aparece producto en productos}
}
-}

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
{-
problema stockDeProducto (stock: seq⟨String × Z⟩, producto: String ) : Z {
requiere: {No hay productos repetidos en stock}
requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero}
asegura: {(res = 0 y producto no se encuentra en el stock) o (existe un i tal que 0 ≤ i < |stock| y producto = stock[i]0
y res = stock[i]1}
}
-}

stockDeProducto :: [(String, Int)] -> String -> Int
stockDeProducto [] _ = 0
stockDeProducto ((producto, stock):xs) p | producto == p = stock
                                         | otherwise = stockDeProducto xs p

-- Ejercicio 3
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

precioPorProducto :: [(String, Float)] -> String -> Float
precioPorProducto [] _ = 0
precioPorProducto ((producto, precio):xs) p | producto == p = precio
                                            | otherwise = precioPorProducto xs p

dineroEnStock :: [(String, Int)] -> [(String, Float)] -> Float
dineroEnStock [] _ = 0
dineroEnStock ((producto,stock):xs) precios = precioPorProducto precios producto * fromIntegral stock + dineroEnStock xs precios


-- Ejercicio 4
{-
problema aplicarOferta (stock: seq⟨String × Z⟩, precios: seq⟨String × R⟩ ) : seq⟨String × R⟩ {
requiere: {No hay productos repetidos en stock}
requiere: {No hay productos repetidos en precios}
requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero}
requiere: {Todas las precios (segundas componentes) de precios son mayores a cero}
requiere: {Todo producto de stock aparece en la lista de precios}
asegura: {|res| = |precios|}
asegura: {Para todo 0 ≤ i < |precios|, si stockDeProducto(stock, precios[i]0) > 10, entonces res[i]0 = precios[i]0 y
res[i]1 = precios[i]1∗ 0,80}
asegura: {Para todo 0 ≤ i < |precios|, si stockDeProducto(stock, precios[i]0) ≤ 10, entonces res[i]0 = precios[i]0 y
res[i]1 = precios[i]1 }
}
-}

aplicarOferta :: [(String, Int)] -> [(String, Float)] -> [(String,Float)]
aplicarOferta [] _ = []
aplicarOferta ((producto, stock):xs) precios | stock > 10 = (producto, precioPorProducto precios producto*0.80) : aplicarOferta xs precios
                                             | otherwise = (producto, precioPorProducto precios producto) : aplicarOferta xs precios


--------------- SOPA DE LETRAS
-- Ejercicio 5
{-
Fila = seq⟨Z⟩
Tablero = seq⟨F ila⟩
Posicion = Z × Z – Observaci´on: las posiciones son: (fila, columna)
Camino = seq⟨P osicion⟩

problema maximo (t: Tablero) : Z {
requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al
menos un elemento}
requiere: {Existe al menos una columna en el tablero t }
requiere: {El tablero t no es vac´ıo, todos los n´umeros del tablero son positivos, mayor estricto a 0}
asegura: {res es igual al n´umero m´as grande del tablero t}
}
-}

maximoFila :: [Int] -> Int
maximoFila [x] = x
maximoFila (x:y:xs) | x > y = maximoFila (x:xs)
                  | otherwise = maximoFila (y:xs)

maximo :: [[Int]] -> Int
maximo [x] = maximoFila x
maximo (x:y:xs) | maximoFila x > maximoFila y = maximo (x:xs)
                | otherwise = maximo (y:xs)

-- Ejercicio 6
reunirTodos :: [[Int]] -> [Int]
reunirTodos [x] = x
reunirTodos (x:y:xs) = x ++ y ++ reunirTodos xs

cantidadApariciones :: [Int] -> Int -> Int
cantidadApariciones [] _ = 0
cantidadApariciones (x:xs) i | x == i = 1 + cantidadApariciones xs i
                             | otherwise = cantidadApariciones xs i

cantidadAparicionesxElem :: [Int] -> [(Int, Int)]
cantidadAparicionesxElem [] = [] 
cantidadAparicionesxElem (x:xs) = (x, cantidadApariciones (x:xs) x) : cantidadAparicionesxElem (eliminarTodos xs x) 

maxCantAparicionesxElem :: [(Int, Int)] -> Int
maxCantAparicionesxElem [x] = fst x
maxCantAparicionesxElem (x:y:xs) | snd x > snd y = maxCantAparicionesxElem (x:xs)
                                 | otherwise = maxCantAparicionesxElem (y:xs)

masRepetido :: [[Int]] -> Int
masRepetido xs = maxCantAparicionesxElem (cantidadAparicionesxElem (reunirTodos xs))

-- Ejercicio 7
--valoresDeCamino :: [[Int]] -> [(Int, Int)] -> [Int]
