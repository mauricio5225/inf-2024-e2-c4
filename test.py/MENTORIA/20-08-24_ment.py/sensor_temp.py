#Imagina una clase SensorTemperatura que registra la temperatura de un dispositivo. Queremos asegurarnos de que la
# temperatura se mantenga dentro de un rango seguro, por ejemplo, entre -40°C y 100°C.c



class SensorTemperatura:
    def __init__(self, temperatura_inicial):
        self.temperatura = temperatura_inicial

    def set_temperatura(self, nueva_temperatura):
        if -40 <= nueva_temperatura <= 100:
            self.temperatura = nueva_temperatura
        else:
            raise ValueError("Temperatura fuera del rango seguro (-40°C a 100°C)")

    def get_temperatura(self):
        return self.temperatura

# Ejemplo de uso
sensor = SensorTemperatura(25)  # Inicializa el sensor con una temperatura de 25°C
print(sensor.get_temperatura())  # Imprime la temperatura actual: 25

sensor.set_temperatura(50)  # Cambia la temperatura a 50°C
print(sensor.get_temperatura())  # Imprime la nueva temperatura: 50

try:
    sensor.set_temperatura(150)  # Intenta cambiar la temperatura a 150°C
except ValueError as e:
    print(e)  # Imprime el error: "Temperatura fuera del rango seguro (-40°C a 100°C)"
 # PANOZZO
 
class SensorTemperatura:
    temperatura_valida = True

    def __init__(self, temperatura_inicial=0.0):
        self.__temperatura = None
        self.set_temperatura(temperatura_inicial)

    def get_temperatura(self):
        if self.temperatura_valida:
            return self.__temperatura
        else:
            print("La temperatura no es válida.")
            return None

    def set_temperatura(self, nueva_temperatura):
        if -40 <= nueva_temperatura <= 100:
            self.__temperatura = nueva_temperatura
            self.temperatura_valida = True
        else:
            print("Error: La temperatura debe estar entre -40°C y 100°C.")
            self.temperatura_valida = False

# Ejemplo de uso
sensor = SensorTemperatura(25.0)
print(sensor.get_temperatura())  # Debería imprimir 25.0

sensor.set_temperatura(50.0)
print(sensor.get_temperatura())  # Debería imprimir 50.0

sensor.set_temperatura(500.0)
print(sensor.get_temperatura())  # Debería imprimir "La temperatura no es válida." y luego None


#

#Rafael Ricardo Strongoli
#16:29
class CarritoDeCompras:
    def __init__(self, precio_unitario):
        self.__cantidad = 0
        self.__precio_unitario = precio_unitario
        self.__precio_total = 0

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
        self.__precio_total = self.__precio_unitario * self.__cantidad

    def get_precio_total(self):
        return self.__precio_total

# Uso
carrito = CarritoDeCompras(100)
carrito.set_cantidad(5)
print(f"Precio total: {carrito.get_precio_total()}")  # Precio total: 500


class Empleado:
    def __init__(self, nombre, salario_anual):
        self.nombre = nombre
        self.__salario_anual = salario_anual

    def get_salario_mensual(self):
        return self.__salario_anual / 12

# Uso
empleado = Empleado("Carlos", 60000)
print(f"Salario mensual: {empleado.get_salario_mensual()}")  # 5000.0

# Intentar modificar el salario mensual directamente (no permitido)
# empleado.set_salario_mensual(6000)  # Error: Método no existe


# carrito de compra
class CarritoDeCompras:
    def __init__(self, precio_unitario):
        self.__cantidad = 0
        self.__precio_unitario = precio_unitario
        self.__precio_total = 0

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
        self.__precio_total = self.__precio_unitario * self.__cantidad

    def get_precio_total(self):
        return self.__precio_total

# Uso
carrito = CarritoDeCompras(100)
carrito.set_cantidad(5)
print(f"Precio total: {carrito.get_precio_total()}")  # Precio total: 500


class Empleado:
    def __init__(self, nombre, salario_anual):
        self.nombre = nombre
        self.__salario_anual = salario_anual

    def get_salario_mensual(self):
        return self.__salario_anual / 12

# Uso
empleado = Empleado("Carlos", 60000)
print(f"Salario mensual: {empleado.get_salario_mensual()}")  # 5000.0

# Intentar modificar el salario mensual directamente (no permitido)
# empleado.set_salario_mensual(6000)  # Error: Método no existe

