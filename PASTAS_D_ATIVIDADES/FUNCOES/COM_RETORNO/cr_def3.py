
import os
os.system("cls || clear")


def somar(x, y): 
    return x+y

n1=int(input("Digite o primeiro numero: "))
n2=int(input("Digite o segundo numero: "))

soma=somar(n1,n2)
media=soma/2
print(f"Media: {media:.2f}")