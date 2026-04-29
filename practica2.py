# Programación Orientada a Objetos
# Práctica 2: Atributos y métodos de clase

class Perro:
    # Atributo de la clase
    especie = "Mamífero"

    def __call__(self, nombre, raza):
        print(f"Creando al perro {nombre}, {raza}")

        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza

print(Perro.especie) # Accediendo al atributo de clase