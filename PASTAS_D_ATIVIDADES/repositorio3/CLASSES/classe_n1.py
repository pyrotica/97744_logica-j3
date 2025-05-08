import os
os.system("cls || clear")

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

#exemplo
Pessoa1 = Pessoa("Miguel", 17)
Pessoa2 = Pessoa("mathes", 18)

print(f"Nome: {Pessoa1.nome}, Idade: {Pessoa1.idade}")
print(f"Nome: {Pessoa2.nome}, Idade: {Pessoa2.idade}")