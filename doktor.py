from personel import Personel

class Doktor(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

    # Accesor metotları
    def get_uzmanlik(self):
        return self.__uzmanlik

    def get_deneyim_yili(self):
        return self.__deneyim_yili

    def get_hastane(self):
        return self.__hastane

    def set_uzmanlik(self, uzmanlik):
        self.__uzmanlik = uzmanlik

    # Mutator metotları
    def set_deneyim_yili(self, deneyim_yili):
        self.__deneyim_yili = deneyim_yili

    def set_hastane(self, hastane):
        self.__hastane = hastane

    # Maas Arttırma metotu
    def maas_arttir(self, oran):
        self.set_maas(self.get_maas() * (1 + oran / 100))

    def __str__(self):
        return super().__str__() + f", Uzmanlık: {self.__uzmanlik}, Deneyim Yılı: {self.__deneyim_yili}, Hastane: {self.__hastane}"
