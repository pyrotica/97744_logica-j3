import os
import time
os.system("cls || clear")

mulher_rica=0
pessoas=0
salario_total=0
media_salarial_total=0

idade_pessoa=[]
while True:  
 print("""
    ================= MENU =================
    1 |\t Adicionar pessoa
    2 |\t Exibir resultados
    3 |\t Sair
          """)
 print()   
 opcao = int(input("Digite o número da opção desejada: "))
 print()
 
 match opcao:
        case 1:
            os.system("cls || clear")
            print()
            pessoas+=1
            sexo=str(input("digite o sexo| \n(F) para feminivo \n(M) para masculino \nRª:")).upper()
            idade=str(input("digite a idade do individuo: "))
            if sexo == "F":
                salario_feminino=int(input("digite o seu salario: "))
                salario_total+=salario_feminino

                if salario_feminino >=5000:
                 mulher_rica+=1
                
            else:
             print()
             salario=int(input("digite o seu salario: "))
             salario_total+=salario
             print()
             
            idade_pessoa.append(idade)    
            velho=max(idade_pessoa)
            novo=min(idade_pessoa)
        case 2:
            if pessoas> 0:
             print(f"a quantidade de pessoas são {pessoas}")
             print(f"o mais velho tem {velho}")
             print(f"o mais novo tem {novo}")
             print(f"a quantidade de mulheres que ganham 5k são {mulher_rica}")
             print(f"o salario total da familia é R${salario_total}")
             print(f"A media salarial da familia é R${media_salarial_total}")
             time.sleep(5)
             os.system("cls || clear")
            else:
               print("Não a registros no banco de dados \nespere 3 segundos")
               time.sleep(3)
               os.system("cls || clear")
        case 3:
         print("saiu...")
         break
        case _:
            print("Opção inválida. \n tente novamente")
            print("espere 2 segundos")
            time.sleep(2)
            os.system("cls || clear")
          
   