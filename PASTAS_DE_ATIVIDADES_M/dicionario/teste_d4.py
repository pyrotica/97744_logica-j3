import os
os.system("cls || clear")

# Criar um dicionário para armazenar o usuário e a senha
credenciais = {}

# Solicitar o nome de usuário e a senha inicial
usuario = input("Digite o nome de usuário: ")
senha = input("Digite sua senha: ")

# Armazenar o usuário e a senha no dicionário
credenciais[usuario] = senha
print("\nUsuário e senha cadastrados com sucesso!")

# Solicitar a alteração da senha
nova_senha = input(f"\nUsuário {usuario}, digite a nova senha: ")
credenciais[usuario] = nova_senha
print("Senha alterada com sucesso!")

# Pedir o usuário e a nova senha para confirmar
print("\nPor favor, faça login novamente para confirmar as alterações.")
usuario_login = input("Digite o nome de usuário: ")
senha_login = input("Digite sua senha: ")

# Verificar se o usuário e a senha estão corretos
if usuario_login in credenciais and credenciais[usuario_login] == senha_login:
    print("\nLogin bem-sucedido! A senha foi alterada corretamente.")
else:
    print("\nErro de login! Nome de usuário ou senha incorretos.")