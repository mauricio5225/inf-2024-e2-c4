#CALCULADORA BASICA CORREGIDA
           
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

while True:
    print("Bienvenido a la calculadora básica")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Ingrese el número de la operación que desea realizar: ")

    if opcion == "5":
        print("¡Hasta luego!")
        break

    if opcion not in ["1", "2", "3", "4", "5"]:
        print("Número incorrecto, elija un número de 1 a 5.")
        continue

    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            resultado = suma(num1, num2)
            print("El resultado de la suma es:", resultado)
        elif opcion == "2":
            resultado = resta(num1, num2)
            print("El resultado de la resta es:", resultado)
        elif opcion == "3":
            resultado = multiplicacion(num1, num2)
            print("El resultado de la multiplicación es:", resultado)
        elif opcion == "4":
            if num2 == 0:
                print("No se puede dividir entre cero")
            else:
                resultado = division(num1, num2)
                print("El resultado de la división es:", resultado)
    except ValueError:
        print("Error: Ingrese solo valores numéricos.")

    print("")

        
