
while True:
    # Ingresamos los tres números
    numero1 = int(input("Ingresa el primer número: "))
    numero2 = int(input("Ingresa el segundo número: "))
    numero3 = int(input("Ingresa el tercer número: "))

    # Comparamos los números y los ordenamos
    if numero1 <= numero2 and numero1 <= numero3:
        print(f"{numero1} es el menor de los tres números")
        if numero2 <= numero3:
            print(f"El orden es: {numero1}, {numero2}, {numero3}")
        else:
            print(f"El orden es: {numero1}, {numero3}, {numero2}")
    elif numero2 <= numero1 and numero2 <= numero3:
        print(f"{numero2} es el menor de los tres números")
        if numero1 <= numero3:
            print(f"El orden es: {numero2}, {numero1}, {numero3}")
        else:
            print(f"El orden es: {numero2}, {numero3}, {numero1}")
    else:
        print(f"{numero3} es el menor de los tres números")
        if numero1 <= numero2:
            print(f"El orden es: {numero3}, {numero1}, {numero2}")
        else:
            print(f"El orden es: {numero3}, {numero2}, {numero1}")

    # Preguntamos al usuario si desea continuar
    continuar = input("¿Deseas ingresar otros números? (s/n): ")
    if continuar.lower() != 's':
        break

     
     
   
# otro ejmplo
   
while True:
    try:
        num1 = int(input("Ingrese un número: "))
        num2 = int(input("Ingrese un segundo número: "))
        num3 = int(input("Ingrese un tercer número: "))
        break
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

numeros_ordenados = sorted([num1, num2, num3])
print("Números ordenados:", numeros_ordenados)



#Nancy Debárbora

while True:
    lista = []

    numero1 = int(input("Ingresa el primer número: "))
    lista.append(numero1)

    numero2 = int(input("Ingresa el segundo número: "))
    lista.append(numero2)

    numero3 = int(input("Ingresa el tercer número: "))
    lista.append(numero3)

    lista.sort()
    print(lista)

    # Preguntamos al usuario si desea continuar
    continuar = input("¿Deseas ingresar otros números? (s/n): ")
    if continuar.lower() != 's':
        break



#Rafael Ricardo Strongoli
#16:38

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))
numero3 = int(input("Ingrese otro número: "))

lista = [numero1, numero2, numero3]

for i in range(1, len(lista)):
    valor = lista[i]  # numero3
    posicion = i - 1  # 1
    while posicion >= 0 and lista[posicion] > valor:  # numero2 > numero3
        lista[posicion + 1] = lista[posicion]  # numero3 = numero2
        posicion -= 1
    lista[posicion + 1] = valor

print(lista)

#ejemplo profe
# ingresamos 3 numeros:
num1 = int(input("Ingresa el primer numero elegido: "))
num2 = int(input("Ingresa el segundo numero elegido: "))
num3 = int(input("Ingresa el tercer numero elegido: "))


lista = [num1,num2,num3]
for i in range(1, len (lista)):
    valor = lista [i]
    posicion = i-1
    while posicion >=0 and lista [posicion]> valor:
        lista[posicion+1]=lista[posicion]
        posicion-=1
    lista[posicion+1]=valor
    print(lista)    
        