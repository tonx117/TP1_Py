def missing_number(number,array):
    #se creo un conjunto con los numeros del 1 al numero dado
    numberset = set(range(1,number+1))
    #se creo un conjunto con los numeros de la lista
    numbersgiven = set(array)
    #se obtiene el numero faltante acorde a los conjuntos
    missing = numberset - numbersgiven
    #se obtiene el resultado ya que el metodo pop agarraria el valor restante del conjunto
    result = missing.pop() if missing else "No hay numeros que falten"
    print(result)
    return result

assert missing_number(5,[1,2,4,5]) == 3, "Error en el caso de prueba"

print("todo se ejecuto correctamente")