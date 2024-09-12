from operaciones import *





print("Bienvenido")
seguir = "SI"
while seguir == "SI":
    print("Elija una opción:  ")
    print("1-SUMA")
    print("2-RESTA")
    print("3-DIVIDIR")
    print("4-MULTIPLICAR")
    print("0-SALIR")
    
    oper = int(input())
    
    if oper == 0:
        seguir = "NO"
    elif oper > 4:
        print("Número incorrecto, por favor elija una opción válida.")
    else:
        num1 = int(input("Ingrese el primer número: ")) 
        num2 = int(input("Ingrese el segundo número: "))
        
        if oper == 1:
            resultado =suma(num1,num2) #num1 + num2
            print ("resultado",resultado)
        elif oper == 2:
            resultado = num1 - num2
        elif oper == 3:
            resultado = num1 // num2
        elif oper == 4:
            resultado = num1 * num2
        
        print(f"El resultado es: {resultado}")
        seguir = input("¿Seguimos? SI/NO\n: ").upper()
    
print("Gracias por usar nuestra calculadora")

#clase
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

          