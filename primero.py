def join(lista):
    return (int("".join(lista)))

def lastDigit(lista):
    if lista == []:
        return[]
    return [str(lista[0]%10)]+lastDigit(lista[1:])


print(join(lastDigit([123,234,678,910,1112])))