# Solicitar la edad al usuario
edad = int(input("Escribe tu edad: "))

# Verificar si la persona es mayor de edad
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
    
    
    
    #usando while
    
    # Solicitar la edad al usuario
edad = int(input("Escribe tu edad: "))

# Verificar si la persona es mayor de edad usando un bucle while
while edad < 0:
    print("La edad no puede ser negativa. Inténtalo de nuevo.")
    edad = int(input("Escribe tu edad: "))

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")


#uso de len
numeros = [1, 2, 3, 4, 5]
print(len(numeros))  # Salida: 5

mensaje = "Hola, mundo"
print(len(mensaje))  # Salida: 11

numeros = [10, 20, 30, 40, 50]
for i in range(len(numeros)):
    print(f"Índice {i}: {numeros[i]}")


