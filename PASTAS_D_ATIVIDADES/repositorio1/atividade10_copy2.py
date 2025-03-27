import os
os.system('clear')

print("""
==========================MENU==========================

CODIGO:     PRATO:     PREÇO:

   1 -       DOMINGO      
   2 -       SEGUNDA-FEIRA      
   3 -       TERÇA-FEIRA    
   4 -       QUARTA-FEIRA
   5 -       QUINTA-FEIRA 
   6 -       SEXTA-FEIRA   
   7 -       SABADO 
""")

print()

num=int(input("digite o primeiro numero: "))


if num > 1 and num < 7:
    resultado= "dia util"
  

elif num == 1 and num == 7:
  resultado = "Fim de semana"    
      
else:
  resultado= "numero invalido"

print()
print(f"resultado: {resultado}")