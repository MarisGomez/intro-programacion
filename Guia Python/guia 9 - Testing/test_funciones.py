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