##Calcular el numero maximo de un arreglo sin usar .max()

numeros = [34,23,5,2,5,98]

def numMayor(lista):
    ordenados = sorted(lista, reverse=True)
    mayor = ordenados[0]
    return mayor

print(numMayor(numeros))

