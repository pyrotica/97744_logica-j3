import os
os.system("cls || clear")

contador=0
soma=0
while True:
    num=int(input("digite um numero: "))
    continuacao=str(input("deseja coninuar? \n: ")).lower()
    soma += num
    contador += 1
    if continuacao =="n":
       print("parou")
       print()
       break

    
media=(num)/contador

print(f"A quantidade de repetição é {contador}")
print(f"A soma é {soma}")
print(f"A media é {media:.2f}")