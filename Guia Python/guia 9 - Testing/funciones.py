############# nombre archivo: "funciones.py"
def sumar ( x : int , y : int ) -> int :
    sumando : int = 0
    abs_y : int = 0
    if y < 0:
        sumando = -1
        abs_y = -y
    else :
        sumando = 1
        abs_y = y
    result : int = x
    count : int = 0
    while ( count < abs_y ):
        result = result + sumando
        count = count + 1
    return result

############# nombre archivo: "test_funciones.py"
# Este archivo puede usarse como template para testear funciones. 
import unittest
from funciones import sumar # Reemplazar por el import correspondiente para testear las funciones deseadas

# La clase puede tener otro nombre pero es necesario mantener el unittest.TestCase
class FuncionesTest(unittest.TestCase):

    # Definimos uno o más casos de test
    def test_1(self):
        self.assertEqual(sumar(3, -2), 1, "primer test")

    def test_2(self):
        self.assertEqual(sumar(3, 1), 4, "segundo test")

if __name__ == '__main__':
    unittest.main(verbosity=2)

#EN LA TERMINAL:
#coverage run --include=ejercicios.py -m unittest
#coverage report
#coverage html
#open htmlcov/index.html