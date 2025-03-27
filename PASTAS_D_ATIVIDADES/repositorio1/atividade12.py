import os
os.system('clear')

valor=int(input("digite o valor da compra: "))

print()

print("informe o tipo de pagamento: ")

print()
print("""
==========================TIPO DE PAGAMENTO==========================

   1-               à vista     
   2-               à prazo     
   
""")
print()

escolha=int(input("digite o tipo de pagamento "))
print()

match escolha:

    case 1:
        print('---à vista---')
        print()
        desconto=(10/100)
        valor_descontado= (valor*desconto)
        total=(valor-valor_descontado)
        print(f"""
        o valor foi de: {valor} Reais
        
        com o desconto de 10% foi de {valor_descontado} Reais
       
       o valor total foi de {total} reais
        """)

    case 2:
        print('---á prazo---')
        print()
        parcelas= int(input("digite a quantidade de parcelas: "))
        print()

        if parcelas >= 1 and parcelas<=6:
          valor_parcelado=(valor/parcelas)
          print(f"o valor foi de: {valor} Reais ")
          print()
          print(f'a parcela foi dividida em {parcelas} vezes')
          print()
          print(f"o valor a ser pago a cada mês é de: {valor_parcelado} Reais")
          print()
          print(f"o valor total a prazo foi de {valor} Reais ")
        else:
            print('---quantidade de parcelas invalida---')
    

    case _:
        print("---OPERAÇÃO INVALIDA---")



    
print()
