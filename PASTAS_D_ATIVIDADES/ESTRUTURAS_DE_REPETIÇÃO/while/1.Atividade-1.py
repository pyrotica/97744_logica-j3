import os
os.system("cls || clear")


while True:
    num=int(input("digite um numero: "))

    if num <0:
        print(f"{num} é um Numero negativo, codigo encerrado")
        break
    elif num == 0:
     print("zero")
    else:
        print("numero positivo")
print()

