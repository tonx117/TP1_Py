def number_spiral(fila, columna):
    #se obtiene el maximo entre la fila y la columna
    maximo = max(fila, columna)
    #se obtiene el valor de la diagonal del cuadrante
    diagonal = (maximo - 1) ** 2
    #se verifica si el maximo es par o impar
    if maximo % 2 == 0:
        #se devuelve el valor de la diagonal mas la fila si el maximo es igual a la columna y 
        #si no se devuelve el valor de la diagonal mas 2 veces el maximo menos la columna
        return diagonal + fila if maximo == columna else diagonal + 2 * maximo - columna
    else:
        #se devuelve el valor de la diagonal mas la columna si el maximo es igual a la fila y 
        #si no se devuelve el valor de la diagonal mas 2 veces el maximo menos la fila
        return diagonal + columna if maximo == fila else diagonal + 2 * maximo - fila



fila = int(input("Ingrese la posición de la fila: "))
columna = int(input("Ingrese la posición de la columna: "))

assert number_spiral(2, 2) == 3, "Error en el caso de prueba"

valor = number_spiral(fila, columna)
print("El valor en la posición (", fila, ",", columna, ") es:", valor)

