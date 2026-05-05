# Programación orientada a objetos

# Métodos Dunder

# Ejemplo 1 - Cálculo de Vectores
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

#  Uso

v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2

print(v3)  # Output: Vector(6, 8)

#  Ejemplo 2 - Almacenamiento en caché de resultados

class ComputacionCache():
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n not in self.cache:
            self.cache[n] = self.calculo_costoso(n)
        return self.cache[n]
    
    def calculo_costoso(self, n):
        return n ** 2  # Simula un cálculo costoso
    

# Uso

computar = ComputacionCache()

print(computar(10))  # Output: 100 (calculado)
print(computar(5))  # Output: 100 (obtenido de la caché)

