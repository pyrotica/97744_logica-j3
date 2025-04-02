import os
os.system('cls || clear')

pares=0
impares=0
print()
soma = 0
for i in range(6):
    num1=int(input("digite numero: "))
    if num1 % 2 ==0:
        pares+=1
    else:
        impares+=1

total=(impares+pares)
    
print()
print(f"A quantidade de pares é {pares}")
print()
print(f"A quantidade de impares é {impares}")
print()
print(f"O total é {total}")
print()
