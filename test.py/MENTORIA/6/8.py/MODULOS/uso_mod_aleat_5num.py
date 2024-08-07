import random

def generador_numeros():
    return random.sample(range(1, 101), 5)

print("¡Bienvenido al generador de números aleatorios del Info! (números del 1 al 100).")
respuesta = input("¿Querés comenzar? S/N: ")

while respuesta.upper() == 'S':
    numeros = generador_numeros()
    print(f"Los números generados son: {numeros}")
    respuesta = input("¿Querés seguir generando números aleatorios? S/N: ").upper()

print("¡Gracias por jugar con el generador de números del Info!")
print("Gracias totales")