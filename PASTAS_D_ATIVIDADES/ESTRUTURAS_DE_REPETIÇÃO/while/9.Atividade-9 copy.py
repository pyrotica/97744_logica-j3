import os
os.system("cls || clear")

while True:
    nota1=float(input("digite a primeira nota: "))
    print()
    

    if nota1>= 0 and nota1 <= 10:
       
       print(f"a sua primeira nota é {nota1}")
       print()
       break
    else:
        print("ALGO DEU ERRADO, TENTE NOVAMENTE")
      #  print(f"e a sua media aritmetica é: {media}")
       
      #  media =(nota1+nota2)/2

while True:
 nota2=float(input("digite a segunda nota: "))
 print()

 if nota2>= 0 and nota2 <= 10:
       
       print(f"a sua segunda nota é {nota2}")
       print()
       break
 else:
        print("ALGO DEU ERRADO, TENTE NOVAMENTE")

media=(nota2+nota1)/2

print(f"A media é {media}")