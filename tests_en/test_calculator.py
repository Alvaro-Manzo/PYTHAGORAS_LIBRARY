"""Unit tests for the Pythagorean module."""

import unittest
import math
from Pythagorean import (
    calculate_hypotenuse,
    calculate_side_a,
    calculate_side_b,
    is_right_triangle,
    validate_triangle,
)


class TestPythagoreanCalculations(unittest.TestCase):
    """Test cases for Pythagorean theorem calculations."""

    def test_calculate_hypotenuse_basic(self):
        """Test hypotenuse calculation with 3-4-5 triangle."""
        result = calculate_hypotenuse(3, 4)
        self.assertAlmostEqual(result, 5.0, places=5)

    def test_calculate_hypotenuse_decimals(self):
        """Test hypotenuse calculation with decimal values."""
        result = calculate_hypotenuse(5.5, 7.3)
        expected = math.sqrt(5.5**2 + 7.3**2)
        self.assertAlmostEqual(result, expected, places=5)

    def test_calculate_side_a(self):
        """Test side a calculation."""
        result = calculate_side_a(5, 4)
        self.assertAlmostEqual(result, 3.0, places=5)

    def test_calculate_side_b(self):
        """Test side b calculation."""
        result = calculate_side_b(5, 3)
        self.assertAlmostEqual(result, 4.0, places=5)

    def test_is_right_triangle_valid(self):
        """Test validation of a valid right triangle."""
        result = is_right_triangle(3, 4, 5)
        self.assertTrue(result)

    def test_is_right_triangle_invalid(self):
        """Test validation of an invalid right triangle."""
        result = is_right_triangle(1, 2, 3)
        self.assertFalse(result)

    def test_validate_triangle_valid(self):
        """Test explicit validation of a valid triangle."""
        result = validate_triangle(3, 4, 5)
        self.assertTrue(result)

    def test_validate_triangle_invalid(self):
        """Test explicit validation of an invalid triangle."""
        result = validate_triangle(3, 4, 6)
        self.assertFalse(result)

    def test_calculate_hypotenuse_negative_input(self):
        """Test that negative inputs raise ValueError."""
        with self.assertRaises(ValueError):
            calculate_hypotenuse(-3, 4)

    def test_calculate_side_a_invalid_hypotenuse(self):
        """Test that invalid hypotenuse raises ValueError."""
        with self.assertRaises(ValueError):
            calculate_side_a(3, 5)

    def test_zero_input(self):
        """Test that zero inputs raise ValueError."""
        with self.assertRaises(ValueError):
            calculate_hypotenuse(0, 4)

    def test_negative_with_zero(self):
        """Test that negative input with zero raises ValueError."""
        with self.assertRaises(ValueError):
            calculate_side_a(-5, 3)


if __name__ == "__main__":
    unittest.main()
