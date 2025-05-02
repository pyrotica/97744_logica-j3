# import os
# os.system("clear")

# def BubbleSport(lista):
#     tamanho = len(lista)
#     for i in range(tamanho):
#        for j in range(0, tamanho - i - 1):
#          if lista[j]>lista[j+1]:
#                 lista[j], lista[j+1] = lista[j+1], lista[1]
#     return lista

# lista = [2,12,3,0,8,90,69]
# lista_ordenada = BubbleSport(lista)
# print(f"Lista ordenada: {lista_ordenada}")

import os

# Limpar a tela
os.system("clear")
QUANT=int(input("digite a quantidade de numeros na lista: "))
os.system("clear")

# Função de ordenação Bubble Sort
def BubbleSort(lista):
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(0, tamanho - i - 1):
            if lista[j] > lista[j + 1]:
                # Trocar os elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Lista a ser ordenada
lista = []
for i in range(QUANT):
    num=int(input(f"digite o {1+i}º da lista: "))
    lista.append(num)
    os.system("clear")


# Ordenar a lista
lista_ordenada = BubbleSort(lista)

# Exibir a lista ordenada
print(f"Lista ordenada: {lista_ordenada}")