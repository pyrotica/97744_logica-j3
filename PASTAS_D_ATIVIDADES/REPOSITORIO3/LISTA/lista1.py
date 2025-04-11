import os
os.system("cls || clear")

#declarando listas
lista1=[]
lista2=[]
lista3=[]

for i in range(4):
    num=int(input(f"digite o {1+i}º numero: "))
    #multiplicando por 2, deixando ao quadrado e adicionando em cada tabela
    lista1.append(num)
    multinum=num*2
    lista2.append(multinum)
    quadnum=num*num
    lista3.append(quadnum)


# declarar os primeiros e segundos numeros de cada lista
pri_numero1=lista1[0]
seg_numero1=lista1[1]
pri_numero2=lista2[0]
seg_numero2=lista2[1]
pri_numero3=lista3[0]
seg_numero3=lista3[1]
tamanho1= len(lista1)
tamanho2= len(lista2)
tamanho3= len(lista3)
#imprimindo o tamanho das listas
print(f"o tamanho da lista 1 é: {tamanho1}")
print()
print(f"o tamanho da lista 2 é: {tamanho2}")
print()
print(f"o tamanho da lista 3 é: {tamanho3}")
print()
print()
#imprimindo os primeiros e segundos numeros de cada lista
print(f"o primeiro numero da lista 1 é {pri_numero1}")
print()
print(f"o segundo numero da lista 1 é {seg_numero1}")
print()
print(f"o primeiro numero da lista 2 é {pri_numero2}")
print()
print(f"o segundo numero da lista 2 é {seg_numero2}")
print()
print(f"o primeiro numero da lista 3 é {pri_numero3}")
print()
print(f"o segundo numero da lista 3 é {seg_numero3}")
print()
print()
#imprimindo as listas
print(lista1)
print()
print(lista2)
print()
print(lista3)