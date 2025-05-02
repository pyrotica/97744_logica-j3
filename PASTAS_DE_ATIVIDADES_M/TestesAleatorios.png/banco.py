import os

# Função para limpar a tela
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Função para exibir saldo
def exibir_saldo(conta):
    return f"Saldo atual: R$ {conta['saldo']:.2f}"

# Função para depositar
def depositar(conta, valor):
    if valor > 0:
        conta['saldo'] += valor
        return f"Depósito de R$ {valor:.2f} realizado com sucesso!"
    else:
        return "Valor inválido para depósito."

# Função para sacar
def sacar(conta, valor):
    if valor > 0:
        if valor <= conta['saldo']:
            conta['saldo'] -= valor
            return f"Saque de R$ {valor:.2f} realizado com sucesso!"
        else:
            return "Saldo insuficiente para saque."
    else:
        return "Valor inválido para saque."

# Função para exibir o histórico
def exibir_historico(historico):
    if not historico:
        return "Nenhuma transação realizada ainda."
    return "\n".join(historico)

# Inicializar conta e histórico
conta = {"nome": "Usuário", "saldo": 0.0}
historico = []

# Menu principal
while True:
    limpar_tela()
    print("=== Banco Simulado ===")
    print("1. Exibir Saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Histórico de Transações")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")

    # Usando match-case para tratar as opções
    match opcao:
        case "1":
            limpar_tela()
            print("=== Exibir Saldo ===")
            print(exibir_saldo(conta))
            input("\nPressione Enter para voltar ao menu.")
        case "2":
            limpar_tela()
            print("=== Depositar ===")
            try:
                valor = float(input("Digite o valor para depósito: "))
                mensagem = depositar(conta, valor)
                historico.append(f"Depósito: R$ {valor:.2f}")
                print(mensagem)
            except ValueError:
                print("Erro: Digite um valor válido.")
            input("\nPressione Enter para voltar ao menu.")
        case "3":
            limpar_tela()
            print("=== Sacar ===")
            try:
                valor = float(input("Digite o valor para saque: "))
                mensagem = sacar(conta, valor)
                if "sucesso" in mensagem:
                    historico.append(f"Saque: R$ {valor:.2f}")
                print(mensagem)
            except ValueError:
                print("Erro: Digite um valor válido.")
            input("\nPressione Enter para voltar ao menu.")
        case "4":
            limpar_tela()
            print("=== Histórico de Transações ===")
            print(exibir_historico(historico))
            input("\nPressione Enter para voltar ao menu.")
        case "5":
            limpar_tela()
            print("Obrigado por usar o Banco Simulado. Até a próxima!")
            break
        case _:
            limpar_tela()
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para voltar ao menu.")