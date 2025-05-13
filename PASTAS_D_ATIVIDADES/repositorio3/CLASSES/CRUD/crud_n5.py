import os
os.system("cls || clear")
import time
from dataclasses import dataclass
QUANT=3
@dataclass
class Client:
  nome_clie: str
  nasc_clie: str
  End_clie: str
liat_D_clientes=[]

  
@dataclass
class CLT:
    nome_func: str
    nasc_func: str
    Mat: str
    End_func: str
liat_D_funcionarios=[]

for i in range(QUANT):
 print("===INFORME OS DADOS DOS CLIENTES===\n")
 clients=Client(
    nome_clie=input("NOME DO CLIENTE: "),
    nasc_clie=input("DATA DE NASCIMENTO DO CLIENTE: "),
    End_clie=input("ENDEREÇO DO CLIENTE: ")
 )
 liat_D_clientes.append(clients)
 pessoas = "Clientes.txt"

 with open(pessoas, "a") as arquivo:
  arquivo.write(f"{clients.nome_clie}, {clients.nasc_clie}, {clients.End_clie}\n")

 print()
 os.system("cls || clear")
for i in range(QUANT):
 print("===INFORME OS DADOS DOS FUNCIONARIOS===\n")
 funcionarios=CLT(
   nome_func=input("NOME DO FUNCIONARIO: "),
    nasc_func=input("DATA DE NASCIMENTO DO FUNCIONARIO: "),
    Mat=input("MATRICULA: "),
    End_func=input("ENDEREÇO DO FUNCIONARIO: ")
  )
 liat_D_funcionarios.append(funcionarios)
 
 clts = "Funcionarios.txt"

 with open(clts, "a") as arquivo:
  arquivo.write(f"{funcionarios.nome_func}, {funcionarios.nasc_func}, {funcionarios.Mat}, {funcionarios.End_func}\n")

 print()
 os.system("cls || clear")
        

print("= SALVANDO OS DADOS DOS CLIENTES =")
time.sleep(3)
os.system("cls || clear")


print("\t\n\t== Salvo com sucesso ==\t\nESPERE 5 SEGUNDOS PARA IMPRIMIR OS RESULTADOS")
time.sleep(5)
os.system("cls || clear")
print()
print("\t== FUNCIONARIOS ==\n")
try:
  with open(clts, "r") as clts:
    linhas = clts.readlines()
    for linha in linhas:
      print(f"- {linha.strip()}")

except FileNotFoundError:
  print("ARQUIVO NAO ENCONTRADO")
print()
print()
print()
print("\t== CLIENTES ==\n")

try:
  with open(pessoas, "r") as pessoas:
    linhas = pessoas.readlines()
    for linha in linhas:
      print(f"- {linha.strip()}")

except FileNotFoundError:
  print("ARQUIVO NAO ENCONTRADO")

