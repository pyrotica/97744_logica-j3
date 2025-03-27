import os
os.system("clear")

nota1=float(input("digite a primeira nota: "))
nota2=float(input("digite a segunda nota: "))
nota3=float(input("digite a terceira nota: "))

soma=(nota1 + nota2 +nota3)

media=(soma)/3

if media >= 7:
    print("aprovado")

else:
    print("reprovado")

print(f"media de fulano é: {media}")