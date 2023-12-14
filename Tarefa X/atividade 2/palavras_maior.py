def maior(lista, nova_lista):
    for palavra in lista:
        if palavra>=5:
            nova_lista.append(palavra)
    return nova_lista