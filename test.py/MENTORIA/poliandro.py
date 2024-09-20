def es_palindromo(texto):
    # Convertir el texto a minúsculas y eliminar espacios
    texto = texto.lower().replace(" ", "")
    # Comparar el texto con su reverso
    return texto == texto[::-1]

# Solicitar al usuario que ingrese una palabra o frase
entrada = input("Ingrese una palabra o frase: ")

# Verificar si es un palíndromo
if es_palindromo(entrada):
    print(f'"{entrada}" es un palíndromo.')
else:
    print(f'"{entrada}" no es un palíndromo.')
