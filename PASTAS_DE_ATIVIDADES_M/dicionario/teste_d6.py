import os
import time
os.system("cls || clear")

#primeira e segunda questão
aluno={'nome': "joao", 'idade': 17, 'curso': "informatica"}

aluno['estado_civil']="solteiro"

print(aluno)
time.sleep(5)
os.system("cls || clear")

#terceira, quarta e quinta questão
livro={'nomeclatura': "python", 'divisoria': "hastag"}
carro={'\nmarca': "cli", 'polegadas': "24 polegadas"}

livro.update(carro)
for chave, valor in livro.items():
    print(f"{chave}: {valor}\n")

print(livro.values())
print(livro.keys())

