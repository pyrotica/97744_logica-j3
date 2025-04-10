import os
os.system("cls || clear")

imc=0
def indice(): 
    imc=(peso)/(altura*altura)

    if imc <18.5:
        print("abaixo do peso \n")
        print("consulte um nutricionista, papyrus")

    elif imc >=18.5 and imc <=24.9:
        print("peso normal \n")
        print("se mantenha-se normal\n")

    elif imc >=25 and imc <=29.9:
        print("sobre peso \n")
        print("faça uma dieta, bola do quico\n")

    elif imc >=30 and imc <=34.9:
        print("Obesidade grau 1 \n")
        print("procure uma oritação de um profissional de saude, bolo de forma\n")

    elif imc >=35 and imc <=39.9:
        print("Obesidade grau 2 \n")
        print("Calma ai baleio, consulte um medico ai\n")

    elif imc >=40:
        print("Obesidade grau 3 \n")
        print("BUSQUE ASSITENCIA MEDICA, PLANETO\n")

    
    return imc



peso=float(input(f"Digite o seu peso: "))
altura=float(input("digite a sua altura: "))
print()



imc=indice()
print(f"IMC DA PESSOA: {imc:.2f}")
