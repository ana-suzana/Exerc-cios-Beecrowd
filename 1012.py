#Area
entradas = input().split(" ")
a = float(entradas[0])
b = float(entradas[1])
c = float(entradas[2])
pi = 3.14159

area_triangulo = (a * c) / 2
print(f"TRIANGULO: {area_triangulo:.3f}")

area_circulo = pi * c**2
print(f"CIRCULO: {area_circulo:.3f}")

area_trapezio = ((a + b) * c) /2
print(f"TRAPEZIO: {area_trapezio:.3f}")

area_quadrado = b**2
print(f"QUADRADO: {area_quadrado:.3f}")

area_retangulo = a* b
print(f"RETANGULO: {area_retangulo:.3f}")
