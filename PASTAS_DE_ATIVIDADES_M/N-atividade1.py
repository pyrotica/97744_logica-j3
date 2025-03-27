import os
os.system('clear')

num=int(input("digite o primeiro numero: "))


match num:
    case 1:
        print('Segunda')

    case 2:
      print('Fevereiro')

    case 3:
      print('Março')

    case 4:
      print('Abril')

    case 5:
      print('Maio')

    case 6:
      print('Junho')

    case 7:
      print('Julho')
      
    case 8:
      print('Agosto')

    case 9:
      print('Setembro')

    case 10:
      print('Outubro')

    case 11:
      print('Novembro')

    case 12:
      print('Dezembro')

    case _:
     print("numero invalido")