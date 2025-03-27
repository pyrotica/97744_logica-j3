import os
os.system("clear")

a=int(input("digite o primeiro numero: "))
b=int(input("digite o segundo numero: "))
c=int(input("digite o segundo numero: "))

soma=(a + b)

if soma < c:
    print(f"a soma de A e B ({soma}), é menor que o valor de C ({c})")

else:
    print(f"a soma de A e B ({soma}), é maior que o valor de C ({c})")
