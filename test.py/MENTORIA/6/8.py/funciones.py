def invertir_cadena(cadena):
    return cadena[::-1]

# Ejemplo de uso
texto = "Python es divertido"
cadena_invertida = invertir_cadena(texto)
print(f"Cadena original: {texto}")
print(f"Cadena invertida: {cadena_invertida}")
                        
# crear una func llamada es_capicua que tome un numero como parámetor y devuelva True su es capucua  y False de lo contrario

def es_capicua (numero):
    cadena = str(numero)
    return cadena == cadena[::-1] 

numero=52124
if es_capicua(numero):
    print (f"El numero {numero} es capicua.")
else:
    print(f"El numero {numero} no es capicua.")
    
    
# factorial de n
def calcular_factorial(n):
    # Caso especial: 0! = 1
    if n == 0:
        return 1
    
    # Inicializar el factorial en 1
    factorial = 1
    
    # Multiplicar todos los números desde 1 hasta n
    for i in range(1, n + 1):
        factorial *= i
    
    return factorial

# Ejemplo de uso
numero =int(input("por favor ingrese un numero entero positivo: ")) 
print(f"El factorial de {numero} es {calcular_factorial(numero)}")


#
def calcular_factorial(n):
    # Caso especial: 0! = 1
    if n == 0:
        return 1
    
    # Inicializar el factorial en 1
    factorial = 1
    
    # Multiplicar todos los números desde 1 hasta n
    for i in range(1, n + 1):
        factorial *= i
    
    return factorial

# Bucle principal
while True:
    # Pedir al usuario que ingrese un número
    numero = int(input("Ingresa un número entero para calcular su factorial: "))
    
    # Calcular el factorial y mostrar el resultado
    print(f"El factorial de {numero} es {calcular_factorial(numero)}")
    
    # Preguntar al usuario si quiere calcular otro factorial
    continuar = input("¿Quieres calcular otro factorial? (s/n): ").lower()
    
    # Si el usuario no quiere continuar, romper el bucle
    if continuar != 's':
        print("¡Gracias por usar el programa!")
        break






   
