import os
os.system("cls || clear")


while True:
    nota=int(input("digite uma nota: "))
    if nota>= 0 and nota <= 10 :
       print(f"sua nota é {nota}")
       break
    else:
     print("NOTA INVALIDA, DIGITE NOVAMENTE")