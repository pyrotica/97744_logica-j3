import os
os.system("cls || clear")
diciplina=""
# função sem retorno
def logo_senai():
    print(f"=== SENAI ===")
logo_senai() #chamar a função
aluno=str(input("digite o seu nome: "))
os.system("cls || clear")
logo_senai() #chamar a função
idade=int(input("digite a sua idade: "))
os.system("cls || clear")
logo_senai() #chamar a função
print(f"\nNome: {aluno}")
print(f"\nIdade: {idade}")

