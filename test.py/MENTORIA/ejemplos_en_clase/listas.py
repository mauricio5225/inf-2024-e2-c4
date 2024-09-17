lista_1 = ["mauro", 10, True]

lista_2 = ["diego", "ceci"," franco"]

lista_3 = ["un dato","pelota", lista_1, "otra lista", lista_2]

lista_4=['mauro', 10,345, ['diego', 'ceci', ' franco',"mauro y tere",345]]

print(lista_1, "\n")
print(lista_2, "\n")
print(lista_3, "\n")

print(lista_3[4])
#slicing
print(lista_3[1:4])

#reversa
print(lista_3[-2])
print(lista_3[-1])

#agrego elementos a la lista
lista_1[-1] = lista_2
print(lista_1)

#metodos
#append, se agrega un nuevo parametro al final de la lista
lista_1=['mauro', 10, ['diego', 'ceci', ' franco']]
print(lista_1,"\n")
lista_1.append("mauro y tere")
print(lista_1)

#remove(parametro)
lista_4=['mauro', 10,345, ['diego', 'ceci', ' franco',"mauro y tere",345]]
print(lista_4)
lista_4.remove(345)
print(lista_4)

#insert
lista_4=['mauro', 10, 345, ['diego', 'ceci', ' franco',"mauro y tere",345]]
print(lista_4)
lista_4.insert(3,"info")
print(lista_4)

#count(paramet)
lista_4=['mauro', 10, 345, ['diego', 'ceci', ' franco',"mauro y tere",345]]
print(lista_4)
conteo_345= lista_4.count(345)
print(conteo_345)

#index(parametro)

lista_4 = ['mauro', 10, 345, ['diego', 'ceci', ' franco',"mauro y tere",345]]
indice_mauro = lista_4.index('mauro')
print(f"el indice de 'mauro' en la lista principal es de:  {indice_mauro}")

# Buscar el índice de 'mauro' en la lista principal
lista_4 = ['mauro', 10, 345, ['diego', 'ceci', 'franco', "mauro y tere", 345]]
indice_mauro = lista_4.index('mauro')
print(f"El índice de 'mauro' en la lista principal es: {indice_mauro}")

#sort()
#lista_4 = ['mauro', 10, 345, ['diego', 'ceci', 'franco', "mauro y tere", 345]]
def key_func(element):
    if isinstance(element, int):
        return (0, element)  # Los enteros tienen prioridad más alta
    elif isinstance(element, str):
        return (1, element)  # Las cadenas tienen prioridad intermedia
    elif isinstance(element, bool):
        return (2, element)  # Los booleanos tienen prioridad más baja
    else:
        return (3, element)  # Otros tipos de datos (si los hubiera)
# Ordenamos por ejemplo la sublista en la posición 3 de lista_4
lista_3=sorted(lista_3,key=key_func)

print(lista_3)


