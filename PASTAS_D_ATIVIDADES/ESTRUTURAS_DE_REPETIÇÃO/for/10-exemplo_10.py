import os
os.system('cls || clear')


print()
soma = 0
for i in range(4):
    num1=int(input("Digite numero: "))
    soma += num1
print(f"A soma total é: {soma}")
    
media=(soma)/4

print(f"A media total é: {media}")