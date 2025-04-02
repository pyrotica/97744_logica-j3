import os
os.system("cls || clear")
soma=0
contador=0
while True:
    num=int(input("digite um numero: "))

    soma += num
    contador += 1
    if num <0:
        print(f"{num} é um Numero negativo, codigo encerrado") 
        break
    elif num == 0:
     print("zero")
    else:
        print("numero positivo")
print()
media=(soma)/contador
print(f"A soma é {soma}")
print(f"A media é {media:.2f}")
