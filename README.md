# Glosario de Practicas

Este documento indica de manera ordenada todos los tipos de practicas y lo que se ha trabajado en ella.

## Programación Orientada a Objetos

### Introducción

1. Practica 1: Atributos de instancia.

```python

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

```

### Atributos de clase

2. Practica 2: Atributos de clase.

```python
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
```

### Métodos de clase

3. Practica 3: Métodos de la clase.

```python
# Programación orientada a objetos

class Perro:

    especie = "Mammalia"

    # Constructor de la clase
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    # Método de la clase
    def ladrar(self):
        print("Woof, Woof, Bark")

    def caminar(self, pasos):
        print(f"El perro está caminando un total de {pasos} pasos")
    

mi_perro = Perro("Firulais", "Yorkshire Terrier");
mi_perro.ladrar()
mi_perro.caminar(10)
```


4. Practica 4: Método de la clase.

```python

# Programación orientada a objetos

# Método de clase

class Prueba:
    @classmethod
    def metodo_clase(cls):
        return "Este es un método de clase", cls

print(Prueba.metodo_clase())

```

5. Practica 5: Método de la clase (estático).

```python
# Programacion orientada a objetos

# Métodos de clase (Estático)

class Prueba:
    @staticmethod
    def metodo_estatico():
        return "Este es un método estático"

# Crear una instancia de la clase
prueba = Prueba()
Prueba.metodo_estatico()  # Llamada al método estático sin necesidad de crear una instancia
print(Prueba.metodo_estatico())  # Llamada al método estático a través de la clase
print(prueba.metodo_estatico())  # Llamada al método estático a través de la instancia
```

