import os
os.system("cls || clear")
lista_par=[]
lista_impar=[]
lista_total=[]
lista_zero=[]
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
        lista_par.append(n1)
        lista_total.append(n1)


 else:
    impares+=1
    lista_impar.append(n1)
    lista_total.append(n1)


pares=par(pares)
impares=impar(impares)
parimpa=pares_impares(lista_total)

os.system("cls || clear")
print("\t==RESULTADO==\n")
print(f"pares: {pares}\nimpares: {impares}\n")
print(f"lista de numeros pares: {lista_par}\n\nlista de numeros impares: {lista_impar}\n\n")
print("=====TERMOS DA LISTA=====\n")
for i, n1 in enumerate(lista_total, start=1):
 print(f"\n{i}º termo da lista: {n1}")
