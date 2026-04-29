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