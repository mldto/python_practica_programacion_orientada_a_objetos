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

## Clases Hijas

1. Practica 6: Introducción.
```python
# Programación orientada a objetos (Clases hijas)

'''
En la programación orientada a objetos, una clase hija es una clase que hereda atributos y métodos de una clase padre. Esto permite reutilizar código y crear una jerarquía de clases. La clase hija puede agregar sus propios atributos y métodos, o modificar los heredados de la clase padre.
'''

# Definimos una clase padre

class Animal:
    pass

# Definimos una clase hija que hereda de la clase padre

class Perro(Animal):
    pass

# Ver si la clase Perro es una subclase de la clase Animal

print(Perro.__bases__) # Muestra las clases de las que hereda Perro
```

2. Práctica 7: Jugando con las clases (I)
```python
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
```

3. Práctica 8: Añadir nuevos atributos a una clase hija.
```python
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
```

4. Práctica 9: Herencia Múltiple

```python
# Primer Ejemplo: Una clase que hereda de las dos anteriores.

class Uno():
    pass

class Dos():
    pass

class Tres(Uno, Dos):
    pass

# Segundo Ejemplo: Una clase que hereda de una clase que a su vez hereda de otra.

class Cuatro():
    pass

class Cinco(Cuatro):
    pass

class Seis(Cinco):
    pass    


print(Seis.__mro__) # MRO: Method Resolution Order (Orden de Resolución de Métodos) es el orden en el que se buscan los métodos en una jerarquía de clases. En este caso, el orden es Seis, Cinco, Cuatro, object.

# Una clase que hereda de las pasadas.

class Siete():
    pass

class Ocho():
    pass

class Nueve():
    pass

class Diez(Siete, Ocho, Nueve):
    pass

print(Diez.__mro__) # El orden es Diez, Siete, Ocho, Nueve, object.
```

## Decoradores

### Decorador Property

#### Básica
```python
# Programación Orientada a Objetos

# Decorador Property

'''

'''

class Prueba:
    def __init__(self, mi_atributo):
        self.__mi_atributo = mi_atributo

    @property
    def mi_atributo(self):
        return self.__mi_atributo

prueba = Prueba("Hola Mundo")
print(prueba.mi_atributo)
```

> [!NOTE]Nota
> Este código pertenece a la práctica 10.

