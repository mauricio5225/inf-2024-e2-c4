# Crear una lista vacía para almacenar los artículos
"""
lista_compras = []

def agregar_articulo():
    articulo = input("Agrega un artículo: ")
    lista_compras.append(articulo.capitalize())
    print("Artículo agregado con éxito.")

def borrar_articulo():
    articulo = input("Ingresa el artículo a eliminar: ")
    try:
        lista_compras.remove(articulo.capitalize())
        print("Artículo eliminado con éxito.")
    except ValueError:
        print("El artículo no está en la lista.")

def ver_lista():
    print("\nArtículos en tu lista:")
    for item in lista_compras:
        print(item)

while True:
    print("\nMenú:")
    print("1. Agregar artículo")
    print("2. Eliminar artículo")
    print("3. Ver lista")
    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == "1":
        agregar_articulo()
    elif opcion == "2":
        borrar_articulo()
    elif opcion == "3":
        ver_lista()
    else:
        print("Opción inválida. Inténtalo nuevamente.")"""
        
        
        # Crear una lista vacía para almacenar los artículos
lista_compras = []

while True:
    print("\nMenú:")
    print("1. Agregar artículo")
    print("2. Eliminar artículo")
    print("3. Ver lista")
    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == "1":
        articulo = input("Agrega un artículo: ")
        lista_compras.append(articulo.capitalize())
        print("Artículo agregado con éxito.")
    elif opcion == "2":
        articulo = input("Ingresa el artículo a eliminar: ")
        try:
            lista_compras.remove(articulo.capitalize())
            print("Artículo eliminado con éxito.")
        except ValueError:
            print("El artículo no está en la lista.")
    elif opcion == "3":
        print("\nArtículos en tu lista:")
        for item in lista_compras:
            print(item)
    else:
        print("Opción inválida. Inténtalo nuevamente.")

