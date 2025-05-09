import os
os.system("cls || clear")

from dataclasses import dataclass



@dataclass
class Cliente:
    nome: str
    EMAIL: str
    telefone: int

lista_pessoas=[]
QUANT=2

print("===INFORME OS DADOS===\n")
for i in range(QUANT):
    cliente=Cliente(
        nome=input("NOME: "),
        EMAIL=input("EMAIL: "),
        telefone=input("TELEFONE: ")
    )
    lista_pessoas.append(cliente)   
    print()
    os.system("cls || clear")
    


print("===EXIBIR RESULTADOS===\n")

for clientes in lista_pessoas:
    print(f"---PESSOA {1+i}")
    print(f"NOME: {cliente.nome}")
    print(f"EMAIL: {cliente.EMAIL}")
    print(f"TEFONE: {cliente.telefone}\n\n")


