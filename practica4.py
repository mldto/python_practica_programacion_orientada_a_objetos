# Programación orientada a objetos

# Método de clase

class Prueba:
    @classmethod
    def metodo_clase(cls):
        return "Este es un método de clase", cls

print(Prueba.metodo_clase())