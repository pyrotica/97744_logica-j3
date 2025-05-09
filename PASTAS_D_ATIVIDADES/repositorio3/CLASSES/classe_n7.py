import os
os.system("cls || clear")

from dataclasses import dataclass



@dataclass
class Autor:
    nome: str
    biografia: str

@dataclass
class Livro:
    titulo: str
    ano: int

lista_livros=[]
QUANT=2

print("===INFORME OS DADOS===\n")

autor1 = Autor(
    nome=input("NOME: "),
    biografia = input("DIGITE A BIOGRAFIA DO AUTOR: ")
)
os.system("cls || clear")
for i in range(QUANT):
    livros=Livro(
        titulo=input("TITULO DO LIVRO: "),
        ano=input("ANO DE PUBLICAÇÃO: ")
    )
    lista_livros.append(livros)   
    print()
    os.system("cls || clear")
print("===CLASSE DO AUTOR===\n")
print(f"Nome: {autor1.nome}")
print(f"Bibiografia do autor: {autor1.biografia}\n\n") 
print("===CLASSE DOS LIVROS===\n")
for livros in lista_livros:
    print(f"Titulo do livro: {livros.titulo}")
    print(f"Ano de publicação: {livros.ano}\n\n")
    
