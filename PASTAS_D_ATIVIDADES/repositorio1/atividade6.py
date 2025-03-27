#maior=max(num1, num2)
#menor=min(num1, num2)

import os

os.system("clear")

num1=int(input("digite o primeiro numero: "))
num2=int(input("digite o segundo numero: "))
num3=int(input("digite o terceiro numero: "))

maior=max(num1, num2, num3)
menor=min(num1, num2, num3)

print(f"os numeros ecolhidos são: {num1}, o {num2} e o {num3}")
print()
print(f'o maior numero é: {maior}, e o menor é: {menor}')