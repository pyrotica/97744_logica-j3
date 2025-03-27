import os
os.system("clear")

idade=int(input("digite a idade: "))


if idade >=18 and idade <=65:
    print(" é obrigado a votar--")
elif idade == 16 or idade == 17:
    print("voto opicional")
else:
    print("--nao é obrigado a votar--")
