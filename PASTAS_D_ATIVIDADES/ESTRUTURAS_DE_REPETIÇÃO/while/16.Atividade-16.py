import os
import time
os.system("cls || clear")

pessoas=0
salario_total=0
maior_salario=0
filote_por_familha=0
menor_salario=float('inf')
while True:  
 print("""
    ================= MENU =================
    1 |\t Adicionar pessoa
    2 |\t Sair & Exibir resultados
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
            cria=str(input("possui filho?: ")).lower()
            
            print()
            salario=int(input("digite o seu salario: "))
            salario_total+=salario
            print()
            if salario > maior_salario:
               maior_salario=salario
     
            if salario < menor_salario:
               menor_salario=salario  

            if cria == "s":
               filote_por_familha+=1
     
            media_salarial_total=salario_total/pessoas
            media_de_filhos=filote_por_familha/pessoas
            os.system("cls || clear")
        case 2:
            if pessoas> 0:
             print("saiu...")
             print()
             print(f"a quantidade de pessoas que respoderam a pesquisa são {pessoas}")
             print(f"o mair salario é de R${maior_salario}")
             print(f"o menor salario é de R${menor_salario}")
             print(f"a media de filhos é de {media_de_filhos}")
             print(f"o salario total da familia é R${salario_total}")
             print(f"A media salarial da familia é R${media_salarial_total}")
            else:
               print("Não a registros no banco de dados \nespere 3 segundos")
               time.sleep(3)
               os.system("cls || clear")
            break
         
        case _:
            print("Opção inválida. \n tente novamente")
            print("espere 2 segundos")
            time.sleep(2)
            os.system("cls || clear")
          
   