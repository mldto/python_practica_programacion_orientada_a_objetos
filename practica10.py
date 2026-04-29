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