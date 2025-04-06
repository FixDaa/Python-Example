# ///////////////////////////////////

import subprocess
import sys

def install_package(package_name):
    """Belirtilen paketi yükler."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

try:
    import folium
except ImportError:
    print("Görünüşe göre 'folium' kütüphanesi yüklenmemiş. Yükleniyor...")
    install_package('folium')
    import folium  # Kütüphaneyi yükledikten sonra tekrar import ediyoruz

# /////////////////////////////////////////////

# Haritanın merkez koordinatları (İstanbul)
latitude = 41.0082
longitude = 28.9784

# Haritayı oluştur
harita = folium.Map(location=[latitude, longitude], zoom_start=12)

# Haritaya bir işaretçi ekle
folium.Marker(
    location=[latitude, longitude],
    popup='İstanbul',
    icon=folium.Icon(icon='cloud')
).add_to(harita)

# Haritayı kaydet
harita.save('istanbul_harita.html')

# Haritayı görüntülemek için tarayıcıda açabilirsiniz
print("Harita 'istanbul_harita.html' olarak kaydedildi.")