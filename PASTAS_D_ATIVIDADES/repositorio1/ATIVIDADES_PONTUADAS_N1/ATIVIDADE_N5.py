import os
os.system('clear')

num1=int(input("digite o primeiro numero: "))
num2=int(input("digite o segundo numero: "))
operacao=str(input('digite o tipo de operacao: '))





match operacao:
     case '+':
        soma=(num1+num2)
        print(f'soma: {soma}')
        resultado=(soma)

     case '-':
      subtracao=(num1-num2)
      print(f'subtração: {subtracao}')
      resultado=(subtracao)
     case '*':
      multiplicacao=(num1*num2)
      print(f'multiplicação: {multiplicacao}')
      resultado=(multiplicacao)
     case '/':
      divisao=(num2/num1)
      print(f'divisão: {divisao}')
      resultado=(divisao)
     case _:
      print("operação invalida")
