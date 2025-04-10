
import os
os.system("cls || clear")


def media_calc(x, y): 
    soma=x+y
    media=soma/2
    return media

n1=int(input("Digite o primeiro numero: "))
n2=int(input("Digite o segundo numero: "))

media=media_calc(n1,n2)
print(f"soma: {n1+n2}")
print(f"Media: {media:.2f}")