import random

# Generar un número entero aleatorio entre 1 y 10
numero_entero = random.randint(1, 10)
print(f"Número entero aleatorio: {numero_entero}")

# Generar un número flotante aleatorio entre 0 y 1
numero_flotante = random.random()
print(f"Número flotante aleatorio: {numero_flotante}")

# Seleccionar un elemento aleatorio de una lista
opciones = ['piedra', 'papel', 'tijera']
eleccion = random.choice(opciones)
print(f"Elección aleatoria: {eleccion}")

# Mezclar una lista
lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print(f"Lista mezclada: {lista}")





# ejemplo modulo 8
import random

def generador_numeros():
    return random.randint(1, 100)

print("¡Bienvenido al generador de números aleatorios del Info! (números del 1 al 100).")
respuesta = input("¿Querés comenzar? S/N: ")

while respuesta.upper() == 'S':
    numero = generador_numeros()
    print(f"El número generado es: {numero}")
    respuesta = input("¿Querés seguir generando números aleatorios? S/N: ").upper()

print("¡Gracias por jugar con el generador de números del Info!")
