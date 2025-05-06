import os
import time
os.system("cls || clear")

def tabuada(num):
   for i in range(1, 11):
     print(f"{num} X {i} = {num*i}")
     time.sleep(0)
    # print("===TABUADA===")

num_infor=float(input("digite um numero: "))
tabuada(num_infor)

              

    
    