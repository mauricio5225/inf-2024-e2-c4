# Vamos a crear una tienda en línea simplificada. Tendremos productos con nombre, precio y cantidad en stock. Utilizaremos un bucle for para iterar sobre una lista de productos y un bucle while para simular la compra de productos hasta que el cliente decida salir.

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def venta(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Se han vendido {cantidad} unidad(es) de {self.nombre}")
        else:
            print(f"No hay suficiente stock.")

    def compra(self, precio, stock):
        self.precio = precio
        self.stock += stock

productos = [
    Producto("Zapatillas", 60000, 100),
    Producto("Pantalón", 10000, 80),
    Producto("Camisa", 5000, 30)
]

def tienda():
    while True:
        print("\nProductos disponibles:")
        for i, producto in enumerate(productos):
            if producto.stock > 0:
                print(f"{i+1} - {producto.nombre} - ${producto.precio}")
        opcion = int(input("¿Qué producto deseas comprar? - 0 para salir: "))
        if opcion == 0:
            print("Gracias. Vuelva pronto.")
            break
        cantidad = int(input("¿Cuántas unidades deseas? "))
        if opcion > 0 and opcion <= len(productos):
            print(f"Vas a comprar {cantidad} unidades de {productos[opcion - 1].nombre}. El costo total es de: ${cantidad * productos[opcion - 1].precio}")
            confirma = input("¿Confirmas la operación? (si/no): ")
            if confirma == "no":
                print("Gracias. Vuelva pronto.")
                break
            else:
                productos[opcion - 1].venta(cantidad)

tienda()
