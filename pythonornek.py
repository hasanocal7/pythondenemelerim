"""def fakto(x):
    if x==1:
        return 1
    else:
        return (x*fakto(x-1))
sonuc=fakto(5)
print(sonuc)  """
def asallar(x):
    for x in range (y+1):
        sayac=0
        for i in range(1,x+1):
            if x%i==0:
                sayac+=1
        if sayac==2:
            print(x)        
sonuc=asallar(5,25)
print(sonuc)                                         