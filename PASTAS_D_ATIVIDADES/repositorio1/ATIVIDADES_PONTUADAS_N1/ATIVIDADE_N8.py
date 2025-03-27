import os
os.system('clear')

import os
os.system('clear')

print("""
==========================MENU DE CORES==========================

CODIGO:     COR:
          
   1 -       VERDE     
   2 -       AZUL      
   3 -       AMARELO    
   4 -       VERMELHO
   """)
cor = input("digite o codigo da cor")

if cor =='1':
    print("VERDE, R$10,00")

elif cor == '2':
    print("AZUL, R$20,00")

elif cor == '3':
    print("AMARELO, R$30,00")

elif cor == '4':
    print("VERMELHO, R$40,00")

else:
    print("CODIGO INVALIDO")