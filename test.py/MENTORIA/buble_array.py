# Defino la función de ordenamiento
def bubbleSort(array):
    length = len(array)
    print(length)
    
    # Bucle para pasadas
    for i in range(length):
        print(f"pasada #{i+1}")
        
        # Comparaciones e intercambios
        for j in range(0, length - i - 1):
            print(f"comparacion: {array[j]} > {array[j+1]}")
            if array[j] > array[j+1]:
                print(f"intercambiar: {array[j]} x {array[j+1]}")
                aux = array[j]
                array[j] = array[j+1]
                array[j+1] = aux
        print(f"lista:  {array}")
    return array

scores = [70, 90, 0, 80, 60, 85]
print("Antes de ordenar: ")
print(scores)
print("Después de ordenar:")
print(bubbleSort(scores))



