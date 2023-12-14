from remover_duplicados import remover
from mostrar_lista import mostrar

if __name__=="__main__":
    lista=[1,2,2,3,4,5,5,6,7,8,8,9,10,10]
    lista=remover(lista)
    mostrar(lista)