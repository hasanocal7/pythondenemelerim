class Personel:
    def __init__(self,isim,maas,yetenek,rutbe,gunsayisi):
        self.isim=isim
        self.maas=maas
        self.yetenek=yetenek
        self.rutbe=rutbe
        self.gunsayisi=gunsayisi
    def Calis(self):
        self.gunsayisi+=1
    def Terfi(self):
        self.maas+=200
    def Bilgileri_Goster(self):
        print(self.isim,self.maas,self.yetenek,self.rutbe,self.gunsayisi,sep=" ")    
class Yonetici(Personel):
    def __init__(self, isim, maas, yetenek, rutbe, gunsayisi,yonetimBecerisi):
        super().__init__(isim, maas, yetenek, rutbe, gunsayisi)
        self.rutbe="CTO"
        self.yonetimBecerisi=yonetimBecerisi
    def MaasArttirim(self):
        self.maas+=523    
    def Bilgileri_Goster(self):
        super().Bilgileri_Goster() + print(self.yonetimBecerisi)
    def Calis(self):
        self.yonetimBecerisi+=0.5
        super().Calis()
personel1=Personel("Hasan",1000,"Yazılım","Takım Lideri",5)
personel1.Calis()
personel1.Terfi()
personel1.Bilgileri_Goster()
yonetici1=Yonetici("Ahmet",2000,"Yazılım","CTO",7,5)
yonetici1.MaasArttirim()
yonetici1.Calis()
yonetici1.Bilgileri_Goster()