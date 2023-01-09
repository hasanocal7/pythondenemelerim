"""import math
print(math.__doc__)"""
import random
"""x=random.randrange(100)
while True:
    sayi=int(input("Sayı giriniz: "))
    if sayi==x:
        print("Doğru")
        break
    elif sayi<x:
        print("Az")
    else:
        print("Fazla")   """




kursun=random.randrange(1,7)
for i in range(1,7):
    if i!=kursun:
        _=input("SIK")
        continue
    else:
        print("ÖLDÜN")
        break