#Crea una clase Cliente que herede de la clase Persona y agregue atributos
# como numero  de cliente y compra

class Persona():
    def __init__(self, Apellido, Nombre, Edad, Nacionalidad,  Domicilio):
        self.Apellido = Apellido
        self.Nombre = Nombre
        self.Edad = Edad
        self.Nacionalidad = Nacionalidad
        self.Domicilio = Domicilio
        
        
    def mostrar_datos_persona(self):    
        print(f"{self.Apellido}, {self.Nombre}, {self.Edad}, {self.Nacionalidad}, {self.Domicilio}")
        
persona1=Persona("Burgos", "Mauricio Fabian", 53, "Argentino", "Av. Velez Sarsfield 145")
persona1.mostrar_datos_persona() 

class Cliente(Persona):
    def __init__(self, Apellido, Nombre, Edad, Nacionalidad, Domicilio, Telefono, Numero_Cliente, Compra, Producto):
        super().__init__(Apellido, Nombre, Edad, Nacionalidad, Domicilio)
        
        self.Telefono = Telefono
        self.Numero_Cliente = Numero_Cliente
        self.Compra = Compra
        self.Producto = Producto
        
    def mostrar_datos_cliente(self):
        print(f"{self.Apellido}, {self.Nombre}, {self.Edad}, {self.Nacionalidad}, {self.Domicilio}, {self.Telefono} {self.Numero_Cliente}, {self.Compra}, { self.Producto}")

# Creo una instancia de Empleado
cliente1 = Cliente("Burgos", "Mauricio Fabian", 53, "Argentino", "Av.Velez Sarsfield 145", "3624603307 ", "000-000005225", "Informática", "Notebook Asus")
# Llamada a la función
cliente1.mostrar_datos_cliente()
