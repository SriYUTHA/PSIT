"""Difference()"""
def difference():
    """Print setA - setB"""
    numa = int(input())
    numb = int(input())
    lista = []
    listb = []
    for i in range(numa):
        seta = int(input())
        lista.append(seta)
    for i in range(numb):
        setb = int(input())
        listb.append(setb)
    for i in listb:
        if i in lista:
            lista.remove(i)
    lista.sort()
    for i in lista:
        print(i, end=' ')
difference()
