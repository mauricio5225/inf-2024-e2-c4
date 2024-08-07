# Ordenamiento por seleccion (sort)

def seleccion(lista_desordenada):
    n = len(lista_desordenada)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista_desordenada[j] < lista_desordenada[min_idx]:
                min_idx = j
        lista_desordenada[i], lista_desordenada[min_idx] = lista_desordenada[min_idx], lista_desordenada[i]
    return lista_desordenada

# Ejemplo de uso (uso de sorted)
lista = [64, 25, 12, 22, 11]
print(seleccion(lista))

# 2. Ordenamiento por Inserción
def insercion(lista_desordenada):
    for i in range(1, len(lista_desordenada)):
        key = lista_desordenada[i]
        j = i - 1
        while j >= 0 and key < lista_desordenada[j]:
            lista_desordenada[j + 1] = lista_desordenada[j]
            j -= 1
        lista_desordenada[j + 1] = key
    return lista_desordenada

# Ejemplo de uso
lista = [12, 11, 13, 5, 6]
print(insercion(lista))

# 3. Ordenamiento por Intercambio (Bubble Sort)
def intercambio(lista_desordenada):
    n = len(lista_desordenada)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_desordenada[j] > lista_desordenada[j+1]:
                lista_desordenada[j], lista_desordenada[j+1] = lista_desordenada[j+1], lista_desordenada[j]
    return lista_desordenada

# Ejemplo de uso
lista = [64, 34, 25, 12, 22,1000, 11, 90]
print(intercambio(lista))
   
