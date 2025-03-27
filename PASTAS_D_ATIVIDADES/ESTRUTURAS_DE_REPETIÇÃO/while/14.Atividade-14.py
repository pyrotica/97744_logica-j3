import os
os.system("cls || clear")

soma=0
impares=0
pares=0
contador=0
contador_par=0
soma_par=0

while True:
    nota=int(input("digite uma nota: "))
    print()
    
    
    if nota == 0:
       print("ZERO INSERIDO, CODIGO ENCERRADO")
       print()
       break
    else:
       soma += nota 
       contador+=1
     

    if nota % 2 ==0:
        soma_par+=nota
        pares+=1
        contador_par+=1
    else:
        impares+=1

media_geral= soma/contador
media_par= soma_par/contador_par

print(f"A quantidade de pares é {pares}")
print()
print(f"A quantidade de impares é {impares}")
print()
print(f"soma é {soma}")
print()
print(f"media geral é {media_geral:.2f}")
print()
print(f"media geral é {media_par:.2f}")