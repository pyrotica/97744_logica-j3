import os
os.system("cls || clear")


while False:
    num=int(input("digite um numero: "))

    if num <0:
        print(f"{num} é um Numero negativo, codigo encerrado")
        
    elif num == 0:
     print("zero")
    else:
        print(f"{num} é um numero positivo")
    break