import os
os.system("cls || clear")

soma=0
for i in range(2):
  while True:
    nota=float(input(f"digite a {i+1}º nota: "))
    print()
    

    if nota< 0 and nota > 10:
       print(f"NOTA INVALIDA")
       print()
       
    else:
       soma += nota
       break

media= soma/2

print(f"soma é {soma}")
print()
print(f"media é {media}")