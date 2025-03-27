import os
os.system('cls || clear')


soma = 0
for i in range(4):
    num1=int(input("Digite numero: "))
    soma += num1
print()
print(f"A soma total das notas é: {soma}")
print()    
media=(soma)/4

print(f"A media total das notas é: {media}")
print()

if media >=7:
    print("______________aprovado______________")

elif media <=4:
    print("______________reprovado______________")

else:
    print("______________recuperação______________")