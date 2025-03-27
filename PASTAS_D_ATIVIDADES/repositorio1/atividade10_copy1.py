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

print()

match num:
    case 1 | 7:
        resultado = "Fim de semana"

    case 2 | 3 | 4 | 5| 6:
      resultado= "dia util"
      
    case _:
     resultado= "numero invalido"

print()
print(f"resultado: {resultado}")

