import os
os.system("clear")

num1=float(input("digite o primeiro numero: "))
num2=float(input("digite o segundo numero: "))

soma=(num1 + num2)

media=(soma)/2

produto=(num1 * num2)

print()

maior=max(num1, num2)
menor=min(num1, num2)

print()
print(f"a soma é: {soma}")
print()
print(f"a media é: {media}")
print()
print(f"o produto é: {produto}")
print(f"o maior numero é: {maior}")
print()
print(f"o menor numero é: {menor}")
print()