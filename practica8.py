class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    

class Perro(Animal):
    def __init__(self, especie, edad, dueño):
        super().__init__(especie, edad)
        self.dueño = dueño

perro1 = Perro("Canino", 5, "Daniel")
print(perro1.especie)  # Salida: Canino
print(perro1.edad)     # Salida: 5
print(perro1.dueño)    # Salida: Daniel
