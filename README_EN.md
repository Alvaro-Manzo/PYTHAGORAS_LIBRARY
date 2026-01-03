# Pythagorean

Professional and simple library for Pythagorean theorem calculations. Perfect for students, educators, and developers working with right triangles.

## Features

- Calculate hypotenuse from two sides
- Calculate missing sides given the hypotenuse
- Validate if three sides form a valid right triangle
- Clean, simple, and easy to use code
- Robust error handling
- Complete documentation in English
- No external dependencies
- Fully typed with type hints
- Unit test suite included

## Installation

### From PyPI (coming soon)

```bash
pip3 install Pythagorean
```

### For development

```bash
git clone https://github.com/Alvaro-Manzo/PYTHAGOREAN_LIBRARY.git
cd PYTHAGOREAN_LIBRARY
pip3 install -e .
```

## Quick Start

```python
from Pythagorean import calculate_hypotenuse, is_right_triangle

# Calculate hypotenuse with sides 3 and 4
result = calculate_hypotenuse(3, 4)
print(result)  # Output: 5.0

# Validate if it's a right triangle
valid = is_right_triangle(3, 4, 5)
print(valid)  # Output: True
```

## API Reference

### calculate_hypotenuse(side_a, side_b)

Calculate the hypotenuse of a right triangle using the Pythagorean theorem.

Formula: `c = √(a² + b²)`

**Parameters:**
- `side_a` (float): Length of the first side
- `side_b` (float): Length of the second side

**Returns:**
- (float): The length of the hypotenuse

**Raises:**
- `ValueError`: If any side is less than or equal to zero

**Example:**
```python
from Pythagorean import calculate_hypotenuse

# Calculate the hypotenuse of a 3-4-5 triangle
c = calculate_hypotenuse(3, 4)
print(c)  # 5.0

# With decimal values
c = calculate_hypotenuse(5.5, 7.3)
print(c)  # 9.140021881811881
```

---

### calculate_side_a(hypotenuse, side_b)

Calculate side 'a' given the hypotenuse and side 'b'.

Formula: `a = √(c² - b²)`

**Parameters:**
- `hypotenuse` (float): Length of the hypotenuse
- `side_b` (float): Length of side b

**Returns:**
- (float): The length of side a

**Raises:**
- `ValueError`: If the hypotenuse is not the longest side or values are invalid

**Example:**
```python
from Pythagorean import calculate_side_a

# Calculate side a knowing c=5 and b=4
a = calculate_side_a(5, 4)
print(a)  # 3.0
```

---

### calculate_side_b(hypotenuse, side_a)

Calculate side 'b' given the hypotenuse and side 'a'.

Formula: `b = √(c² - a²)`

**Parameters:**
- `hypotenuse` (float): Length of the hypotenuse
- `side_a` (float): Length of side a

**Returns:**
- (float): The length of side b

**Raises:**
- `ValueError`: If the hypotenuse is not the longest side or values are invalid

**Example:**
```python
from Pythagorean import calculate_side_b

# Calculate side b knowing c=5 and a=3
b = calculate_side_b(5, 3)
print(b)  # 4.0
```

---

### is_right_triangle(side_a, side_b, side_c)

Check if three sides form a valid right triangle.

This function automatically identifies which is the hypotenuse (the longest side) and validates if the Pythagorean theorem is satisfied.

**Parameters:**
- `side_a` (float): Length of the first side
- `side_b` (float): Length of the second side
- `side_c` (float): Length of the third side

**Returns:**
- (bool): True if the sides form a right triangle, False otherwise

**Raises:**
- `ValueError`: If any side is less than or equal to zero

**Example:**
```python
from Pythagorean import is_right_triangle

# Triangle 3-4-5 is valid
print(is_right_triangle(3, 4, 5))  # True

# Triangle 1-2-3 is not valid
print(is_right_triangle(1, 2, 3))  # False

# Order doesn't matter
print(is_right_triangle(5, 3, 4))  # True
```

---

### validate_triangle(side_a, side_b, hypotenuse)

Validate if three specific sides form a right triangle.

Use this function when you already know which is the hypotenuse.

**Parameters:**
- `side_a` (float): Length of the first side
- `side_b` (float): Length of the second side
- `hypotenuse` (float): Length of the hypotenuse

**Returns:**
- (bool): True if it's a valid right triangle, False otherwise

**Raises:**
- `ValueError`: If any side is less than or equal to zero

**Example:**
```python
from Pythagorean import validate_triangle

# Validate a 3-4-5 triangle
print(validate_triangle(3, 4, 5))  # True

# Validate an invalid triangle
print(validate_triangle(3, 4, 6))  # False
```

---

## Error Handling

All functions validate input values and raise descriptive exceptions if there are problems:

```python
from Pythagorean import calculate_hypotenuse

# Try to calculate with negative values
try:
    calculate_hypotenuse(-3, 4)
except ValueError as e:
    print(f"Error: {e}")
    # Error: All sides must be greater than zero.

# Try to calculate with zero
try:
    calculate_hypotenuse(0, 4)
except ValueError as e:
    print(f"Error: {e}")
    # Error: All sides must be greater than zero.

# Invalid hypotenuse
try:
    calculate_side_a(3, 5)  # 3 cannot be hypotenuse if the other side is 5
except ValueError as e:
    print(f"Error: {e}")
    # Error: Hypotenuse must be longer than the other sides.
```

## Practical Examples

### Example 1: Calculate the hypotenuse

```python
from Pythagorean import calculate_hypotenuse

# Problem: A ladder leans against a wall at 3 meters height
# and is 4 meters away from the wall. How long is the ladder?

height = 3
distance = 4
ladder_length = calculate_hypotenuse(height, distance)

print(f"The ladder is {ladder_length} meters long")
# The ladder is 5.0 meters long
```

### Example 2: Find an unknown side

```python
from Pythagorean import calculate_side_a

# Problem: In a right triangle, the hypotenuse measures 13 cm
# and one of the legs measures 5 cm. How long is the other leg?

hypotenuse = 13
known_leg = 5
unknown_leg = calculate_side_a(hypotenuse, known_leg)

print(f"The unknown leg measures {unknown_leg} cm")
# The unknown leg measures 12.0 cm
```

### Example 3: Validate a triangle

```python
from Pythagorean import is_right_triangle

# Problem: Check if three segments form a right triangle

side1 = 6
side2 = 8
side3 = 10

if is_right_triangle(side1, side2, side3):
    print("The segments form a right triangle")
else:
    print("The segments DO NOT form a right triangle")
```

## Tests

The library includes a complete unit test suite:

```bash
python3 -m pytest tests/
```

Or run tests directly:

```bash
python3 -m unittest tests.test_calculator
```

## Project Structure

```
PYTHAGOREAN_LIBRARY/
├── Pythagorean/               # Main package
│   └── __init__.py           # All functions
├── tests/
│   ├── __init__.py
│   └── test_calculator.py    # Test suite
├── setup.py                  # PyPI configuration
├── README.md                 # This file
├── LICENSE                   # MIT License
├── requirements.txt          # Dependencies
└── .gitignore
```

## Contributing

Contributions are welcome. Please:

1. Fork the repository
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

**Alvaro-Manzo**

- GitHub: [@Alvaro-Manzo](https://github.com/Alvaro-Manzo)
- Repository: [PYTHAGOREAN_LIBRARY](https://github.com/Alvaro-Manzo/PYTHAGOREAN_LIBRARY)

## The Pythagorean Theorem

The Pythagorean theorem states that in any right triangle, the square of the hypotenuse equals the sum of the squares of the legs:

**c² = a² + b²**

Where:
- `c` is the hypotenuse (the longest side)
- `a` and `b` are the legs (the other two sides)

This library implements this theorem so you can calculate any missing side or validate right triangles simply.

## FAQ

**What is the hypotenuse?**
The hypotenuse is the longest side of a right triangle, always opposite the 90-degree angle.

**Can I use decimal numbers?**
Yes, all functions accept decimal numbers and return precise results.

**What happens if I enter negative values?**
The library will raise a `ValueError` with a descriptive message.

**Can I use the library in commercial projects?**
Yes, it's licensed under MIT, which allows commercial use.

---

**Made with dedication by Alvaro-Manzo**
