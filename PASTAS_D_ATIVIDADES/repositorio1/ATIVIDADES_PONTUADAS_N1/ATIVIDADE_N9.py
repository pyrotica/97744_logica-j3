import os
os.system("clear")

renda_mensal= float(input("digite o valor de sua renda mensal: "))
emprestimo= float(input("digite o valor do emprestimo: "))
prestacoes= float(input("digite o numero de prestações: "))

valor_prestacao =(emprestimo / prestacoes)

if emprestimo <=10 * renda_mensal and prestacoes <= 0.30 * renda_mensal:
    print("emprestimo autorizado")
else:
    print("emprestimo negado")
