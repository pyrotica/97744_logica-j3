import os
os.system("cls || clear")


def somar(x, y):
    return x+y

def subt(x, y):
    return x-y

def multi(x, y):
    return x*y

def divi(x, y):
    return x/y

n1=int(input("Digite o primeiro numero: "))
n2=int(input("Digite o segundo numero: "))

soma=somar(n1,n2)
subtracao=subt(n1,n2)
multiplicacao=multi(n1,n2)
divisao=divi(n1,n2)
print()
print("\t===RESULTADO===")
print()
print(f"soma: {soma}")
print(f"subtração: {subtracao}")
print(f"multiplicação: {multiplicacao}")
print(f"divisão: {divisao:.2f}")










# def media(x, y):
#     calcular=soma/2
#     return calcular

# print(f"media: {media}")

# numeclatura=media(n1+n2)/2