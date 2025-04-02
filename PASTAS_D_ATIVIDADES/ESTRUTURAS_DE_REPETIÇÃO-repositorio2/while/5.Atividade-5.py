import os
os.system("cls || clear")
opcao = 0
print("""
==========================MENU==========================

CODIGO:                   RESULTADO:

   1 -                    CONTINUAR 
   2 -                    MENSAGEM
   3 -                      SAIR
  """)
print()

while True:
    
    print()
    opcao = str(input("Digite a opção: "))
    
    if opcao == '1':
         print()
         print("Você escolheu continuar.")
         
    elif opcao == '2':
         print()
         print("Mensagem :V")
         
    elif opcao == '3':
         print()
         print("Saindo do programa...")
         
         break
    else:
          print()
          print("Opção inválida. Tente novamente.")