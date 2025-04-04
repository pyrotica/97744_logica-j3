import os
os.system("cls || clear")



def par_impares():
    
  pares=0
  impares=0

  for i in range(6):
   n1=int(input(f"Digite o {1+i}º numero: "))
   print()

   if n1 % 2 ==0:
    pares+=1


   else:
     impares+=1

  return pares, impares


pares, impares = par_impares()

print(f"pares: {pares}\nimpares: {impares}")
