class Okul():
    tip = "egitimyeri"

    def __init__(self, adi, turu, ogretmen_sayisi, ögrenci_sayisi, sinif_sayisi):
        self.adi = adi
        self.turu = turu
        self.ogretmen_sayisi = ogretmen_sayisi
        self.ögrenci_sayisi = ögrenci_sayisi
        self.sinif_sayisi = sinif_sayisi

O1 = Okul("Namık Klemal", "İlkÖğretim Okulu", 80, 1000, 80)
O2 = Okul("Atatürk", "Fen Lisesi", 20, 650, 45)
O3 = Okul("Boğaziçi", "Üniversitesi", 30, 1450, 70)

Okullar = [O1, O2, O3]

for okul in Okullar:
    print(okul.adi, okul.turu, okul.ogretmen_sayisi, okul.ögrenci_sayisi, okul.sinif_sayisi)