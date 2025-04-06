# 1. Değişkenler ve Veri Tipleri
x = 5  # int
y = 3.14  # float
isim = "Ahmet"  # string
dogru_mu = True  # bool
print(x, y, isim, dogru_mu)

# 2. Veri Yapıları
# Liste
meyveler = ["Elma", "Armut", "Muz"]
print(meyveler[0])  # Elma

# Tuple (değiştirilemez liste)
renkler = ("Kırmızı", "Yeşil", "Mavi")
print(renkler[1])  # Yeşil

# Sözlük (Dictionary)
kişi = {"ad": "Ahmet", "yaş": 25}
print(kişi["ad"])  # Ahmet

# Set (kendi içinde tekrarsız elemanlar barındırır)
sayilar = {1, 2, 3, 4}
print(sayilar)

# 3. Kontrol Yapıları
# Koşul yapıları (if, elif, else)
yas = 18
if yas >= 18:
    print("Yetişkin")
else:
    print("Çocuk")

# Döngüler (for, while)
# for döngüsü
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# while döngüsü
sayac = 0
while sayac < 3:
    print("Sayac:", sayac)
    sayac += 1

# 4. Fonksiyonlar
def selamla(isim):
    return f"Merhaba, {isim}!"

print(selamla("Ahmet"))  # Merhaba, Ahmet!

# 5. Hata Yönetimi (Try-Except)
try:
    sayi = 10 / 0
except ZeroDivisionError:
    print("Sıfıra bölme hatası!")

# 6. Sınıflar ve Nesne Yönelimli Programlama
class Kisi:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def tanit(self):
        return f"Benim adım {self.ad} ve {self.yas} yaşındayım."

kisi = Kisi("Ahmet", 25)
print(kisi.tanit())  # Benim adım Ahmet ve 25 yaşındayım.

# 7. Lambda Fonksiyonları
