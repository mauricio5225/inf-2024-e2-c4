#funciones

def obtener_pares(lista_numeros):
    return [num for num in lista_numeros if num % 2 == 0]

numeros= [1,2,3,4,5,6,7,8,9,10,11]
pares = obtener_pares(numeros)
print(pares)

mi_lista=[23,35,659,465,6,1,67,89,92,36,44,55,26]
par=obtener_pares(mi_lista)
print(par)

#diccionario
def longitud_palabras(lista_palabras):
    return {palabra: len(palabra) for palabra in lista_palabras}

# Ejemplo de uso
lista = ["hola", "mundo", "Python", "programación"]
resultado = longitud_palabras(lista)
print(resultado)

#EJ MENTORIA

def dictPalabras(listaPalabras):
    diccionario={}
    for palabra in listaPalabras:
        longitud=len(palabra)
        diccionario[palabra] = longitud
        

# tupla - escribir una fincion que tome una tupla de tuplas y devuelva una lista plana con todoslos elementos
#ejemplo en clase

tuplaDeNumeros=((5,89,34),(6,34,2),(67,455,33),(1,3,55,55))

listaDeLaTuplaDeNumeros=(5,89,34,6,34,2,67,455,33,1,3,55,55)
def listaPlana(tuplaDeTuplas):
    lista=[]
    for tupla in tuplaDeTuplas:
        for elemento in tupla:
            lista.append(elemento)
    return lista
print(listaPlana(tuplaDeNumeros))
            
    



def suma_tupla(numeros):
    return sum(numeros)

# Ejemplo de uso
tupla_numeros = (1, 2, 3, 4, 5)
resultado = suma_tupla(tupla_numeros)
print(resultado)

# tupla de tupla
def tupla_a_lista(tuplas):
    lista_plana = []
    for tupla in tuplas:
        for elemento in tupla:
            lista_plana.append(elemento)
    return lista_plana

# Ejemplo de uso-convierte una tupla a lista
tuplas = ((1, 2), (3, 4), (5, 6))
resultado = tupla_a_lista(tuplas)
print(resultado)

