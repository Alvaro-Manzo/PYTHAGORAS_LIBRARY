"""Suite de pruebas para la biblioteca Pytagoras."""

import unittest
import math
from Pytagoras import (
    calcular_hipotenusa,
    calcular_lado_a,
    calcular_lado_b,
    es_triangulo_rectangulo,
    validar_triangulo,
)


class PruebasCalculoPitagoras(unittest.TestCase):
    """Casos de prueba para los calculos del teorema de Pitagoras."""

    def prueba_calcular_hipotenusa_basico(self):
        """Prueba el calculo de la hipotenusa con triangulo 3-4-5."""
        resultado = calcular_hipotenusa(3, 4)
        self.assertAlmostEqual(resultado, 5.0, places=5)

    def prueba_calcular_hipotenusa_decimales(self):
        """Prueba el calculo de la hipotenusa con valores decimales."""
        resultado = calcular_hipotenusa(5.5, 7.3)
        esperado = math.sqrt(5.5**2 + 7.3**2)
        self.assertAlmostEqual(resultado, esperado, places=5)

    def prueba_calcular_lado_a(self):
        """Prueba el calculo del lado a."""
        resultado = calcular_lado_a(5, 4)
        self.assertAlmostEqual(resultado, 3.0, places=5)

    def prueba_calcular_lado_b(self):
        """Prueba el calculo del lado b."""
        resultado = calcular_lado_b(5, 3)
        self.assertAlmostEqual(resultado, 4.0, places=5)

    def prueba_es_triangulo_valido(self):
        """Prueba la validacion de un triangulo rectangulo valido."""
        resultado = es_triangulo_rectangulo(3, 4, 5)
        self.assertTrue(resultado)

    def prueba_es_triangulo_invalido(self):
        """Prueba la validacion de un triangulo no rectangulo."""
        resultado = es_triangulo_rectangulo(1, 2, 3)
        self.assertFalse(resultado)

    def prueba_validar_triangulo_valido(self):
        """Prueba la validacion explicita de un triangulo valido."""
        resultado = validar_triangulo(3, 4, 5)
        self.assertTrue(resultado)

    def prueba_validar_triangulo_invalido(self):
        """Prueba la validacion explicita de un triangulo invalido."""
        resultado = validar_triangulo(3, 4, 6)
        self.assertFalse(resultado)

    def prueba_calcular_hipotenusa_entrada_negativa(self):
        """Prueba que entradas negativas lanzar ValueError."""
        with self.assertRaises(ValueError):
            calcular_hipotenusa(-3, 4)

    def prueba_calcular_lado_a_hipotenusa_invalida(self):
        """Prueba que una hipotenusa invalida lanza ValueError."""
        with self.assertRaises(ValueError):
            calcular_lado_a(3, 5)

    def prueba_entrada_cero(self):
        """Prueba que entrada cero lanza ValueError."""
        with self.assertRaises(ValueError):
            calcular_hipotenusa(0, 4)

    def prueba_entrada_negativa_cero(self):
        """Prueba que entrada negativa con cero lanza ValueError."""
        with self.assertRaises(ValueError):
            calcular_lado_a(-5, 3)


if __name__ == "__main__":
    unittest.main()
