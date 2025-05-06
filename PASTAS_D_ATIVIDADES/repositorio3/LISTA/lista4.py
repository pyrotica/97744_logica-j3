import os
os.system("clear")
soma=0
contador=0
resultado=""
lista=[]
QUANT=4
for i in range(QUANT):
 num=int(input(f"digite a {1+i}º nota: "))
 
 soma+=num
 lista.append(num)
 contador+=1


# lista.remove(lista[1])

media=sum(lista)/contador

if media >= 7:
 resultado="APROVADO"

elif media >=5:
 resultado="RERCUPERAÇÃO"

elif media <5:
 resultado="REPROVADO"

print("________GABARITO________\n\n")
print(resultado)
print()
print(f"somatoria das notas: {sum(lista)}\n")
print(f"media: {media}\n")
for i, num in enumerate(lista, start=1):
 print(f"{i}º numero {num}")

# for num in lista: