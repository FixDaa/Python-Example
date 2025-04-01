import subprocess
import sys

def install_package(package_name):
    """Belirtilen paketi yükler."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

try:
    import periodictable
except ImportError:
    print("Görünüşe göre 'periodictable' kütüphanesi yüklenmemiş. Yükleniyor...")
    install_package('periodictable')

# ///////////////////////////////////

import periodictable

def element_bilgisi(element_ismi):
    try:
        # Elementi almak için ismi kullan
        element = getattr(periodictable, element_ismi.capitalize())
        
# Element bilgilerini yazdır
        print(f"Element: {element.name}")
        print(f"Sembol: {element.symbol}")
        print(f"Atom Numarası: {element.number}")
        print(f"Atom Kütlesi: {element.mass:.3f} g/mol")
        print(f"Elektron Yapısı: {element.electrons}")
        print(f"Yük: {element.charge}")
        print(f"Durum: {element.state}")
        print(f"Isı Kapasitesi: {element.heat_capacity} J/(kg·K)")
        print(f"Erime Noktası: {element.melting_point} °C")
        print(f"Kaynama Noktası: {element.boiling_point} °C")
        print(f"Yoğunluk: {element.density} g/cm³")
        print(f"Grup: {element.group}")
        print(f"Periyot: {element.period}")
        print(f"Doğada Bulunma Yüzdesi: {element.abundance} ppm")
    except AttributeError:
        print("Bu element mevcut değil. Lütfen geçerli bir element ismi girin.")


# Kullanıcıdan element ismini al
while True:
    element_ismi = input("Element ismini girin (çıkmak için 'exit' yazın): ")
    if element_ismi.lower() == 'exit':
        break
    element_bilgisi(element_ismi)