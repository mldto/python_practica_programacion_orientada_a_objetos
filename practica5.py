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