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

#crear una funcion que reciba un diccionario y devuelva una lista
#ordenada de las claves

diccionario={
    "c":0,
    "b":1,
    "e":4,
    "a":10
}

def listaDeClavesOrdenadas(diccionario:dict):
    listaDeClaves = diccionario.keys() #["c","b","e","a"]
    return sorted(listaDeClaves)
print(listaDeClavesOrdenadas(diccionario))
    
    
#escribir una funcion que imprima la tabla de multiplicar de un numero dado

def Tabla_de_multiplicar(numero, maximo):
    for i in range(0, maximo +1):
        print(f"{numero} x {i} = {numero * i}")
        
numero=int(input("ingrese un nuemro para visualizar su tabla de multiplicar: ")) 
maximo = int(input("ingrese el numero dmacimo de tabla:"))
Tabla_de_multiplicar(numero, maximo)

        
        
# crear una f que reciba una lista de diccionarios, cada uno representando a una persona
#con nombre y edad. la f debe devolver una lista ordenada de personas por edad

lista_de_nombre=[{"Rafael"}]

"""def ordenar_por_edad(lista_personas):
    return sorted(lista_personas, key=lambda persona: persona['edad'])

# Ejemplo de uso
personas = [
    {'nombre': 'Juan', 'edad': 25},
    {'nombre': 'Ana', 'edad': 20},
    {'nombre': 'Pedro', 'edad': 30}
]
personas_ordenadas = ordenar_por_edad(personas)
print(personas_ordenadas)"""


def obtener_edad(persona):
    return persona['edad']

def ordenar_por_edad(lista_personas):
    return sorted(lista_personas, key=obtener_edad)

# Ejemplo de uso
personas = [
    {'nombre': 'Juan', 'edad': 25},
    {'nombre': 'Ana', 'edad': 20},
    {'nombre': 'Pedro', 'edad': 30}
]
personas_ordenadas = ordenar_por_edad(personas)
print(personas_ordenadas)



