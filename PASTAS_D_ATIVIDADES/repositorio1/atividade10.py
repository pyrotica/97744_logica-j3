import os
os.system('clear')

print("""
==========================CALENDARIO==========================

   1 -       DOMINGO      
   2 -       SEGUNDA-FEIRA      
   3 -       TERÇA-FEIRA    
   4 -       QUARTA-FEIRA
   5 -       QUINTA-FEIRA 
   6 -       SEXTA-FEIRA   
   7 -       SABADO 
      
""")

num=int(input("digite o primeiro numero: "))


match num:
    case 1:
        print('final de semana')
        print('domingo')

    case 2:
      print('é dia util')
      print('segunda-feira')

    case 3:
      print('é dia util')
      print('terça-feira')

    case 4:
      print('é dia util')
      print('Quarta-feira')

    case 5:
      print('é dia util')
      print('Quinta-feira')

    case 6:
      print('é dia util')
      print('sexta-feira')

    case 7:
      print('final de semana')
      print('sabado')

    case _:
     print("numero invalido")

