"""class Ogrenci:
    ad=""
    soyad=""
    numara=""
kayit=Ogrenci()
kayit.ad=input("Öğrenci adı giriniz: ")
kayit.soyad=input("Öğrenci soyad giriniz: ")
kayit.numara=input("Öğrenci numara giriniz: ")
print(kayit.ad,kayit.soyad,kayit.numara, sep=",")"""

"""class Hayat:
    def Ye(self):
        print("Yiyorum")
    def iç(self):
        print("İçiyorum")
    def Sıç(self):
        print("Sıçıyorum")
insan=Hayat()
insan.Ye()
insan.iç()
insan.Sıç()"""

"""class Calisan:
    def __init__(self,kimlik,ad,soyad,babad,anad):
        self.kimlik=kimlik
        self.ad=ad
        self.soyad=soyad
        self.babad=babad
        self.anad=anad
calisan=Calisan("123","Hasan","Öcal","Adnan","Yasemin")
print(calisan.ad,calisan.soyad)"""

"""class Dikdortgen:
    uzun_kenar=0
    kisa_kenar=0
    def AlanHesap(self,kenar1,kenar2):
        self.kisa_kenar=kenar1
        self.uzun_kenar=kenar2
        print(kenar1*kenar2)
class Kare(Dikdortgen):
    kenar=0        
sekil1=Dikdortgen()
sekil2=Kare()
sekil2.AlanHesap(5,2)    
sekil1.AlanHesap(3,3)"""
"""class Dikdortgen:
    def __init__(self,uzke,kiske) -> None:
        self.uzke=uzke
        self.kiske=kiske
    def AlanHesap(self):
        alan=self.kiske*self.uzke
        return alan
    def __add__(self,other):
        return self.AlanHesap()+other.AlanHesap()
sekil1=Dikdortgen(5,3)
sekil2=Dikdortgen(7,2)
alantop=sekil1+sekil2
print(alantop)"""
