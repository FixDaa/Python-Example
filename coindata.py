# ///////////////////////////////////

import subprocess
import sys

def install_package(package_name):
    """Belirtilen paketi yükler."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

try:
    import requests
except ImportError:
    print("Görünüşe göre 'requests' kütüphanesi yüklenmemiş. Yükleniyor...")
    install_package('requests')

# ///////////////////////////////////


def get_crypto_details(crypto_name):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_name}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

if __name__ == "__main__":
    crypto_name = input("Kripto para ismini girin (örneğin 'bitcoin', 'ethereum'): ").lower()
    crypto_details = get_crypto_details(crypto_name)

    if crypto_details:
        print(f"İsim: {crypto_details['name']}\n")
        print(f"Sembol: {crypto_details['symbol']}\n")
        print(f"Piyasa Değeri: ${crypto_details['market_data']['market_cap']['usd']}\n")
        print(f"24 Saatlik İşlem Hacmi: ${crypto_details['market_data']['total_volume']['usd']}\n")
        print(f"Güncel Fiyat: ${crypto_details['market_data']['current_price']['usd']}\n")
    else:
        print("Geçersiz bir kripto para ismi girdiniz veya veri alınamadı.")
