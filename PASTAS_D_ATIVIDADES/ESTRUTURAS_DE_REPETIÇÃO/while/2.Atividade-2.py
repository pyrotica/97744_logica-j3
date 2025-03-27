import os
os.system("cls || clear")

senha_cadastrada="1234"


while True:
    senha=str(input("digite a senha: "))

    if senha==senha_cadastrada:
        print()
        print("senha correta, bem-vindo")
        break
    else:
        print()
        print("senha incorreta, tente novamente")
        print()
print()

print("""
⠀⣀⣀⣤⣤⣤⣤⣄⣀⣀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣴⣤⣀⠀
⠘⠟⠋⢉⣠⣤⣭⣭⠭⡍⠀⠀⠀⢩⠭⣭⣭⣤⣄⡈⠙⠻⠂
⠀⠀⠴⠯⢽⣿⡿⣹⣍⠟⠀⠀⠀⠻⠸⠏⠿⠿⠧⡽⠂⠀⠀
      
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⢰⠃⠀⠀
⠀⠀⠀⠀⠀⢠⣀⣀⣀⣀⣀⣀⣀⣀⡤⠤⠞⠁⢀⡏⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠋⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀


""")
