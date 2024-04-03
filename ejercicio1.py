def weird_algorithm(number):
    numlist = [number]
    #la funcion se ejecuta mientras el numero sea diferente de 1
    #while number != 1: # cambio de condicion despues de leer bien la consigna xD
    #la funcion se ejecuta mientras el numero sea mayor a 1 y menor a 10^6
    while number > 1 and number < 10**6:
        #divide al numero entre 2 si es par y si no lo multiplica por 3 y le suma 1
        number = number // 2 if number % 2 == 0 else 3 * number + 1
        #agrega el numero a la lista
        numlist.append(number)
    return numlist
number = int(input("ingrese un numero: "))
#caso de prueba
assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"

test = weird_algorithm(number)
print(test)
print("todo se ejecuto de manera correcta")