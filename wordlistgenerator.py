import itertools
import math

def generate_wordlist(characters, min_length, max_length, output_file):
    """
    Belirtilen karakter setine göre, min_length ile max_length (her iki sınır dahil)
    arasında tüm kombinasyonları oluşturur ve output_file dosyasına yazar.
    """
    with open(output_file, "w", encoding="utf-8") as f:
        for length in range(min_length, max_length + 1):
            for combo in itertools.product(characters, repeat=length):
                f.write("".join(combo) + "\n")

if __name__ == '__main__':
    # Kullanıcıdan karakter setini al
    characters = input("Lütfen kullanılacak karakterleri giriniz (örn. araba): ").strip()
    if not characters:
        print("Hata: Karakter seti boş olamaz.")
        exit(1)

    # Karakter setinin uzunluğu, minimum oluşturulacak uzunluk olarak alınır
    min_length = len(characters)
    print(f"Minimum oluşturulacak uzunluk (karakter seti uzunluğu): {min_length}")

    # Kullanıcıdan maksimum uzunluğu al
    try:
        max_length = int(input("Oluşturulacak maksimum kelime uzunluğunu giriniz (örn. 7): "))
    except ValueError:
        print("Hata: Maksimum uzunluk sayı olmalıdır.")
        exit(1)

    if max_length < min_length:
        print(f"Hata: Maksimum uzunluk en az {min_length} olmalıdır.")
        exit(1)

    # Çıktı dosyası adı
    output_file = input("Çıktı dosyasının adını giriniz (örn. wordlist.txt): ").strip()
    if not output_file:
        print("Hata: Çıktı dosyası adı boş olamaz.")
        exit(1)

    # Toplam kombinasyon sayısını hesapla
    total_combinations = sum(len(characters) ** i for i in range(min_length, max_length + 1))

    # Tahmini üretim hızı (kombinasyon/saniye) – bu değer sisteminize göre değişebilir
    # Bu örnekte yaklaşık 500,000 kombinasyon/saniye baz alınıyor.
    combinations_per_second = 500000
    estimated_seconds = total_combinations / combinations_per_second

    # Tahmini süreyi okunabilir formata çevir (saniye, dakika, saat)
    if estimated_seconds < 60:
        time_str = f"{estimated_seconds:.2f} saniye"
    elif estimated_seconds < 3600:
        time_str = f"{estimated_seconds / 60:.2f} dakika"
    else:
        time_str = f"{estimated_seconds / 3600:.2f} saat"

    print("\n*** Tahmini Bilgiler ***")
    print(f"Toplam kombinasyon sayısı: {total_combinations}")
    print(f"Tahmini üretim süresi: {time_str}")
    print("Not: Üretim sırasında kombinasyonlar teker teker oluşturulup dosyaya yazılır, bu sayede bellek kullanımı minimaldir.")
    print("Ancak, kombinasyon sayısı çok yüksekse CPU yükü ve disk alanı kullanımı artabilir.\n")

    onay = input("Devam etmek istiyor musunuz? (e/h): ").strip().lower()
    if onay != "e":
        print("İşlem iptal edildi.")
        exit(0)

    print(f"\nKombinasyonlar '{output_file}' dosyasına yazılıyor...")
    generate_wordlist(characters, min_length, max_length, output_file)
    print(f"İşlem tamamlandı. Wordlist başarıyla '{output_file}' dosyasına kaydedildi.")
