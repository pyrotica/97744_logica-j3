import os
os.system('clear')


print("""
==========================MENU==========================

CODIGO:      frutas:        ate 5 kg:      acima de 5kg:

   1 -       MORANGO           2,50             2,20
   2 -       MAÇÃS             1,80             1,50
  
""")
maca=float(2.50)
maca2=float(2.20)
morango=float(1.80)
morango2=float(1.50)

quat_maca=int(input("digite a quantidade de maçãs"))
quant_morango=int(input("digite a quantidade de morangos"))
#quant_total=(quant_morango+quat_maca)

if quant_morango and quat_maca <=5:
    total=(quant_morango*morango)+(quat_maca*maca)
    print(f"{total}")
elif quat_maca or quant_morango > 8:
    total=(quant_morango*morango)+(quat_maca*maca)
    total_final=(total)*0.10
    print(f"o valor que se deve pagar é: {total_final}")
    
#else:
    #total=(quant_morango*morango2)+(quat_maca*maca2)
    #print(f"{total}")
    
