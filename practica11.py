class Clase():
    def __init__(self, mi_atributo):
        self.__mi_atributo = mi_atributo
    
    @property
    def mi_atributo(self):
        return self.__mi_atributo
    
    @mi_atributo.setter
    def mi_atributo(self, valor):
        if valor != "":
            print("Valor asignado correctamente")
            self.__mi_atributo = valor
        else:
            print("Valor no asignado, el valor no puede ser una cadena vacía")


mi_clase = Clase("Valor inicial")


mi_clase.mi_atributo = "Nuevo valor" # Asignación válida

mi_clase.mi_atributo = ""  # Intento de asignar una cadena vacía (no válido)