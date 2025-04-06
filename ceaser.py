def sezar_sifrele(metin, kaydirma):
    sifreli_metin = ""

    for char in metin:
        if char.isalpha():  # Sadece harfleri kontrol et
            # Harfin ASCII değerini al ve kaydır
            shift = 65 if char.isupper() else 97
            sifreli_char = chr((ord(char) + kaydirma - shift) % 26 + shift)
            sifreli_metin += sifreli_char
        else:
            # Harf olmayan karakterleri olduğu gibi ekle
            sifreli_metin += char

    return sifreli_metin

def print_background_text(text, bg_color_code):
    print(f"\033[{bg_color_code}m{text}\033[0m")

# Kullanıcıdan giriş al
metin = input("Şifrelenecek metni girin: ")
kaydirma = int(input("Kaydırma değerini girin: "))

sifreli_metin = sezar_sifrele(metin, kaydirma)
print("Şifreli Metin:", sifreli_metin)

print_background_text(sifreli_metin, 41)