"""def HasaniMutluEt():
    print("İstediğin her şeyi başarırsın ve penis kafalısın")
HasaniMutluEt()"""
"""list=[]
def asal_mi(sayi):
    for i in range(sayi+1):
        a=1
        if sayi%(i+1)==0:
            list.append(i)
    if len(list)==2:
        print(True)
    else:
        print(False)
asal_mi(13)
asal_mi(12)"""
"""def adsoy(ad,soyad,numara):
    print("isim: "+ad+"soyad: "+soyad+"numara: "+numara)
adsoy("hasan",numara="548", ) """
"""def my_generator(n):

    # initialize counter
    value = 0

    # loop until counter is less than n
    while value < n:

        # produce the current value of the counter
        yield value

        # increment the counter
        value += 1

# iterate over the generator object produced by my_generator
for value in my_generator(3):

    # print each value produced by generator
    print(value)
"""
"""def adim1():
    n=1
    def adim2():
        nonlocal n
        n+=1
        return n
    return adim2
s=adim1()
print(s())"""