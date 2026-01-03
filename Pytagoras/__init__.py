"""
Pytagoras: Biblioteca profesional para calculos del teorema de Pitagoras.

Esta biblioteca proporciona utilidades sencillas y faciles de usar para calcular
relaciones entre los lados de triangulos rectangulos.
"""

import math
from typing import Union


def calcular_hipotenusa(lado_a: float, lado_b: float) -> float:
    """
    Calcula la hipotenusa de un triangulo rectangulo.

    Utiliza el teorema de Pitagoras: c = sqrt(a^2 + b^2)

    Argumentos:
        lado_a: Longitud del primer lado.
        lado_b: Longitud del segundo lado.

    Retorna:
        La longitud de la hipotenusa.

    Lanza:
        ValueError: Si algun lado es menor o igual a cero.

    Ejemplo:
        >>> calcular_hipotenusa(3, 4)
        5.0
    """
    if lado_a <= 0 or lado_b <= 0:
        raise ValueError("Todos los lados deben ser mayores que cero.")

    return math.sqrt(lado_a**2 + lado_b**2)


def calcular_lado_a(hipotenusa: float, lado_b: float) -> float:
    """
    Calcula el lado 'a' de un triangulo rectangulo.

    Utiliza el teorema de Pitagoras: a = sqrt(c^2 - b^2)

    Argumentos:
        hipotenusa: Longitud de la hipotenusa.
        lado_b: Longitud del lado b.

    Retorna:
        La longitud del lado a.

    Lanza:
        ValueError: Si la hipotenusa no es el lado mas largo o los valores son invalidos.

    Ejemplo:
        >>> calcular_lado_a(5, 4)
        3.0
    """
    if hipotenusa <= 0 or lado_b <= 0:
        raise ValueError("Todos los lados deben ser mayores que cero.")

    if hipotenusa <= lado_b:
        raise ValueError("La hipotenusa debe ser mas larga que los otros lados.")

    return math.sqrt(hipotenusa**2 - lado_b**2)


def calcular_lado_b(hipotenusa: float, lado_a: float) -> float:
    """
    Calcula el lado 'b' de un triangulo rectangulo.

    Utiliza el teorema de Pitagoras: b = sqrt(c^2 - a^2)

    Argumentos:
        hipotenusa: Longitud de la hipotenusa.
        lado_a: Longitud del lado a.

    Retorna:
        La longitud del lado b.

    Lanza:
        ValueError: Si la hipotenusa no es el lado mas largo o los valores son invalidos.

    Ejemplo:
        >>> calcular_lado_b(5, 3)
        4.0
    """
    if hipotenusa <= 0 or lado_a <= 0:
        raise ValueError("Todos los lados deben ser mayores que cero.")

    if hipotenusa <= lado_a:
        raise ValueError("La hipotenusa debe ser mas larga que los otros lados.")

    return math.sqrt(hipotenusa**2 - lado_a**2)


def es_triangulo_rectangulo(lado_a: float, lado_b: float, lado_c: float) -> bool:
    """
    Verifica si tres lados forman un triangulo rectangulo.

    Esta funcion identifica automaticamente la hipotenusa como el lado mas largo
    y valida si se cumple el teorema de Pitagoras.

    Argumentos:
        lado_a: Longitud del primer lado.
        lado_b: Longitud del segundo lado.
        lado_c: Longitud del tercer lado.

    Retorna:
        True si los lados forman un triangulo rectangulo, False en caso contrario.

    Lanza:
        ValueError: Si algun lado es menor o igual a cero.

    Ejemplo:
        >>> es_triangulo_rectangulo(3, 4, 5)
        True
        >>> es_triangulo_rectangulo(1, 2, 3)
        False
    """
    if lado_a <= 0 or lado_b <= 0 or lado_c <= 0:
        raise ValueError("Todos los lados deben ser mayores que cero.")

    lados = sorted([lado_a, lado_b, lado_c])
    epsilon = 1e-9

    calculado = math.sqrt(lados[0]**2 + lados[1]**2)
    return abs(calculado - lados[2]) < epsilon


def validar_triangulo(lado_a: float, lado_b: float, hipotenusa: float) -> bool:
    """
    Valida si tres lados forman un triangulo rectangulo valido.

    Argumentos:
        lado_a: Longitud del primer lado.
        lado_b: Longitud del segundo lado.
        hipotenusa: Longitud de la hipotenusa.

    Retorna:
        True si los lados forman un triangulo rectangulo valido, False en caso contrario.

    Lanza:
        ValueError: Si algun lado es menor o igual a cero.

    Ejemplo:
        >>> validar_triangulo(3, 4, 5)
        True
    """
    if lado_a <= 0 or lado_b <= 0 or hipotenusa <= 0:
        raise ValueError("Todos los lados deben ser mayores que cero.")

    epsilon = 1e-9
    hipotenusa_calculada = math.sqrt(lado_a**2 + lado_b**2)
    return abs(hipotenusa_calculada - hipotenusa) < epsilon
