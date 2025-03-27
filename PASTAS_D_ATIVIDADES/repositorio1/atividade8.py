import os
os.system('clear')

num1=int(input("digite o primeiro numero: "))
num2=int(input("digite o segundo numero: "))
operacao=str(input('digite o tipo de operacao: '))


soma=(num1+num2)
subtracao=(num1-num2)
multiplicacao=(num1*num2)
divisao=(num2/num1)

match operacao:
     case '+':
        print(f'soma: {soma}')
     case '-':
      print(f'subtração: {soma}')

     case '*':
      print(f'multiplicação: {multiplicacao}')

     case '/':
      print(f'divisão: {divisao}')

     case _:
      print("operação invalida")
