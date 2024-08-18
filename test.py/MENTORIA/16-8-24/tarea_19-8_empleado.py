#Crea una clase Empleado que herede de la clase Persona y agregue atributos
# como sueldo y puesto.


# creo clase persona
class Persona():
    def __init__(self, Apellido, Nombre, Edad, Domicilio):
        self.Apellido = Apellido
        self.Nombre = Nombre
        self.Edad = Edad
        self.Domicilio = Domicilio
        
    def mostrar_datos_persona(self):    
        print(f"{self.Apellido}, {self.Nombre}, {self.Edad}, {self.Domicilio}")
persona1=Persona("Burgos", "Mauricio Fabian", 53,  "Av.V Sarsfield 145")
persona1.mostrar_datos_persona()        
       
       

class Empleado(Persona):
    def __init__(self, Apellido, Nombre, Edad, Domicilio, Puesto, Sueldo):
        super().__init__(Apellido, Nombre, Edad, Domicilio)
       
        self.Puesto = Puesto
        self.Sueldo = Sueldo
         
    def mostrar_datos_empleado(self):
        print(f"{self.Apellido}, {self.Nombre}, {self.Edad}, {self.Domicilio},  {self.Puesto}, {self.Sueldo}")
        

# Creo una instancia de Empleado
empleado1 = Empleado("Burgos", "Mauricio Fabian", 53,  "Av.V Sarsfield 145", "Gerente", 500000)

# Llamada a la función
empleado1.mostrar_datos_empleado()


        