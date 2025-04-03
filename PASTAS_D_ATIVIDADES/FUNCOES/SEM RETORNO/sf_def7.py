import os
os.system("cls || clear")

def par_impar(num):
   if num>0:
        print(f"{num} é um numero positivo")

   elif num == 0:
    print("zero / neutro")
    
   else:
    print(f"{num} é um numero negativo")

num_infor=float(input("digite um numero: "))
par_impar(num_infor)



