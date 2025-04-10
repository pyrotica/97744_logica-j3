import os
os.system("cls || clear")

def par_impar(num):
   if num % 2 ==0:
        print(f"{num} é par")

   elif num == 0:
    print("zero")
    
   else:
    print(f"{num} é impar")

num_infor=float(input("digite um numero: "))
par_impar(num_infor)





