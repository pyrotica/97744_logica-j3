import os
os.system('clear')

print("""
==========================CALENDARIO==========================

   1-               JANEIRO      
   2-               FEVEREIRO      
   3-               MARÇO    
   4-               ABRIL
   5-               MAIO
   6-               JUNHO  
   7-               JULHO 
   8-               AGOSTO 
   9-               SETEMBRO 
   10-              OUTUBRO 
   11-              NOVEMBRO 
   12-              DEZEMBRO 

""")

print()

num=int(input("digite o primeiro numero: "))

print()

match num:
    case 1:
        print('---Janeiro---')

    case 2:
      print('---Fevereiro---')

    case 3:
      print('---Março---')

    case 4:
      print('---Abril---')

    case 5:
      print('---Maio---')

    case 6:
      print('---Junho---')

    case 7:
      print('---Julho---')
      
    case 8:
      print('---Agosto---')

    case 9:
      print('---Setembro---')

    case 10:
      print('---Outubro---')

    case 11:
      print('---Novembro---')

    case 12:
      print('---Dezembro---')

    case _:
     print("---numero invalido---")
print()