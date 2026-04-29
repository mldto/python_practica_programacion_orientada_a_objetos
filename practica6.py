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