class Vehiculo:
    def __init__(self, nombre):
        self.nombre = nombre 

    def mover(self, tipo):
        self.tipo = tipo


class Coche(Vehiculo):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def mover(self, tipo):
        super().mover(tipo)
        print(f"El coche {self.nombre} se mueve {self.tipo}")



todos_los_coches = []

while True:
    nombre = input("Ingrese el nombre del coche: ")
    tipo = input("Ingrese el tipo de movimiento (avanzar, retroceder, girar): ")

    coche = Coche(nombre)
    coche.mover(tipo)

    todos_los_coches.append(coche)

    continuar = input("¿Desea ingresar otro coche? (s/n): ")
    if continuar.lower() == 'n':
        break

print("\nTodos los coches ingresados:")
for coche in todos_los_coches:
    print(f"Coche: {coche.nombre}, Movimiento: {coche.tipo}")

