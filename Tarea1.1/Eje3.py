##Eliminar elementos repetidos de una lista

elementos = [33,64,23,1,45,5,72,7,4,1,23,33,64]
elementosOrdenados = []

def eliminaRepetidos(lista):
    for elemento in lista:
        if elemento not in elementosOrdenados:
            elementosOrdenados.append(elemento)
    return sorted(elementosOrdenados)

print(eliminaRepetidos(elementos))