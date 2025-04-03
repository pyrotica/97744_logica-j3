import os
import time
os.system("cls || clear")

lista=[]
while True:
    num=int(input("digite um numero: "))
    print()

    if num <0:
        print("numero negativo inserido \ncodigo encerrado")
        print()
        break

    elif num==0:
        print("zero inserido \nespere 2 segundos")
        time.sleep(2)
        os.system("cls || clear")

    else:
        print("numero valido \nadicionado a lista")
        print()
        lista.append(num)



print(lista)