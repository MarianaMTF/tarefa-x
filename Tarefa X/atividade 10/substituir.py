def substituir(lista):
    for i in lista:
        if i%2==0:
            lista[i]=0
    for i in lista:
        print(i)