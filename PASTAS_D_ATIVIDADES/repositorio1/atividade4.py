import os
os.system("clear")

login_cadastrado ="miguel"
senha_cadastrada = "1234"

login=str(input("digite o usuario: "))
senha=str(input("digite a senha: "))

if login_cadastrado == login and senha_cadastrada == senha:
    print("bem vindo")
else:
    print("login ou senha incorretos")
