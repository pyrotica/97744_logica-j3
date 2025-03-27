import os
os.system("clear")

def BubbleSport(lista):
    tamanho = len(lista)
    for i in range(tamanho):
       for j in range(0, tamanho - i - 1):
         if lista[j]>lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[1]
    return lista

lista = [2,12,3,0,8,90,69]
lista_ordenada = BubbleSport(lista)
print(f"Lista ordenada: {lista_ordenada}")