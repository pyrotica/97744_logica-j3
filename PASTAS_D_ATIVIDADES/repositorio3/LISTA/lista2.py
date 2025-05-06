import os
import time
os.system("cls || clear")

soma=0
lista=[]

while True:
    num=int(input("\ndigite um numero: "))
    print()

    if num <0:
        print("\nnumero negativo inserido \ncodigo encerrado")
        time.sleep(1.5)
        os.system("cls || clear")
        break

    elif num==0:
        print("\nzero inserido \nespere 2 segundos")
        time.sleep(2)
        os.system("cls || clear")

    else:
        print("\nnumero valido \nadicionado a lista")
        soma+=num
        lista.append(num)


print("\t===IMPRESSÃO===")
print(f"\nlista final:\t{lista}")
print(f"\nsoma da lista:\t({soma})")