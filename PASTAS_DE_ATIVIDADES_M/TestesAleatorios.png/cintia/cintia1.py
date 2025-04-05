#codigo 1

import os
os.system("clear")


while True:
 num=int(input("digite um numero: "))

 if num<0:
  print("numero negativo inserido \ncodigo encerrado")
  break
 
 else:
    soma+=num

print(f"soma: {soma}")