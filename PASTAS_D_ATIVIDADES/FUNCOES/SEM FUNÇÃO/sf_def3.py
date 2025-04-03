import os
os.system("cls || clear")
diciplina=""
# função sem retorno
def estudante(nome):
    print(f"saldação {nome}! bem-vindo ao nosso site do Senai!")

aluno=str(input("digite o seu nome: "))
estudante(aluno)
print()

# if diciplina == "logica de programacao":
def nomeclatura(diciplina):
    print(f"A diciplina ({diciplina}), faz parte do curso de DS")
    print()

# for i in range(2):
diciplina=str(input("digite o nome da diciplina: "))
nomeclatura(diciplina)