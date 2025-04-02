import os
os.system("cls || clear")

print("""
==========================MENU==========================

     CODIGO:     PRATO:          PREÇO:

\t1 - \tPICANHA          R$25,00
\t2 - \tLASANHA          R$20,00
\t3 - \tSTROGONOFF       R$18,00
\t4 - \tBIFE ACEBOLADO   R$15,00
\t5 - \tPÃO COM OVO      R$5,00
      
========================================================
""")
print()
print()
# pedir que escolha o prato
pedido=str()
escolha=str(input("digite o codigo da comida: "))
if escolha=="1":
 pedido="picanha"
 preco=25
elif escolha=="2":
 pedido="lasanha"
 preco=20
elif escolha=="3":
 pedido="strogonoff"
 preco=18
elif escolha=="4":
 pedido="bife acebolado"
 preco=15
elif escolha=="5":
 pedido="pão com ovo"
 preco=5

desejo=str(input("deseja mais algum prato? \n(s) para sim \n(n) para não \n: ")).lower()

while desejo=="s":
# caso escolhe pedir mais
 escolha=str(input("digite o codigo da comida \n Digite qualquer numero diferente de 1/2/3/4/5 se quiser não pedir mais \n: "))
 if escolha == "1":
  pedido+=" / picanha"
  preco+=25
 elif escolha=="2":
  pedido+=" / lasanha"
  preco+=20
 elif escolha=="3":
   pedido+=" / strogonoff"
   preco+=18
 elif escolha=="4":
  pedido+=" / bife acebolado"
  preco+=15
 elif escolha=="5":
  pedido+=" / pão com ovo"
  preco+=5
 else:
  break

preco_gorjeta=(preco*0.1)
gorjeta=str(input(f"Deseja pagar uma gorjeta ao garçom? A gorjeta sera adicionado ao valor final da compra. \n de {preco_gorjeta} \n(s) para sim \n(n) para nâo \n: ")).lower()
if gorjeta=="s":
#caso quera pagar a gorjeta adicional
   
   preco_total=(preco+preco_gorjeta)
   print(f"os pratos são {pedido}, no preço total de R${preco_total},00")
else:
# caso nâo queira pagar a gorjeta
   preco_total=preco
   print(f"o prato é {pedido} com o preço total de R${preco_total},00")

   #fim





   #por que esta lendo isso? o codigo ja acabou. xispa
