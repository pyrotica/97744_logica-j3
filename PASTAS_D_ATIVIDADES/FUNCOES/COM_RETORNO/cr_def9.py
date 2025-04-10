import os
os.system("cls || clear")

soma=0
contador=0
def media_calc(): 
    media=soma/contador
    return media



for i in range(2):
 n1=int(input(f"Digite o {1+i}º numero: "))
 print()
 soma+=n1
 contador+=1

media=media_calc()
print(f"Media: {media:.2f}")
if media >=7:
          print()
          print("______________aprovado______________")
          print()
else:
          print("______________reprovado______________")
          print()
