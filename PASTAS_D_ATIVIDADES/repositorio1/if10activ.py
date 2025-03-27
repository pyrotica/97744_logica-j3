import os

os.system("clear")

num= int(input("digite um numero: "))

if num > 10:
    print(f'{num} É MAIOR QUE 10')

elif num == 10:
    print(f'{num} É IGUAL A 10')

else:
    print(f'{num} NAO É MAIOR QUE 10')