import os
os.system("cls || clear")

soma=0
quant=int(input("Digite a quantidade de numeros: "))
os.system("cls || clear")

def mediuacao():
    media=soma/quant
    return media

for i in range(quant):
    num=int(input(f"Digite o {1+i}º numero: "))
    soma+=num
    os.system("cls || clear")

media=mediuacao()
print(f"a soma dos numeros é: {soma}\na media é: {media}")
