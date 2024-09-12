def sumar_lista(lista):
    return sum(lista)

def encontrar_maximo(lista):
    return max(lista)

def encontrar_minimo(lista):
    return min(lista)

def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]

def filtrar_impares(lista):
    return [num for num in lista if num % 2 != 0]

def main():
    print("Calculadora de listas")
    print("1. Sumar todos los elementos de una lista")
    print("2. Encontrar el máximo")
    print("3. Encontrar el mínimo")
    print("4. Filtrar por pares")
    print("5. Filtrar por impares")
    
    opcion = int(input("Seleccione una opción: "))
    lista = list(map(int, input("Ingrese los valores de la lista separados por espacios: ").split()))
    
    if opcion == 1:
        print("Suma:", sumar_lista(lista))
    elif opcion == 2:
        print("Máximo:", encontrar_maximo(lista))
    elif opcion == 3:
        print("Mínimo:", encontrar_minimo(lista))
    elif opcion == 4:
        print("Pares:", filtrar_pares(lista))
    elif opcion == 5:
        print("Impares:", filtrar_impares(lista))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
