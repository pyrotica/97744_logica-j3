import math
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def calculadora_cientifica():
    while True:
        limpar_tela()
        print("=== Calculadora Científica ===")
        print("Escolha uma operação:")
        print("1. Soma (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Potência (x^y)")
        print("6. Raiz Quadrada (√x)")
        print("7. Seno (sin)")
        print("8. Cosseno (cos)")
        print("9. Tangente (tan)")
        print("10. Logaritmo (log base 10)")
        print("11. Sair")
        
        opcao = input("Digite a opção desejada (1-11): ")
        
        match opcao:
            case "1":
                limpar_tela()
                print("=== Soma ===")
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print(f"Resultado: {a} + {b} = {a + b}")
                input("\nPressione Enter para continuar.")
            case "2":
                limpar_tela()
                print("=== Subtração ===")
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print(f"Resultado: {a} - {b} = {a - b}")
                input("\nPressione Enter para continuar.")
            case "3":
                limpar_tela()
                print("=== Multiplicação ===")
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print(f"Resultado: {a} * {b} = {a * b}")
                input("\nPressione Enter para continuar.")
            case "4":
                limpar_tela()
                print("=== Divisão ===")
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                if b != 0:
                    print(f"Resultado: {a} / {b} = {a / b}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
                input("\nPressione Enter para continuar.")
            case "5":
                limpar_tela()
                print("=== Potência ===")
                a = float(input("Digite a base: "))
                b = float(input("Digite o expoente: "))
                print(f"Resultado: {a}^{b} = {math.pow(a, b)}")
                input("\nPressione Enter para continuar.")
            case "6":
                limpar_tela()
                print("=== Raiz Quadrada ===")
                a = float(input("Digite o número: "))
                if a >= 0:
                    print(f"Resultado: √{a} = {math.sqrt(a)}")
                else:
                    print("Erro: Não é possível calcular a raiz quadrada de um número negativo.")
                input("\nPressione Enter para continuar.")
            case "7":
                limpar_tela()
                print("=== Seno ===")
                angulo = float(input("Digite o ângulo em graus: "))
                radiano = math.radians(angulo)
                print(f"Seno({angulo}°) = {math.sin(radiano)}")
                input("\nPressione Enter para continuar.")
            case "8":
                limpar_tela()
                print("=== Cosseno ===")
                angulo = float(input("Digite o ângulo em graus: "))
                radiano = math.radians(angulo)
                print(f"Cosseno({angulo}°) = {math.cos(radiano)}")
                input("\nPressione Enter para continuar.")
            case "9":
                limpar_tela()
                print("=== Tangente ===")
                angulo = float(input("Digite o ângulo em graus: "))
                radiano = math.radians(angulo)
                print(f"Tangente({angulo}°) = {math.tan(radiano)}")
                input("\nPressione Enter para continuar.")
            case "10":
                limpar_tela()
                print("=== Logaritmo ===")
                a = float(input("Digite o número: "))
                if a > 0:
                    print(f"log10({a}) = {math.log10(a)}")
                else:
                    print("Erro: O logaritmo só é definido para números positivos.")
                input("\nPressione Enter para continuar.")
            case "11":
                limpar_tela()
                print("Obrigado por usar a Calculadora Científica. Até a próxima!")
                break
            case _:
                limpar_tela()
                print("Opção inválida. Tente novamente.")
                input("\nPressione Enter para continuar.")

# Iniciar a calculadora
calculadora_cientifica()