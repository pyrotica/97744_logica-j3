import os
os.system("clear")

lista=[]
QUANT=5
for i in range(QUANT):
 num=int(input(f"digite a {1+i}º nota: "))

 lista.append(num)


maior_l=max(lista)
menor_l=min(lista)
print()
print("\t==========resultado==========\n")
print(f"maior numero da lista: {maior_l}\n")
print(f"menor numero da lista: {menor_l}\n")
print(f"lista completa: {lista}\n")
print("\t===LISTA===\n")
for i, num in enumerate(lista, start=1):
 print(f"\n{i}º termo da lista: {num}")

print("\n\t===LISTA===\n")
print("\t==========resultado==========")
 