import os
os.system("cls || clear")

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
print("===PESSOA 1===\n")
Pessoa1_nome=str(input("digite seu nome: "))
Pessoa1_idade=int(input("digite sua idade: "))
os.system("cls || clear")

print("===PESSOA 2===\n")
Pessoa2_nome=str(input("digite seu nome: "))
Pessoa2_idade=int(input("digite sua idade: "))
os.system("cls || clear")

Pessoa1 = Pessoa(Pessoa1_nome, Pessoa1_idade)
Pessoa2 = Pessoa(Pessoa2_nome, Pessoa2_idade)

print(f"Nome: {Pessoa1.nome}, Idade: {Pessoa1.idade}\n")
print(f"Nome: {Pessoa2.nome}, Idade: {Pessoa2.idade}")