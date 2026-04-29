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