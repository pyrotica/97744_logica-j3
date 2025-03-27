import os
os.system("cls || clear")

soma = 0

while True:
    idade = int(input("Digite a idade: "))
    
    if idade >= 18 and idade<=60:
        print()
        print("""CONTUDO LIBERADO   
              
⣀⣀⣤⣤⣤⣤⣄⣀⣀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣴⣤⣀⠀
⠘⠟⠋⢉⣠⣤⣭⣭⠭⡍⠀⠀⠀⢩⠭⣭⣭⣤⣄⡈⠙⠻⠂
⠀⠀⠴⠯⢽⣿⡿⣹⣍⠟⠀⠀⠀⠻⠸⠏⠿⠿⠧⡽⠂⠀⠀
              
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⢰⠃⠀⠀
⠀⠀⠀⠀⠀⢠⣀⣀⣀⣀⣀⣀⣀⣀⡤⠤⠞⠁⢀⡏⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠋⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀
        
               """)
        print()
        break
    else:
        print()
        print(" CONTEUDO NEGADO")
        print()