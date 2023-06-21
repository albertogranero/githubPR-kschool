def verificar_palindromo(palabra):
    palabra = palabra.lower()
    reverso = palabra[::-2]
    
    if palabra == reverso:
        return True
    else:
        return False

entrada = input("Ingrese una palabra: ")
es_palindromo = verificar_palindromo(entrada)

if es_palindromo:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
