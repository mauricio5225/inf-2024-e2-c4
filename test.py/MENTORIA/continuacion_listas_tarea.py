"""Funciones de listas:
        Usa la función len() para obtener la longitud de una lista."""
        
lista1=[1, 10, 20, 2, 50, 70,"mauro", 4, 5, 6, 7, 9, 10, 50]
lista=[1, 10, 20, 2, 50, 70, 4, 5, 6, 7, 9, 10, 50]
lista_orden=len(lista1)
print (lista_orden)

        
#Usa la función in para verificar si un elemento está en una lista.

lista1=[1, 10, 20, 2, 50, 70,"mauro", 4, 5, 6, 7, 9, 10, 50]
#busco verificar el string mauro en la lista
x="mauro"
if x in lista1:
        print(f"el elemento {x} se encuentra en la lista")
else:
        print(f"{x} no se encuentra en la lista")    

        #Usa la función index() para encontrar la posición de un elemento en una lista.
lista1=[1, 10, 20, 2, 50, 70,"mauro", 4, 5, 6, 7, 9, 10,"comision", 50]

x = lista1.index("comision")

if "comision" in lista1:
    print(f"el elemnto comision se encuentra en el indice {x} de la  lista")        
else:
    print(f"el elemento comision no se encuentra como indice {x}  en la lista") 
           
        #Usa la función append() para agregar un elemento al final de una lista.
lista1=[1, 10, 20, 2, 50, 70,"mauro", 4, 5, 6, 7, 9, 10,"comision", 50]
lista1.append("info")
print(lista1)

#Usa la función insert() para insertar un elemento en una posición específica de una lista.
        
lista1=[1, 10, 20, 2, 50, 70,"mauro", 4, 5, 6, 7, 9, 10,"comision", 50] 
lista1.insert(5,"clase") 
print(lista1)

      
 #Usa la función remove() para eliminar un elemento de una lista por su valor.
lista1=[1, 10, 20, 2, 50, 70,"mauro", 4, 5, 6, 7, 9, 10,"comision", 50] 
lista1.remove("mauro")
print(lista1)
        
        #Usa la función pop() para eliminar un elemento de una lista por su índice y obtenerlo de vuelta.
lista1=[1, 10, 20, 2, 50, 70,"mauro", 4, 5, 6, 7, 9, 10,"comision", 50]   
elementoAEliniminar = lista1.pop(13)
print(lista1)
     
        
        #Usa la función sort() para ordenar los elementos de una lista.
        
lista1=[1, 10, 20, 2, 50, 70,"mauro", 4, 5, 6, 7, 9, 10,"comision", 50]        
        #Usa la función reverse() para invertir el orden de los elementos de una lista.
lista1=[1, 10, 20, 2, 50, 70,"mauro", 4, 5, 6, 7, 9, 10,"comision", 50]    
lista_reversa= lista1.reverse()
print(lista1)       
        
        #Usa la función copy() para copiar una lista."""
lista1=[1, 10, 20, 2, 50, 70,"mauro", 4, 5, 6, 7, 9, 10,"comision", 50] 
nueva_lista1= lista1.copy()
print(nueva_lista1)        

#Listas anidadas:
 #       Crea una lista de listas.""""
lista =[[1,2,3],[5,6,7],["INFO"]]
print(lista)

#agrego sublista a lista
lista.append([20,"comision"])
print(lista)

#Accede a elementos de listas anidadas.
lista_anidada = [[1, 2, 3], [5, 6, 7], ['INFO'], [20, 'comision']]
# accedo a la sublista 1
sublista_1 = lista_anidada[1]
print(sublista_1)

#Modifica elementos de listas anidadas."""

lista_anidada = [[1, 2, 3], [5, 6, 7], ['INFO'], [20, 'comision']]
sublista_3=lista_anidada[3]
sublista_3.append(4)
print(lista_anidada)