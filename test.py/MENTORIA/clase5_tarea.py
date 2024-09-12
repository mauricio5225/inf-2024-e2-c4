"""Crea una lista a partir de otra lista.
Acceso a elementos:
        Obtén el primer elemento de una lista.
        Obtén el último elemento de una lista.
        Obtén un elemento específico de una lista por su índice.
        Obtén un subconjunto de una lista (slicing).

Modificación de listas:
        Agrega un elemento al final de una lista.
        Inserta un elemento en una posición específica de una lista.
        Elimina un elemento de una lista por su índice.
        Remplaza un elemento de una lista por otro.

Operaciones con listas:
        Une dos listas.
        Verifica si un elemento está en una lista.
        Obtén la longitud de una lista.
        Invierte el orden de los elementos de una lista.
        Ordena los elementos de una lista."""
        
#lista ejercicio de tarea clase 5
lista = [1,10,20,2 ,3,4, 5,6,7,8,9,10]
nueva_lista = list(lista)
print(nueva_lista)
print(nueva_lista[0])
print(nueva_lista[-1])

elemento_esp = nueva_lista[2]
print(elemento_esp)

print(nueva_lista[2:7])
#modificacion de listas
lista = [1,10,20,2 ,3,4, 5,6,7,8,9,10]
#agrego un numero al final de la lista
lista.append(50)
print(lista)
#agregar un elem. en una posic esp de una lista, en 5
lista.insert(5,70)
print(lista)
#elimina un elemento de la lista por medio de un indice
lista.pop(10)
print(lista)
#Remplaza un elemento de una lista por otro.
lista[4]=50
print(lista)
#OPERACIONES CON LISTAS
#UNIR 2 LISTAS
lista1= [1,2,3,4,5,6]
lista2= [10,"COMISION_4","INFOR",'a']
nueva_lista= lista1+lista2
print(nueva_lista)
#Verifica si un elemento está en una lista, por ejemplo "comision 4"
verificar= "COMISION_4" in nueva_lista
print (verificar)    
# Obtén la longitud de una lista.
long = len(nueva_lista)
print(long)
#Invierte el orden de los elementos de una lista.
nueva_lista = [1, 2, 3, 4, 5, 6, 10, 'COMISION_4', 'INFOR', 'a']
nueva_lista.reverse()
print(nueva_lista) 
# Ordena los elementos de una lista.

nueva_lista = [5, 7, 1, 2, 9, 6, 3, 'COMISION_4', 'INFOR', 'A']

"""help, como se resuelve esto: una lista con strings y enteroes"""              

lista = [1,10,20,2 ,3,4, 5,6,7,8,9,10]
lista.sort()
print(lista)

lista_ordenada= sorted(lista)
print (lista)
print(lista_ordenada)




