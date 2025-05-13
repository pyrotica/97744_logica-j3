import os
os.system("cls || clear")
import time
from dataclasses import dataclass



@dataclass
class Carros:
    marca: str
    modelo: str
    categoria: str
    preco: float
informacoes_carristicas=[]
QUANT=2


for i in range(QUANT):
 print("===INFORME OS DADOS===\n")
 carros=Carros(
    
    marca=input("MARCA: "),
    modelo=input("MODELO: "),
    categoria=input("CATEGORIA: "),
    preco=input("PREÇO: ")
)
 
 nome_arquivo= "dados_c.txt"

 with open(nome_arquivo, "a") as arquivo:
  arquivo.write(f"{carros.marca}, {carros.modelo}, {carros.categoria}, {carros.preco}\n")

 print()
 os.system("cls || clear")
        

print("= SALVANDO OS DADOS DOS CLIENTES =")
time.sleep(3)
os.system("cls || clear")


print("\t\nSalvo com sucesso\t")
