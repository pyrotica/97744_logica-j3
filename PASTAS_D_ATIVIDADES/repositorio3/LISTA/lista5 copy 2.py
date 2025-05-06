import os
os.system("clear")

lista=[]
QUANT=5

def maior_menor(lista):
   maior=max(lista)
   menor=min(lista)
   return maior, menor

def solicitar_dados():
 for i in range(QUANT):
  num=int(input(f"digite a {1+i}º nota: "))

  lista.append(num)
 return num

def mostar_dados():
 
 print("\t==========resultado==========\n")
 print(f"maior numero da lista: {maior}\n")
 print(f"menor numero da lista: {menor}\n")
 print("\t==========resultado==========")


solicitar_dados()
maior, menor = maior_menor(lista)
mostar_dados()