import os
import time
os.system("cls || clear")


print("CONTAGEM 1 Á 20 - IMPARES APENAS")
print()
for i in range(1, 21):
   if i % 2 ==1:
    print(f"o valor da variavel é {i}")
   print('_____________')
   time.sleep(0)

print("fim_for")