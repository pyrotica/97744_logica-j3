import os
os.system("clear")


nome=str(input("digite o seu nome: "))
sexo=str(input("digite o seu sexo: ")).lower()


match sexo:

    case "f":

        print("FEMININO")
        estado_civil=str(input("o seu estado civil: ")).lower()

        if estado_civil == "casada":
            ano=int(input("digite a quantidade de anos de casal"))
            print(f"{nome} do sexo {sexo} é {estado_civil} a {ano} anos")
        else:
            print(f"{nome} é solteira")

    case "m":

        print("MASCULINO")
        estado_civil=str(input("o seu estado civil: ")).lower()

        if estado_civil == "casado":
            ano=int(input("digite a quantidade de anos de casal"))
            print(f"{nome} do sexo {sexo} é {estado_civil} a {ano} anos")
        else:
            print(f"{nome} é solteiro")

    case _:
        print("ALGO ERRADO, FAZ O L")
