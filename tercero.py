def listar(lista):
    if lista ==[]:
        return []
    return [(maximo(lista[0]) , minimo(lista[0]) , (maximo(lista[0]) + minimo(lista[0]))) ] + listar(lista[1:])

def maximo(lista):
    return max(lista)

def minimo(lista):
    return min(lista)

print(listar([[1,2,3,4,5],[6,7,8,9],[10,11,12]]))