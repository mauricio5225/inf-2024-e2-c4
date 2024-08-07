x = 10  # Variable global

def mi_funcion():
    global x
    x = 20  # Modifica la variable global
    print(x)

mi_funcion()
print(x)  # La variable global ha sido modificada

# anidadas
def externa():
    x = 10  # Variable no local

    def interna():
        nonlocal x
        x = 20  # Modifica la variable no local
        print(x)

    interna()
    print(x)

externa()

#while
lista = [1,2,3,4,5,6,7,8,9,10]
pares=0
i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
        pares += 1
    i += 1
print(f"la cant dd numeros pares hallados en la lista de : {pares}")

lista = [1, 2, 3, 4, 5, 6, 7]
pares = 0
i = 0

while i < len(lista):
    if lista[i] % 2 == 0:
        pares += 1
    i += 1

print("Number of even numbers:", pares)


#ejer 1 
palab=input("introduce una palabra a eleccion: ")
i=0
while i< len(palab):
    print(palab[i])
    i= i+1
    

# for
# Pedir al usuario una palabra
palabra = input("Introduce una palabra: ")

# Usar un bucle for para recorrer cada letra de la palabra
for letra in palabra:
    # Imprimir la letra
    print(letra)
print (palabra)

# 2 suma de numero
num = int (input("ingresa un numero: "))
suma = 0
i = 1
while i <= (num):
    suma = suma+i
    i= i+1
    print("la suma hasta el numero: ",num,"es",suma )

#jlfdj
# Pedir al usuario un número entero
num = int(input("Ingresa un número entero: "))

# Inicializar la suma
suma = 0

# Inicializar el contador
i = 1

# Usar un bucle while para sumar los números desde 1 hasta num
while i <= num:
    suma += i
    i += 1

# Imprimir el resultado
print("La suma de los números desde 1 hasta", num, "es", suma)

# uso for
num = int(input("Ingresa un número entero: "))
suma=0 


for i in range(1, num + 1):
    suma += i


    print (suma)
print(" la suma total es: ",suma)

    


