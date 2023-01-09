"""import math
print(math.__doc__)"""
import random
x=random.randrange(100)
while True:
    sayi=int(input("Sayı giriniz: "))
    if sayi==x:
        print("Doğru")
        break
    elif sayi<x:
        print("Az")
    else:
        print("Fazla")    