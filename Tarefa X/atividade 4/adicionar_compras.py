def adicionar():
    lista=[]
    while True:
        compra=input("digite sua compra(digite sair para encerrar):")
        if compra=="sair":
            break
        lista.append(compra)
    return lista