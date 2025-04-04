import os
os.system("cls || clear")

metros=float(input("Digite um valor em metros: "))

def cm(metros): 
    centimetros=metros*100
    return metros*100

centimetros=cm(metros)

print(f"{metros} Metros, é eqivalente á {centimetros} centimetros")
