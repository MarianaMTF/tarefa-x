def remover(lista):
    lista_2=[]
    for i in lista:
        if i not in lista_2:
            lista_2.append(i)
    return lista_2