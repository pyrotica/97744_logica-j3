import os
os.system("cls || clear")


print()
while True:
    idade=int(input("digite a idade: "))
    if idade < 18:
        print("Acesso negado \nsomente maiores de 18\n")
        print()

    else:
       break
print("Acesso permitido")
