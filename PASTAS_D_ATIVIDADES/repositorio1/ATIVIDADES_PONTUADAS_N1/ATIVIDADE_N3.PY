import os
os.system("clear")

a=int(input("digite o primeiro numero: "))
b=int(input("digite o segundo numero: "))


if a == b:
   print("soma")
   print()
   soma=(a + b)
   c=(soma)
   print(f"o valor de c é {c}")
else:
    print("multiplicação")
    print()
    multiplicacao=(a * b)
    c=(multiplicacao)
    print(f"o valor de c é {c}")
