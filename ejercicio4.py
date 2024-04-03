#se importa la libreria Counter de la libreria collections para contar las letras de un string
from collections import Counter

def palindrome_reorder(palindromo):
    lettercount = Counter(palindromo)
    print(lettercount)
    #verifica cuantas letras impares hay en el palindromo
    impares = sum(1 for count in lettercount.values() if count % 2 != 0)
    print(impares)
    #El palindromo debe tener una longitud mayor a 1 y menor a 10^6
    if not (1 <= len(palindromo) <= 10**6): 
        return "NO SOLUTION"
    #no puede tener mas de 1 letra impar
    if impares > 1:
        return "NO SOLUTION"
    
    result = []
    #middle_char es el caracter impar que se destinara al medio de el palindromo
    middle_char = ''
    #se recorre el diccionario de letras y se obtiene la cantidad de veces que se repite
    for char, count in lettercount.items():
        #si la cantidad de veces que se repite es impar se guarda el caracter
        if count % 2 != 0:
            middle_char = char
        result.append(char * (count // 2))
    #ordeno los valores de forma que el resultado queda en espejo y el caracter impar queda al medio para lograr el palindromo
    return ''.join(result) + middle_char + ''.join(result[::-1])

assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"

print(palindrome_reorder("acajcaacjcababc"))
