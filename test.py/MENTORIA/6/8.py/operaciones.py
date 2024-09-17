#vamos la log de las operaciones
def suma(a,b):
    return a+b

def resta (a,b):
    return a-b

def multiplicacion (a,b):
    return a*b

def division(a,b):
    if (b==0):
        return "no se puede realizar la op de division por 0"
    else:
        return a/b
  
  
  
# ejerc profe    
    from MENTORIA.calculadora  import*
    
    
    
from operaciones import *

while True:
    print("Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elija una opción: ")

    if opcion == '5':
        break

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        resultado = suma(num1, num2)
        print("Resultado:", resultado)
    elif opcion == '2':
        resultado = resta(num1, num2)
        print("Resultado:", resultado)
    elif opcion == '3':
        resultado = multiplicacion(num1, num2)
        print("Resultado:", resultado)
    elif opcion == '4':
        resultado = division(num1, num2)
        print("Resultado:", resultado)
    else:
        print("Opción inválida.")
