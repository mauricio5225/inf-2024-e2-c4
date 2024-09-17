
## CONJUNTO DE ACCIONES EMPAQUETADAS
# Funciones, f(x) = 2.x = Resultado
# Procedimiento, f(x) = 2.x = No tengo resultado

def f(x):
    return 2 * x

var_2 = f(2)
var_4 = f(4)

print(var_2)
print(var_4)

# Cohesion: El grado de relacion de los componentes internos
# del codigo. Objetivo: Alto.

# Entrada -> CajaNegra -> Resultado
def caja_negra(lista):
    return sorted(lista)

lista = [3,21,4,56,768,234135,685,53214,23,5,67,8,12]
print(caja_negra(lista))


def caja_negra(lista):
    lista.sort()  # Usar el método 'sort' de la lista
    return lista

lista = [3, 1, 4, 1, 5, 9]
print(caja_negra(lista))




def caja_negra(lista):
    return sorted(lista)
    

lista=[123,1568,54987,26454,21,1,5468,19487,79,23564
    ,6,546,41,5468,4878741]
print(caja_negra(lista))

#

## CONJUNTO DE ACCIONES EMPAQUETADAS
# Funciones, f(x) = 2.x = Resultado
# Procedimiento, f(x) = 2.x = No tengo resultado

def f(x):
    return 2 * x

var_2 = f(2)
var_4 = f(4)

print(var_2)
print(var_4)

# Cohesion: El grado de relacion de los componentes internos
# del codigo. Objetivo: Alto.

# Entrada -> CajaNegra -> Resultado
def caja_negra(lista):
    return sorted(lista)

lista = [3,21,4,56,768,234135,685,53214,23,5,67,8,12]
print(caja_negra(lista))

