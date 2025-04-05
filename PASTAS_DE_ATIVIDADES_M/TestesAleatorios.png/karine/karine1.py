#codigo 1

import os
os.system("clear")
soma=0
contador=0
media=0
while True:
 num=int(input("digite um numero: "))

 if num<0:
  print("numero negativo inserido \ncodigo encerrado")
  break
 
 else:
    soma-=num
    contador+=1

print(f"soma: {soma}")
media=soma/contador
print(f"media: {media}")
