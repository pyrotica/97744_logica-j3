import os
os.system("clear")

print("""
==========================MENU DE COMBUSTIVEIS==========================

CODIGO:       COMBUSTIVEL:         PREÇOS:                   ATE 25L                    ACIMA QUE 25L:
          
   A -         ALCOOL               3,79                   2% DE DESCONTO               3% DE DESCONTO 
   G -         GASOLINA             6,59                   4% DE DESCONTO               5% DE DESCONTO
   
   """)

preco_gasolina= 6.59
preco_alcool= 3.79

escolha=str(input("digite o tipo de combustivel: ")).lower()
quant=int(input("digite a quantidade de combustivel a alcool: "))
match escolha:
    case 'a':

        print("ALCOOL")
       
        if quant <= 25:
            preco_alcool_descontado= preco_alcool*0.02
            total= quant*preco_alcool_descontado

        elif quant >25:
            preco_alcool_descontado= preco_alcool*0.04
            total= quant*preco_alcool_descontado
        print(f"o preço a ser pago de seu combustivel a alcool é de {total:.2f}")

    case 'g':

        print("GASOLINA")
       
        if quant <= 25:
            preco_gasolina_descontado= preco_gasolina*0.03
            total= quant*preco_gasolina_descontado

        elif quant >25:
            preco_gasolina_descontado= preco_gasolina*0.05
            total=quant*preco_gasolina_descontado

        print(f"o preço a ser pago de seu combustivel a gasolina é de {total:.2f}")

    case _:
        print("CODIGO INVALIDO")

print()
print(f"quantidade de litro {quant}L")