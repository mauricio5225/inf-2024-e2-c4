lista = [32, 1, 2, 3, 4, 5, 65]

while True:
    print('''
    0 - Salir
    1 - Sumar todos los elementos de la lista
    2 - Encontrar el máximo
    3 - Encontrar el mínimo
    4 - Filtrar por pares
    5 - Filtrar por impares
    6 - Agregar elementos
    7 - Eliminar elementos
    8 - Modificar elementos
    ''')

    try:
        opcion = int(input("Por favor ingrese una opción: "))
    except ValueError:
        print("Opción no válida. Ingresa un número del menú.")
        continue

    if opcion == 0:
        print("¡Hasta luego!")
        break
    elif opcion == 1:
        suma = sum(lista)
        print(f"La suma de los elementos es: {suma}")
    elif opcion == 2:
        maximo = max(lista)
        print(f"El máximo valor es: {maximo}")
    elif opcion == 3:
        minimo = min(lista)
        print(f"El mínimo valor es: {minimo}")
    elif opcion == 4:
        filtrados_pares = list(filter(lambda x: x % 2 == 0, lista))
        print(f"Elementos pares: {filtrados_pares}")
    elif opcion == 5:
        filtrados_impares = list(filter(lambda x: x % 2 != 0, lista))
        print(f"Elementos impares: {filtrados_impares}")
    elif opcion == 6:
        nuevo_elemento = int(input("Ingrese el nuevo elemento: "))
        lista.append(nuevo_elemento)
        print(f"Elemento {nuevo_elemento} agregado a la lista.")
    elif opcion == 7:
        elemento_a_eliminar = int(input("Ingrese el elemento a eliminar: "))
        if elemento_a_eliminar in lista:
            lista.remove(elemento_a_eliminar)
            print(f"Elemento {elemento_a_eliminar} eliminado de la lista.")
        else:
            print(f"El elemento {elemento_a_eliminar} no está en la lista.")
            
    elif opcion == 8:
        indice_modificar = int(input("Ingrese el índice del elemento a modificar: "))
        if 0 <= indice_modificar < len(lista):
            nuevo_valor = int(input("Ingrese el nuevo valor: "))
            lista[indice_modificar] = nuevo_valor
            print(f"Elemento en el índice {indice_modificar} modificado a {nuevo_valor}.")
            print(lista)
        else:
            print("Índice fuera de rango. Intente nuevamente.")
    else:
        print("Opción no válida. Intente nuevamente.")
