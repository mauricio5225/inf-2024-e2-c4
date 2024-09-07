# Calculadora
# Opciones:
# 1 - Sumar todos los elementos de una lista
# 2 - Encontrar el maximo
# 3 - Encontrar el minimo
# 4 - Filtrar por pares
# 5 - Filtrar por impares
### Ingrese los valores de la lista por pantalla, y ademas la lista puede tener cualquier tamanio
# input()

lista = [32,1,2,3,4,5,65]
condicion = 'si'
# while condicion == 'si':
#     numero = input("Ingresar valor para la lista: ")
#     numero = int(numero)
#     lista.append(numero)
#     condicion = input("Desea seguir cargando valores? (si/no)")

print("Su lista cargada es la siguiente:", lista)

opcion = None
while opcion!= 0:

    print(f'''
    0 - Salir
    1 - Sumar todos los elementos de una lista
    2 - Encontrar el maximo
    3 - Encontrar el minimo
    4 - Filtrar por pares
    5 - Filtrar por impares
    6 - Agregar elementos
    7 - Eliminar elementos
    8 - Modificar elementos
    ''')
    opcion = int(input("Por favor ingrese una opcion: "))

    if opcion == 1:
        suma = sum(lista)
        print(suma)
    elif opcion == 2:
        maximo = max(lista)
        print(maximo)
    elif opcion == 3:
        minimo = min(lista)
        print(minimo)
    elif opcion == 4:
        filtradPar = list(filter(lambda x: x % 2 == 0, lista))
        print(filtradPar)
    elif opcion == 5:
        filtradoImpar = list(filter(lambda x: x % 2 != 0, lista))
        print(filtradoImpar)
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
                
    else:
        print("su opcion no esta definida dentro de los limites de las opciones")
    
        
        
        
