#codigo 2

import os
os.system("clear")

contador=0
soma=0
while True:
 num=int(input("digite um numero: "))
print()
 if num<0:
  print("numero negativo inserido \ncodigo encerrado")
  break
 
 else:
    soma+=num
    contador+=1

print(f"soma: {soma}")
media=soma/contador