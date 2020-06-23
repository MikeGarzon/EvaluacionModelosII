#Codigo del profe--------------------------------
class Nodo():
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

def en_orden(arbol):
    if (arbol == None):
        return []
    return en_orden(arbol.izquierda) + [arbol.valor] + en_orden(arbol.derecha)
#---------------------------------------------------------

def digitos(num):
    return [int(x) for x in str(num)]

def arbol(lista):
    if lista == []:
        return []
    return [digitos(lista[0])] + arbol(lista[1:])

print(arbol(en_orden(Nodo(25, Nodo(5, None, Nodo(10)), Nodo(75)))))
