import os
os.system("cls || clear")


while True:
    print("Digite um numero (num1) que seja o dobro de (num2)")
    num2=float(input("(num2) digite um numero: "))
    num1=float(input("(num1) digite um numero: "))


    if num1 == (num2*2):
        print(f"{num1} é o dobro de {num2}, fim do codigo")
        break
     
    else:
        print(f"{num1} não é o dobro de {num2}")
print()


while True:
    print("Digite um numero (num3) que seja a metade de (num4)")
    num3=float(input("(num3) digite um numero: "))
    num4=float(input("(num4) digite um numero: "))


    if num3 == (num4/2):
        print(f"{num3} é a metade de {num4}, fim do codigo")
        break
     
    else:
        print(f"{num3} não é a metade de {num4}")
print()

