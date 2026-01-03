"""
Pythagorean: Professional module for Pythagorean theorem calculations.

This module provides utilities for calculating relationships between sides
of right triangles using the Pythagorean theorem.
"""

import math
from typing import Union


def calculate_hypotenuse(side_a: float, side_b: float) -> float:
    """
    Calculate the hypotenuse of a right triangle.

    Uses the Pythagorean theorem: c = sqrt(a^2 + b^2)

    Args:
        side_a: Length of the first side.
        side_b: Length of the second side.

    Returns:
        The length of the hypotenuse.

    Raises:
        ValueError: If any side is less than or equal to zero.

    Example:
        >>> calculate_hypotenuse(3, 4)
        5.0
    """
    if side_a <= 0 or side_b <= 0:
        raise ValueError("All sides must be greater than zero.")

    return math.sqrt(side_a**2 + side_b**2)


def calculate_side_a(hypotenuse: float, side_b: float) -> float:
    """
    Calculate side 'a' of a right triangle.

    Uses the Pythagorean theorem: a = sqrt(c^2 - b^2)

    Args:
        hypotenuse: Length of the hypotenuse.
        side_b: Length of side b.

    Returns:
        The length of side a.

    Raises:
        ValueError: If hypotenuse is not the longest side or values are invalid.

    Example:
        >>> calculate_side_a(5, 4)
        3.0
    """
    if hypotenuse <= 0 or side_b <= 0:
        raise ValueError("All sides must be greater than zero.")

    if hypotenuse <= side_b:
        raise ValueError("Hypotenuse must be longer than the other sides.")

    return math.sqrt(hypotenuse**2 - side_b**2)


def calculate_side_b(hypotenuse: float, side_a: float) -> float:
    """
    Calculate side 'b' of a right triangle.

    Uses the Pythagorean theorem: b = sqrt(c^2 - a^2)

    Args:
        hypotenuse: Length of the hypotenuse.
        side_a: Length of side a.

    Returns:
        The length of side b.

    Raises:
        ValueError: If hypotenuse is not the longest side or values are invalid.

    Example:
        >>> calculate_side_b(5, 3)
        4.0
    """
    if hypotenuse <= 0 or side_a <= 0:
        raise ValueError("All sides must be greater than zero.")

    if hypotenuse <= side_a:
        raise ValueError("Hypotenuse must be longer than the other sides.")

    return math.sqrt(hypotenuse**2 - side_a**2)


def is_right_triangle(side_a: float, side_b: float, side_c: float) -> bool:
    """
    Check if three sides form a right triangle.

    This function automatically identifies the hypotenuse as the longest side
    and validates if the Pythagorean theorem is satisfied.

    Args:
        side_a: Length of the first side.
        side_b: Length of the second side.
        side_c: Length of the third side.

    Returns:
        True if the sides form a right triangle, False otherwise.

    Raises:
        ValueError: If any side is less than or equal to zero.

    Example:
        >>> is_right_triangle(3, 4, 5)
        True
        >>> is_right_triangle(1, 2, 3)
        False
    """
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        raise ValueError("All sides must be greater than zero.")

    sides = sorted([side_a, side_b, side_c])
    epsilon = 1e-9

    calculated = math.sqrt(sides[0]**2 + sides[1]**2)
    return abs(calculated - sides[2]) < epsilon


def validate_triangle(side_a: float, side_b: float, hypotenuse: float) -> bool:
    """
    Validate if three sides form a valid right triangle.

    Args:
        side_a: Length of the first side.
        side_b: Length of the second side.
        hypotenuse: Length of the hypotenuse.

    Returns:
        True if the sides form a valid right triangle, False otherwise.

    Raises:
        ValueError: If any side is less than or equal to zero.

    Example:
        >>> validate_triangle(3, 4, 5)
        True
    """
    if side_a <= 0 or side_b <= 0 or hypotenuse <= 0:
        raise ValueError("All sides must be greater than zero.")

    epsilon = 1e-9
    calculated_hypotenuse = math.sqrt(side_a**2 + side_b**2)
    return abs(calculated_hypotenuse - hypotenuse) < epsilon
