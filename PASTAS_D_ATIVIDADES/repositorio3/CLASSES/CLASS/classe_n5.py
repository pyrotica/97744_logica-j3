import os
os.system("cls || clear")

from dataclasses import dataclass



@dataclass
class Endereco:
    logradouro: str
    cidade: str

@dataclass
class Pessoa:
    nome: str
    EMAIL: str
    endereco: Endereco


    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"EMAIL: {self.EMAIL}")
        print(f"logradouro: {self.endereco.logradouro}")
        print(f"cidade: {self.endereco.cidade}")
print("===CLASSE 1===")
print()
endereco1=Endereco("Rua A", "Brasilia")
pessoa1=Pessoa("marta", "ender@gmail.com", endereco1)
pessoa1.exibir_dados()
print()
print("==CLASSE 2===")
print()
endereco2=Endereco("Rua B", "São Paulo")
pessoa2=Pessoa("lula", "migues@gmail.com", endereco2)
pessoa2.exibir_dados()
print()
print("==CLASSE 3===")
print()
endereco2=Endereco("Rua C", "Rio de Janeiro")
pessoa2=Pessoa("bolsonabo", "bigues@gmail.com", endereco2)
pessoa2.exibir_dados()
