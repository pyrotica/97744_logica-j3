import os
os.system("clear")

num1=float(input("digite o primeiro numero: "))
num2=float(input("digite o segundo numero: "))

soma=(num1 + num2)

media=(soma)/2

produto=(num1 * num2)

print()

if num1 > num2:
    print(f"{num2} é menor que {num1}")

elif num1 == num2:
    print(f"{num1} é igual a {num2}")

else:
    print(f"{num1} é menor que {num2}")

print()
print(f"a soma é: {soma}")
print()
print(f"a media é: {media}")
print()
print(f"o produto é: {produto}")