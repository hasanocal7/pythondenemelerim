"""def HasaniMutluEt():
    print("İstediğin her şeyi başarırsın ve penis kafalısın")
HasaniMutluEt()"""
list=[]
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
