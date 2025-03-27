import os
os.system('clear')

maca=1.30

macas_compradas=float(input("digite a quantidade de maçãs: "))


if macas_compradas >= 12:
    maca=1.00

total=(maca*macas_compradas)

print(f"a quantidade de maçãs são: {macas_compradas}, que deu {total:.2f}")

