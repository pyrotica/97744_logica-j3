import os

os.system("cls || clear")

porcentagem=0
valor_total = 0
preco_total = 0
pratos_solicitados = ""


while True:
    print("""
    ================= MENU =================
    1 \t Picanha \t\tR$ 250,00
    2 \t Lasanha \t\tR$ 68,00
    3 \t Strogonoff \t\tR$ 46,00
    4 \t Bife acebolado \tR$ 148,00
    5 \t Pão com ovo \t\tR$ 12,00
    6 \t pudim     \t\tR$ 45,00
    7 \t Feijão \t\tR$ 25,00
    
          """)
   
    opcao = int(input("Digite o número da opção desejada: "))

    match opcao:
        case 1:
            prato = "1/Picanha"
            preco = 250
        case 2:
            prato = "2/Lasanha"
            preco = 68
        case 3:
            prato = "3/Strogonoff"
            preco = 46
        case 4:
            prato = "4/Bife acebolado"
            preco = 148
        case 5:
            prato = "5/Pão com ovo"
            preco = 12
        case 6:
            prato = "6/pudim"
            preco = 45
        case 7:
            prato = "7/feijão"
            preco = 25
    
        case _:
          print("Opção inválida. \nTente novamente... \n")
          prato = ""
          preco = 0
            
    preco_total += preco
    pratos_solicitados += ", " + prato if pratos_solicitados else prato
   
    mais_pedidos = input("Deseja fazer um novo pedido?\nUse 'S' ou '0' para responder: ").lower()

    if mais_pedidos == "0":
        break
   
if preco_total > 0:
    via_pag = input("Deseja pagar em qual meio? \n(C) para credito \n(v) para à vista \nRª: ").lower()
    if via_pag == "v":
        via_pag="à vista"
        porcentagem = preco_total * 0.10
        valor_total = preco_total - porcentagem

    elif via_pag == "c":
        via_pag="credito"
        porcentagem = preco_total * 0.10
        valor_total = preco_total + porcentagem


total_pagar = valor_total

print("\n\t=== Nota Fiscal ===")
print(f"Pratos solicitados: {pratos_solicitados}")
print(f"O preco sem o desconto é de: R${preco_total}")
print(f"A forma de pagamento é: {via_pag}")
print(f"Valor total da compra: R${total_pagar}")

if via_pag == "à vista":
 print(f"o valor da desconto foi de: R${porcentagem}")
elif via_pag =="credito":
 print(f"o valor da acrecimo foi de: R${porcentagem}")