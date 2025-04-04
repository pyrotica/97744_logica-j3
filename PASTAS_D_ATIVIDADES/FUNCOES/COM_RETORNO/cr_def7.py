import os
from datetime import datetime
os.system("cls || clear")

ano=int(input("Digite o seu ano de nascimento: "))

def ano_total(ano): 
 return datetime.now().year-ano

idade=ano_total(ano)

print(f"sua idade é {idade}")
