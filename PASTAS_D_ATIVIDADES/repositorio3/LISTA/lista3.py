import os
os.system("clear")
import time
soma=0
contador=0
lista=[]

while True:
 num=int(input(f"digite o um numero: "))
 
 if num<0:
  print("numero negativo")
  time.sleep(2)
  os.system("clear")


  break


 else:
  os.system("clear")

  lista.append(num)
  contador+=1

tamanho=len(lista)
# lista.remove(lista[1])
soma=sum(lista)
print(f"soma: {soma}")
print(f"a primeira nota foi: {lista[0]}")
print(f"lista: {lista}")
print(f"tamanho da lista: {tamanho}")
print(f"quantidade de repetições: {contador}")