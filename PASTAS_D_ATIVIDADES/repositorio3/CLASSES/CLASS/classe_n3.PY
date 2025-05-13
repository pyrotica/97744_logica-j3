import os
os.system("cls || clear")

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

print("===PESSOA 1===\n")
Pessoa1 = Pessoa(
    nome=str(input("digite seu nome: ")),
    idade=int(input("digite sua idade: ")),
    peso=float(input("digite sua peso: ")),
    altura=float(input("digite sua altura: "))
    )
os.system("cls || clear")

print(f"Nome: {Pessoa1.nome}, Idade: {Pessoa1.idade}, Peso: {Pessoa1.peso}, Altura: {Pessoa1.altura}")
