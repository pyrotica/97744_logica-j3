import os
os.system("cls || clear")

from dataclasses import dataclass



@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class Pessoa:
    nome: str
    idade: int
    endereco: Endereco


    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"logradouro: {self.endereco.logradouro}")
        print(f"numero da casa: {self.endereco.numero}")
print("===CLASSE 1===")
print()
endereco1=Endereco("Rua A", 23)
pessoa1=Pessoa("marta", 44, endereco1)
pessoa1.exibir_dados()
print()
print("==CLASSE 2===")
print()
endereco2=Endereco("Rua B", 23)
pessoa2=Pessoa("lula", 50, endereco2)
pessoa2.exibir_dados()
