import unittest

# Definición de la clase de prueba
class PruebaCalculadora(unittest.TestCase):

    def test_suma(self):
        resultado = 2 + 2
        self.assertEqual(resultado, 4)

    def test_resta(self):
        resultado = 5 - 3
        self.assertEqual(resultado, 2)

    def test_multiplicacion(self):
        resultado = 3 * 4
        self.assertEqual(resultado, 12)

    def test_division(self):
        resultado = 10 / 2
        self.assertEqual(resultado, 5)

        
if __name__ == '__main__':
    unittest.main()