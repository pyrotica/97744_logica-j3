#com while

#limpar o craxe
import os
os.system("cls || clear")

#dados pre colocados
senha_cadastrada="1234"
login_cadastrado="migues"
contador = 0

while True:
    
     login=str(input("digite o usuario: ")).lower()
     senha=str(input("digite a senha: "))

     if senha==senha_cadastrada and login==login_cadastrado:
#caso o login e senha sejam corretos
        print()
        print("login e senha corretas \nseja bem-vindo")
        break
     
#caso ultrapasse o numero de tentativas
     else:
        print()
        print("login ou senha incorretos")
        print()
        contador +=1
     if contador==3: 
      print("TENTATIVAS DEMAIS, COMPUTADOR BLOQUEADO")
      break


 