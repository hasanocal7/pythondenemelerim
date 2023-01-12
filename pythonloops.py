"""for i in range(10):
    print(i)
j=1
while j<10:
    print(j)
    j+=1"""
"""list=["ahmet","mehmet","ciklet"]
for i in list:
    print(i)
for i in range(1,20):
    if i==15:
        continue
    print(i)"""

def foo1(num1,num2):
    try:
        return num1+num2+0/1
    except:
        "NewException"
sonuc=foo1(1,2)
print(sonuc)               
