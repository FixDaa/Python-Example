import pyttsx3

# Ses motorunu başlat
engine = pyttsx3.init()

# Sesin hızını ve tonunu ayarlama
def ayarla(hiz=150, ton=1.0):
    # Hız ayarı
    engine.setProperty('rate', hiz)
    # Sesin tonu ayarı
    engine.setProperty('volume', ton)

# Kullanıcıdan metin alıp sesli yanıt verme fonksiyonu
def seslendirme(text):
    engine.say(text)
    engine.runAndWait()

# Kullanıcıdan hız ve ton için ayar almak
def kullanici_ayar():
    try:
        hiz = int(input("Ses hızı (normal: 150): "))
    except ValueError:
        hiz = 150  # Varsayılan hız
    try:
        ton = float(input("Ses tonu (normal: 1.0): "))
    except ValueError:
        ton = 1.0  # Varsayılan ton

    ayarla(hiz, ton)

# Ana program döngüsü
def ana_program():
    print("Metin-to-Speech (Text-to-Speech) Uygulamasına Hoşgeldiniz!")
    while True:
        print("\nYapmak istediğiniz işlemi seçin:")
        print("1. Seslendirme yap")
        print("2. Hız ve ton ayarları")
        print("3. Çıkış")
        secim = input("Seçiminizi yapın (1/2/3): ")

        if secim == '1':
            metin = input("Seslendirilmesini istediğiniz metni yazın: ")
            seslendirme(metin)
        elif secim == '2':
            kullanici_ayar()
        elif secim == '3':
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek, tekrar deneyin!")

# Programı başlat
ana_program()
