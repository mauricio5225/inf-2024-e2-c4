# Vamos a simular una granja con diferentes tipos de animales. Cada animal tendrá un método hacer_ruido(). Utilizaremos un bucle for para iterar sobre una lista de animales y hacer que cada uno emita su sonido.




class Animal:
    def hacer_ruido(self):
        pass

class Perro(Animal):
    def hacer_ruido(self):
        print("Guau guau")

class Gato(Animal):
    def hacer_ruido(self):
        print("Miau Miau")

class Vaca(Animal):
    def hacer_ruido(self):
        print("Muu Muu")

animales = [Perro(), Gato(), Vaca()]

for animal in animales:
    animal.hacer_ruido()
    
    
    
    # POO
    
class Coche():
    ruedas = 4
    
    # constructor
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    # metodo
 
    def acelerar(self):
        print ( f"El auto,{self.marca}, {self.modelo}, {self.color}, tiene una aceleración de 0 a 100 en 3 segundos")
        
    def frenado(self):
        print(f"El auto {self.marca}, {self.modelo}, {self.color}, tiene un frenado de 10 segundos")
        
        
        
# METODOS
    @classmethod
    def incrementar_ruedas(cls):
        cls.ruedas +=2
        
        
#        
    
mi_coche = Coche ("Fiat", "Novo Uno","Blanco")
otro_auto = Coche("VW", "Voyage","Negro")
print (mi_coche.marca)
print (mi_coche.modelo)
print (mi_coche.color)
print (mi_coche.ruedas)
print((f"Mi coche es de marca {mi_coche.marca}, modelo {mi_coche.modelo}, color {mi_coche.color} y tiene {mi_coche.ruedas} ruedas"))
print (f"Mi coche es de marca {otro_auto.marca}, modelo {otro_auto.modelo}, color {otro_auto.color} y tiene {otro_auto.ruedas} ruedas")
mi_coche.acelerar()
mi_coche.frenado()

       

            
 #           

class Contador:
    def __init__(self):
        self.cuenta = 0
    
    def incrementar(self):
        self.cuenta += 1

c = Contador()
c.incrementar()
print(c.cuenta)

for _ in range(2):
    c.incrementar()
print(c.cuenta) 
