from Pytagoras import calcular_hipotenusa, es_triangulo_rectangulo

# Prueba 1: Calcular hipotenusa
resultado = calcular_hipotenusa(3, 4)
print(f"Hipotenusa de 3 y 4: {resultado}")

# Prueba 2: Validar triángulo
valido = es_triangulo_rectangulo(3, 4, 5)
print(f"¿Es 3-4-5 un triángulo rectángulo? {valido}")

# Prueba 3: Con decimales
c = calcular_hipotenusa(5.5, 7.3)
print(f"Hipotenusa de 5.5 y 7.3: {c}")
