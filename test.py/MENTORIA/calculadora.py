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
            resultado = num1 + num2
        elif oper == 2:
            resultado = num1 - num2
        elif oper == 3:
            resultado = num1 // num2
        elif oper == 4:
            resultado = num1 * num2
        
        print(f"El resultado es: {resultado}")
        seguir = input("¿Seguimos? SI/NO\n: ").upper()
    
print("Gracias por usar nuestra calculadora")
       
