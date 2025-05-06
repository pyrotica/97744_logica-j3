import os

os.system("cls || clear")


pratos_solicitados = ""
pratos=[]
precos=[]
while True:
    os.system("cls || clear")
 
    print("""
    ================= MENU =================
    1 \t Picanha \t\tR$ 250,00
    2 \t Lasanha \t\tR$ 48,00
    3 \t Strogonoff \t\tR$ 46,00
    4 \t Bife acebolado \tR$ 78,00
    5 \t Pão com ovo \t\tR$ 10,00
          """)
   
    opcao = int(input("Digite o número da opção desejada: "))
   
    match opcao:
        case 1:
            prato = "Picanha"
            preco = 250
            precos.append(preco)
            pratos.append(prato)
        case 2:
            prato = "Lasanha"
            preco = 48
            precos.append(preco)
            pratos.append(prato)
        case 3:
            prato = "Strogonoff"
            preco = 46
            precos.append(preco)
            pratos.append(prato)
        case 4:
            prato = "Bife acebolado"
            preco = 78
            precos.append(preco)
            pratos.append(prato)
        case 5:
            prato = "Pão com ovo"
            preco = 10
            precos.append(preco)
            pratos.append(prato)
        case _:
            print("Opção inválida. \nTente novamente... \n")
            prato = ""
            preco = 0
   
    preco_total=sum(precos)
    pratos_solicitados += ", " + prato if pratos_solicitados else prato
   
    mais_pedidos = input("Deseja fazer um novo pedido?\nUse 'S' or 'N' para responder: ").upper()

    if mais_pedidos == "N":
        break
   
os.system("cls || clear")

print("\n\t=== Nota Fiscal ===")
print(f"Pratos solicitados: {pratos}")
print(f"Valor total da compra: R$ {sum(precos)},00")