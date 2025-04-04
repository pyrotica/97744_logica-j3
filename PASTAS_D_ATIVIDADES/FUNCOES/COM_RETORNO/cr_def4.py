import os
os.system("cls || clear")

pares=0
impares=0

def par(x):
    return x

def impar(y):
    return y

def pares_impares(z): 
    return z
for i in range(6):
 n1=int(input(f"Digite o {1+i}º numero: "))
 print()

 if n1 % 2 ==0:
        pares+=1


 else:
    impares+=1

pares=par(n1)
impares=impar(n1)
parimpa=pares_impares(n1)

print(f"pares: {pares}\nimpares: {impares}")
