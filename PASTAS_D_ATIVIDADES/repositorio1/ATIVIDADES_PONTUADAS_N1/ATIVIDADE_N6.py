import os
os.system("clear")

nota1=int(input("digite a primeira nota: "))
nota2=int(input("digite a segunda nota: "))

total=(nota1 + nota2)

media=(total)/2

if media >=6:
    print("aprovado")

elif media <= 4:
    print("reprovado")

