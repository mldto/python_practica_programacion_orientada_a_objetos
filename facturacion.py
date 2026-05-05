# Sistema de Facturación Sencillo

class Producto:
    def __init__(self, nombre , precio):
        self.nombre = nombre
        self.precio = precio

class Factura:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)

    
    def calcular_iva(self):
        return sum(p.precio for p in self.productos) * 1.21
    

factura = Factura()
factura.agregar_producto(Producto("Laptop", 1000))
factura.agregar_producto(Producto("Mouse", 50))
factura.agregar_producto(Producto("Teclado", 80))

for producto in factura.productos:
    print(f"{producto.nombre}: {producto.precio}€")

print(f"Total con IVA: {factura.calcular_iva():.2f}€")