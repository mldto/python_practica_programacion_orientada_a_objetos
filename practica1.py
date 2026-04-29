# Programación orientada a objetos

'''
En la programación orientada a objetos, se utilizan clases para definir objetos que tienen atributos (características) y métodos (comportamientos).
Una clase es como un plano o plantilla para crear objetos. Un objeto es una instancia de una clase, que tiene sus propios valores para los atributos definidos en la clase.
En este ejemplo, se define una clase llamada "Perro" con un método constructor "__init__" que se ejecuta cuando se crea una instancia de la clase. El constructor recibe dos parámetros: "nombre" y "raza", que se asignan a los atributos de la instancia. Luego, se crea una instancia de la clase "Perro" llamada "mi_perro" con el nombre "Leo" y la raza "Caniche". Finalmente, se imprime el tipo de la instancia "mi_perro", que es de tipo "Perro".
'''

class Perro:
    def __init__(self, nombre, raza):
        print(f"Creando al perro {nombre}, {raza}")

        # Atributos de la instancia Perro
        self.nombre = nombre
        self.raza = raza

mi_perro = Perro("Leo", "Caniche");
print(type(mi_perro))