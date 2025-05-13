import os
os.system("cls || clear")
import time
from dataclasses import dataclass
QUANT=5

@dataclass
class Seres:
    nome: str
    nasc: str
    RG: str
    CPF: str
liat_D_pessoas=[]

for i in range(QUANT):
 print("===INFORME OS DADOS DOS LIVROS===\n")
 pessoas=Seres(
   nome=input("NOME DO DA PESSOA: "),
    nasc=input("DATA DE NASCIMENTO: "),
    RG=input("RG: "),
    CPF=input("CPF: ")
  )
 liat_D_pessoas.append(pessoas)
 
 nome_arquivo = "Funcionarios.txt"

 with open(nome_arquivo, "a") as arquivo:
  arquivo.write(f"{pessoas.nome}, {pessoas.nasc}, {pessoas.RG}, {pessoas.CPF}\n")

 print()
 os.system("cls || clear")
        

print("= SALVANDO OS DADOS DOS CLIENTES =")
time.sleep(3)
os.system("cls || clear")


print("\t\n\t== Salvo com sucesso ==\t")

try:
  with open(nome_arquivo, "r") as nome_arquivo:
    linhas = nome_arquivo.readlines()
    for linha in linhas:
      print(f"- {linha.strip()}")

except FileNotFoundError:
  print("ARQUIVO NAO ENCONTRADO")

