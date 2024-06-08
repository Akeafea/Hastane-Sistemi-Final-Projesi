from personel import Personel

class Hemsire(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    #Accesor metotları
    def get_calisma_saati(self):
        return self.__calisma_saati

    def get_hastane(self):
        return self.__hastane

    def get_sertifika(self):
        return self.__sertifika

    # Mutator metotları
    def set_sertifika(self, sertifika):
        self.__sertifika = sertifika

    def set_calisma_saati(self, calisma_saati):
        self.__calisma_saati = calisma_saati

    def set_hastane(self, hastane):
        self.__hastane = hastane

    #Maas Arttırma metotu
    def maas_arttir(self, oran):
        self.set_maas(self.get_maas() * (1 + oran / 100))

    def __str__(self):
        return super().__str__() + f", Çalışma Saati: {self.__calisma_saati}, Sertifika: {self.__sertifika}, Hastane: {self.__hastane}"
