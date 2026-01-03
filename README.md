# Pytagoras

Biblioteca profesional y sencilla para realizar cálculos del teorema de Pitágoras. Perfecta para estudiantes, educadores y desarrolladores que necesitan trabajar con triángulos rectángulos.

## Características

- Calcula la hipotenusa a partir de dos lados
- Calcula lados faltantes dada la hipotenusa
- Valida si tres lados forman un triángulo rectángulo válido
- Código limpio, simple y fácil de usar
- Manejo robusto de errores
- Documentación completa en español
- Sin dependencias externas
- Totalmente tipado con type hints
- Suite de pruebas unitarias incluida

## Instalación

### Desde PyPI (próximamente)

```bash
pip3 install Pytagoras
```

### Para desarrollo

```bash
git clone https://github.com/Alvaro-Manzo/PYTHAGORAS_LIBRARY.git
cd PYTHAGORAS_LIBRARY
pip3 install -e .
```

## Inicio Rápido

```python
from Pytagoras import calcular_hipotenusa, es_triangulo_rectangulo

# Calcular hipotenusa con lados 3 y 4
resultado = calcular_hipotenusa(3, 4)
print(resultado)  # Salida: 5.0

# Validar si es un triángulo rectángulo
valido = es_triangulo_rectangulo(3, 4, 5)
print(valido)  # Salida: True
```

## Referencia de API

### calcular_hipotenusa(lado_a, lado_b)

Calcula la hipotenusa de un triángulo rectángulo usando el teorema de Pitágoras.

Fórmula: `c = √(a² + b²)`

**Parámetros:**
- `lado_a` (float): Longitud del primer lado
- `lado_b` (float): Longitud del segundo lado

**Retorna:**
- (float): La longitud de la hipotenusa

**Lanza:**
- `ValueError`: Si algún lado es menor o igual a cero

**Ejemplo:**
```python
from Pytagoras import calcular_hipotenusa

# Calcular la hipotenusa de un triángulo 3-4-5
c = calcular_hipotenusa(3, 4)
print(c)  # 5.0

# Con valores decimales
c = calcular_hipotenusa(5.5, 7.3)
print(c)  # 9.070127018922193
```

---

### calcular_lado_a(hipotenusa, lado_b)

Calcula el lado 'a' dada la hipotenusa y el lado 'b'.

Fórmula: `a = √(c² - b²)`

**Parámetros:**
- `hipotenusa` (float): Longitud de la hipotenusa
- `lado_b` (float): Longitud del lado b

**Retorna:**
- (float): La longitud del lado a

**Lanza:**
- `ValueError`: Si la hipotenusa no es el lado más largo o los valores son inválidos

**Ejemplo:**
```python
from Pytagoras import calcular_lado_a

# Calcular el lado a sabiendo que c=5 y b=4
a = calcular_lado_a(5, 4)
print(a)  # 3.0
```

---

### calcular_lado_b(hipotenusa, lado_a)

Calcula el lado 'b' dada la hipotenusa y el lado 'a'.

Fórmula: `b = √(c² - a²)`

**Parámetros:**
- `hipotenusa` (float): Longitud de la hipotenusa
- `lado_a` (float): Longitud del lado a

**Retorna:**
- (float): La longitud del lado b

**Lanza:**
- `ValueError`: Si la hipotenusa no es el lado más largo o los valores son inválidos

**Ejemplo:**
```python
from Pytagoras import calcular_lado_b

# Calcular el lado b sabiendo que c=5 y a=3
b = calcular_lado_b(5, 3)
print(b)  # 4.0
```

---

### es_triangulo_rectangulo(lado_a, lado_b, lado_c)

Verifica si tres lados forman un triángulo rectángulo válido.

Esta función identifica automáticamente cuál es la hipotenusa (el lado más largo) y valida si se cumple el teorema de Pitágoras.

**Parámetros:**
- `lado_a` (float): Longitud del primer lado
- `lado_b` (float): Longitud del segundo lado
- `lado_c` (float): Longitud del tercer lado

**Retorna:**
- (bool): True si los lados forman un triángulo rectángulo, False en caso contrario

**Lanza:**
- `ValueError`: Si algún lado es menor o igual a cero

**Ejemplo:**
```python
from Pytagoras import es_triangulo_rectangulo

# Triángulo 3-4-5 es válido
print(es_triangulo_rectangulo(3, 4, 5))  # True

# Triángulo 1-2-3 no es válido
print(es_triangulo_rectangulo(1, 2, 3))  # False

# El orden no importa
print(es_triangulo_rectangulo(5, 3, 4))  # True
```

---

### validar_triangulo(lado_a, lado_b, hipotenusa)

Valida si tres lados específicos forman un triángulo rectángulo.

Use esta función cuando ya sepa cuál es la hipotenusa.

**Parámetros:**
- `lado_a` (float): Longitud del primer lado
- `lado_b` (float): Longitud del segundo lado
- `hipotenusa` (float): Longitud de la hipotenusa

**Retorna:**
- (bool): True si es un triángulo rectángulo válido, False en caso contrario

**Lanza:**
- `ValueError`: Si algún lado es menor o igual a cero

**Ejemplo:**
```python
from Pytagoras import validar_triangulo

# Validar un triángulo 3-4-5
print(validar_triangulo(3, 4, 5))  # True

# Validar un triángulo inválido
print(validar_triangulo(3, 4, 6))  # False
```

---

## Manejo de Errores

Todas las funciones validan los valores de entrada y lanzan excepciones descriptivas si hay problemas:

```python
from Pytagoras import calcular_hipotenusa

# Intentar calcular con valores negativos
try:
    calcular_hipotenusa(-3, 4)
except ValueError as e:
    print(f"Error: {e}")
    # Error: Todos los lados deben ser mayores que cero.

# Intentar calcular con cero
try:
    calcular_hipotenusa(0, 4)
except ValueError as e:
    print(f"Error: {e}")
    # Error: Todos los lados deben ser mayores que cero.

# Hipotenusa inválida
try:
    calcular_lado_a(3, 5)  # 3 no puede ser hipotenusa si el otro lado es 5
except ValueError as e:
    print(f"Error: {e}")
    # Error: La hipotenusa debe ser mas larga que los otros lados.
```

## Ejemplos Prácticos

### Ejemplo 1: Calcular la hipotenusa

```python
from Pytagoras import calcular_hipotenusa

# Problema: Una escalera se apoya en una pared a 3 metros de altura
# y está a 4 metros de distancia de la pared. ¿Cuánto mide la escalera?

altura = 3
distancia = 4
largo_escalera = calcular_hipotenusa(altura, distancia)

print(f"La escalera mide {largo_escalera} metros")
# La escalera mide 5.0 metros
```

### Ejemplo 2: Encontrar un lado desconocido

```python
from Pytagoras import calcular_lado_a

# Problema: En un triángulo rectángulo, la hipotenusa mide 13 cm
# y uno de los catetos mide 5 cm. ¿Cuánto mide el otro cateto?

hipotenusa = 13
cateto_conocido = 5
cateto_desconocido = calcular_lado_a(hipotenusa, cateto_conocido)

print(f"El cateto desconocido mide {cateto_desconocido} cm")
# El cateto desconocido mide 12.0 cm
```

### Ejemplo 3: Validar un triángulo

```python
from Pytagoras import es_triangulo_rectangulo

# Problema: Verificar si tres segmentos forman un triángulo rectángulo

lado1 = 6
lado2 = 8
lado3 = 10

if es_triangulo_rectangulo(lado1, lado2, lado3):
    print("Los segmentos forman un triángulo rectángulo")
else:
    print("Los segmentos NO forman un triángulo rectángulo")
```

## Pruebas

La biblioteca incluye una suite completa de pruebas unitarias:

```bash
python3 -m pytest tests/
```

O ejecutar las pruebas directamente:

```bash
python3 -m unittest tests.test_calculator
```

## Estructura del Proyecto

```
PYTHAGORAS_LIBRARY/
├── Pytagoras/                  # Paquete principal
│   └── __init__.py            # Todas las funciones
├── tests/
│   ├── __init__.py
│   └── test_calculator.py     # Suite de pruebas
├── setup.py                   # Configuración para PyPI
├── README.md                  # Este archivo
├── LICENSE                    # Licencia MIT
├── requirements.txt           # Dependencias
└── .gitignore
```

## Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## Autor

**Alvaro-Manzo**

- GitHub: [@Alvaro-Manzo](https://github.com/Alvaro-Manzo)
- Repositorio: [PYTHAGORAS_LIBRARY](https://github.com/Alvaro-Manzo/PYTHAGORAS_LIBRARY)

## Teorema de Pitágoras

El teorema de Pitágoras establece que en todo triángulo rectángulo, el cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos:

**c² = a² + b²**

Donde:
- `c` es la hipotenusa (el lado más largo)
- `a` y `b` son los catetos (los otros dos lados)

Esta biblioteca implementa este teorema para que puedas calcular cualquier lado faltante o validar triángulos rectángulos de forma sencilla.

## Preguntas Frecuentes

**¿Qué es la hipotenusa?**
La hipotenusa es el lado más largo de un triángulo rectángulo, siempre opuesto al ángulo de 90 grados.

**¿Puedo usar números decimales?**
Sí, todas las funciones aceptan números decimales y devuelven resultados precisos.

**¿Qué pasa si ingreso valores negativos?**
La biblioteca lanzará un error `ValueError` con un mensaje descriptivo.

**¿Puedo usar la biblioteca en proyectos comerciales?**
Sí, está licenciada bajo MIT, lo que permite uso comercial.

---

**Hecho con dedicación por Alvaro-Manzo**
