import os
os.system("cls || clear")
import time
from dataclasses import dataclass


@dataclass
class Autoro:
  autor: str

@dataclass
class Livros_Autor:
    nome: str
    categoria: str
    preco: float
liat_D_livros=[]
QUANT=3
criador=Autoro(
 autor=input("AUTOR DO LIVRO: ")
)
os.system("cls || clear")
for i in range(QUANT):
 print("===INFORME OS DADOS DOS LIVROS===\n")
 livros=Livros_Autor(
    
    nome=input("NOME DO LIVRO: "),
    categoria=input("CATEGORIA: "),
    preco=input("PREÇO: ")
)
 
 nome_arquivo= "Catálogo_Livros.txt"

 with open(nome_arquivo, "a") as arquivo:
  arquivo.write(f"{criador.autor}, {livros.nome}, {livros.categoria}, {livros.preco}\n")

 print()
 os.system("cls || clear")
        

print("= SALVANDO OS DADOS DOS CLIENTES =")
time.sleep(3)
os.system("cls || clear")


print("\t\n\t== Salvo com sucesso ==\t")
