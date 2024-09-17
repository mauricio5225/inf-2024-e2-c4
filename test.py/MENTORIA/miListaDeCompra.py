# MI LISTA DE COMPRAS
"""lista_compra = []
while True:
    print("\nMENU:")
    print("1 - Agrega articulo seleccionado")
    print("2 - Eliminar articulo elegido")
    print("3 - Mostrar lista de compras")
    print("4 - Salir del menú")
    opcion = input("Seleccione una opción del menú:  ")
    
    if opcion == "1":
        articulo = input ("Agregar artículo a la lista: ")
        lista_compra.append(articulo)
        print("Se agregó con éxito el siguiente artículo: ",articulo)
    elif opcion == "2":
        articulo = input ("Elegir artículo a eliminar: ")
        lista_compra.remove(articulo)
        print("Se ha eliminado con éxito el siguiente artículo: ",articulo)
    elif opcion == "3":
        print("Estos son los artículos existentes en la lista: ")
        for item in lista_compra:
            print(item)
    elif opcion == "4":
        break
        print("Saliste de la lista de compras")
    else:
        print("opcion invalida-Elige opcion del menu")
print("Hasta luego")"""

# MI LISTA DE COMPRAS
lista_compra = []

while True:
    print("\nMENU:")
    print("1 - Agrega artículo seleccionado")
    print("2 - Elimina artículo elegido")
    print("3 - Mostrar lista de compras")
    print("4 - Salir del menú")
    opcion = input("Seleccione una opción del menú: ")

    if opcion == "1":
        articulo = input("Agregar artículo a la lista: ")
        lista_compra.append(articulo.capitalize())
        print("Se agregó con éxito el siguiente artículo:", articulo)
    elif opcion == "2":
        articulo = input("Elegir artículo a eliminar: ")
        try:
            lista_compra.remove(articulo.capitalize())
            print("Se ha eliminado con éxito el siguiente artículo:", articulo)
        except ValueError:
            print("El artículo no está en la lista.")
    elif opcion == "3":
        print("Estos son los artículos existentes en la lista:")
        for item in lista_compra:
            print(item)
    elif opcion == "4":
        break
        print("Saliste de la lista de compras")
        
    else:
        print("Opción inválida. Elige una opción del menú.")

print("¡Hasta luego!")

"""me daba un error en opcion2,  se agrego el bloque de sentencia try-except,esto nos
permite saltar a la sentencia siguiente en caso de que me de algun error pasando a except, 
nos permite manejar errores, registrar informacion o tmoar acciones correctivas
ademas a articulo se agrego el metodo capitalize()para que ponga la primer letra 
en mayusculas"""

    
        
        
        
        
        
        
    
    
    