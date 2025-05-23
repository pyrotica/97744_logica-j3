import os
os.system("cls || clear")

# Criar um dicionário vazio
meu_dicionario = {}

# Criar um dicionário com pares de chave e valor
dicionario = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "São Paulo"
}
#adicionar um novo valor e chave
dicionario["profissao"] = "Engenheiro"
#alterar valor existente
dicionario["idade"] = 24

#imprissão por partes
print(f"imprimir o nome: {dicionario["nome"]}\n")
print(f"imprimir a idade: {dicionario["idade"]}\n")
print(f"imprimir a cidade: {dicionario["cidade"]}\n")
#remover chave
dicionario.pop("cidade")
#imprissão completa
print(f"dicionario completo: {dicionario}")

#impressão de chaves separadamente
for chave in dicionario:
    print()
    print(chave)
print()
print()
#impressão de valores separadamente
for valor in dicionario.values():
    print(valor)
    print()

print()
print()
#impressão de chaves e valores separadamente
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")
    print()
    
