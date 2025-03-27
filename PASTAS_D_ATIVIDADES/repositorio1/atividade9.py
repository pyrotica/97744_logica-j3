import os
os.system('clear')


print("""
==========================MENU==========================

CODIGO:     PRATO:     PREÇO:

   1 -       PICANHA      R$25,00
   2 -       LASANHA      R$20,00
   3 -      STROGONOFF    R$18,00
   4 -    BIFE ACEBOLADO  R$15,00
   5 -      PÃO COM OVO   R$5,00
""")
print()
escolha=str(input("digite o codigo da comida: "))
print()
#def process_operacao(operacao):
match escolha:
     case '1':
        print(f'Picanha, R$25,00')

     case '2':
      print('Lasanha, R$20,00')

     case '3':
      print('Strogonoff, R$18,00')

     case '4':
      print(f'bife acebolado, R$15,00')

     case '5':
      print('Pão com ovo, R$5,00')

     case _:
      print("codigo invalido")
