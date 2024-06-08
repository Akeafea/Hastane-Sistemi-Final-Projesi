from personel import Personel
from doktor import Doktor
from hemsire import Hemsire
from hasta import Hasta
import pandas as pd


def main():
    try:
        # Personel Nesneleri
        personel1 = Personel(1, "Ahmet", "Yılmaz", "Bilgi İşlem", 5000)
        personel2 = Personel(2, "Mehmet", "Kaya", "Muhasebe", 4500)
        print(personel1)
        print(personel2)

        # Doktor Nesneleri
        doktor1 = Doktor(3, "Akif", "Duman", "Cerrahi", 10000, "Cerrah", 6, "Çiğli Hastanesi")
        doktor2 = Doktor(4, "Ayşe", "Gül", "Pediatri", 9000, "Çocuk Doktoru", 4, "Bakırköy Hastanesi")
        doktor3 = Doktor(5, "Fatma", "Şahin", "Dahiliye", 11000, "Dahiliye Uzmanı", 10, "Çapa Hastanesi")
        print(doktor1)
        print(doktor2)
        print(doktor3)

        # Hemşire Nesneleri
        hemsire1 = Hemsire(6, "Zeynep", "Demir", "Cerrahi", 6000, 40, "Yoğun Bakım Sertifikası", "Çiğli Hastanesi")
        hemsire2 = Hemsire(7, "Merve", "Çelik", "Pediatri", 5800, 38, "Yeni Doğan Sertifikası", "Bakırköy Hastanesi")
        hemsire3 = Hemsire(8, "Elif", "Taş", "Dahiliye", 6100, 42, "Dahiliye Sertifikası", "Çapa Hastanesi")
        print(hemsire1)
        print(hemsire2)
        print(hemsire3)

        # Hasta Nesneleri
        hasta1 = Hasta(1, "Murat", "Öztürk", "1985-06-15", "grip", "ilaç")
        hasta2 = Hasta(2, "Berk", "Yıldız", "1992-03-22", "kırık", "ameliyat")
        hasta3 = Hasta(3, "Selin", "Aydın", "2000-11-05", "enfeksiyon", "antibiyotik")
        print(hasta1)
        print(hasta2)
        print(hasta3)

        # DataFrame için data
        personel_listesi = [
            #Personeller
            [personel1.get_personel_no(), personel1.get_ad(), personel1.get_soyad(), personel1.get_departman(),
             personel1.get_maas(), None, None, None, None, None, None, None, None],
            [personel2.get_personel_no(), personel2.get_ad(), personel2.get_soyad(), personel2.get_departman(),
             personel2.get_maas(), None, None, None, None, None, None, None, None],
            #Doktorlar
            [doktor1.get_personel_no(), doktor1.get_ad(), doktor1.get_soyad(), doktor1.get_departman(),
             doktor1.get_maas(), doktor1.get_uzmanlik(), doktor1.get_deneyim_yili(), doktor1.get_hastane(), None, None,
             None, None, None],
            [doktor2.get_personel_no(), doktor2.get_ad(), doktor2.get_soyad(), doktor2.get_departman(),
             doktor2.get_maas(), doktor2.get_uzmanlik(), doktor2.get_deneyim_yili(), doktor2.get_hastane(), None, None,
             None, None, None],
            [doktor3.get_personel_no(), doktor3.get_ad(), doktor3.get_soyad(), doktor3.get_departman(),
             doktor3.get_maas(), doktor3.get_uzmanlik(), doktor3.get_deneyim_yili(), doktor3.get_hastane(), None, None,
             None, None, None],
            #Hemşireler
            [hemsire1.get_personel_no(), hemsire1.get_ad(), hemsire1.get_soyad(), hemsire1.get_departman(),
             hemsire1.get_maas(), None, None, hemsire1.get_hastane(), hemsire1.get_calisma_saati(),
             hemsire1.get_sertifika(), None, None, None],
            [hemsire2.get_personel_no(), hemsire2.get_ad(), hemsire2.get_soyad(), hemsire2.get_departman(),
             hemsire2.get_maas(), None, None, hemsire2.get_hastane(), hemsire2.get_calisma_saati(),
             hemsire2.get_sertifika(), None, None, None],
            [hemsire3.get_personel_no(), hemsire3.get_ad(), hemsire3.get_soyad(), hemsire3.get_departman(),
             hemsire3.get_maas(), None, None, hemsire3.get_hastane(), hemsire3.get_calisma_saati(),
             hemsire3.get_sertifika(), None, None, None],
            #Hastalar
            [None, hasta1.get_ad(), hasta1.get_soyad(), None, None, None, None, None, None, None,
             hasta1.get_dogum_tarihi(), hasta1.get_hastalik(), hasta1.get_tedavi()],
            [None, hasta2.get_ad(), hasta2.get_soyad(), None, None, None, None, None, None, None,
             hasta2.get_dogum_tarihi(), hasta2.get_hastalik(), hasta2.get_tedavi()],
            [None, hasta3.get_ad(), hasta3.get_soyad(), None, None, None, None, None, None, None,
             hasta3.get_dogum_tarihi(), hasta3.get_hastalik(), hasta3.get_tedavi()]
        ]

        #Sütünları ve Dataframe i oluştur
        df = pd.DataFrame(personel_listesi,
                          columns=["Personel No", "Ad", "Soyad", "Departman", "Maaş", "Uzmanlık", "Deneyim Yılı",
                                   "Hastane", "Çalışma Saati", "Sertifika", "Doğum Tarihi", "Hastalık", "Tedavi"])

        # Boş olan değerler için 0 ata
        df.fillna(0, inplace=True)

        # Doktorları uzmanlık alanlarına göre gruplandırarak toplam sayısını hesaplayınız ve yazdır
        uzmanlik_gruplari = df[df["Uzmanlık"] != 0].groupby("Uzmanlık").size()
        print("\nUzmanlık Alanlarına Göre Doktor Sayısı:\n", uzmanlik_gruplari.to_string())

        # 5 yıldan fazla deneyime sahip doktorların toplam sayısını bul
        deneyimli_doktor_sayisi = df[(df["Deneyim Yılı"] > 5) & (df["Deneyim Yılı"] != 0)].shape[0]
        print("\n5 Yıldan Fazla Deneyime Sahip Doktor Sayısı:", deneyimli_doktor_sayisi)

        # Hasta adına göre DataFrame’i alfabetik olarak sıralayınız ve yazdır
        df_hastalar = df[df["Doğum Tarihi"] != 0].sort_values(by="Ad")
        print("\nAlfabetik Sıralanmış Hastalar:\n", df_hastalar.to_string(index=False))

        # Maaşı 7000 TL üzerinde olan personelleri bul
        yuksek_maasli_personel = df[df["Maaş"] > 7000]
        print("\nMaaşı 7000 TL Üzerinde Olan Personeller:\n", yuksek_maasli_personel.to_string(index=False))

        # Doğum tarihi 1990 ve sonrası olan hastaları göster
        yeni_hastalar = df[
            (df["Doğum Tarihi"] != 0) & (pd.to_datetime(df["Doğum Tarihi"]) >= pd.to_datetime("1990-01-01"))]
        print("\n1990 ve Sonrası Doğumlu Hastalar:\n", yeni_hastalar.to_string(index=False))

        # Tüm nesneleri içeren yeni bir dataframe oluştur
        yeni_df = df[["Ad", "Soyad", "Departman", "Maaş", "Uzmanlık", "Deneyim Yılı", "Hastalık", "Tedavi"]]
        print("\nYeni DataFrame:\n", yeni_df.to_string(index=False))

        # Tedavi süresi hesaplamayı test etmek için print(hasta1.tedavi_suresi_hesapla())

    except Exception as e:
        print("Bir hata oluştu:", e)


if __name__ == "__main__":
    main()
