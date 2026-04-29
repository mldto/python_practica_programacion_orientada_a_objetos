# Programación orientada a objetos

# Jugando con clases padres e hijas

class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    
    # Método para hablar pero con inserción particular
    def hablar(self):
        pass

    # Método para moverse pero con inserción particular
    def moverse(self):
        pass

    # Método para describirse pero con inserción particular
    def describeme(self):
        return f"Soy un {self.especie} y tengo {self.edad} años."
    

# Ejemplo simple de herencia sin modificar nada de la clase padre.
'''
# Clase hija que hereda de Animal
class Perro(Animal):
        pass

# Crear un objeto de la clase Perro
mi_perro = Perro("Perro", 5)
mi_perro.describeme();
'''

# Ejemplo de herencia con métodos modificados

# Clase hija que hereda de Animal
class Perro(Animal):
    def hablar(self):
        return "Guau guau!"
    
    def moverse(self):
        return "El perro corre."
    
    def describeme(self):
        return f"Soy un perro y tengo {self.edad} años."

# Crear un objeto de la clase Vaca

class Vaca(Animal):
    def hablar(self):
        return "Muu muu!"
    
    def moverse(self):
        return "La vaca camina lentamente."
    
    def describeme(self):
        return f"Soy una vaca y tengo {self.edad} años."

# Crar la clase Abeja

class Abeja(Animal):
    def hablar(self):
        return "Bzz bzz!"
    
    def moverse(self):
        return "La abeja vuela."
    
    def describeme(self):
        return f"Soy una abeja y tengo {self.edad} años."
    
    def picar(self):
        return "La abeja pica y duele mucho!"

# Crear objetos de las clases Perro, Vaca y Abeja
mi_perro = Perro("Perro", 5)
mi_vaca = Vaca("Vaca", 3)
mi_abeja = Abeja("Abeja", 1)

# Mostrar información de cada animal

# Perro
print(mi_perro.describeme())
print(mi_perro.hablar())

# Vaca
print(mi_vaca.describeme())
print(mi_vaca.hablar())

# Abeja
print(mi_abeja.describeme())
print(mi_abeja.hablar())
print(mi_abeja.picar())