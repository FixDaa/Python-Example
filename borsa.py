# ///////////////////////////////////

import subprocess
import sys

def install_package(package_name):
    """Belirtilen paketi yükler."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

try:
    import yfinance
except ImportError:
    print("Görünüşe göre 'yfinance' kütüphanesi yüklenmemiş. Yükleniyor...")
    install_package('yfinance')


# ///////////////////////////////////

import yfinance as yf

def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    historical_data = stock.history(period='1d')

    if historical_data.empty:
        raise ValueError("Geçersiz sembol.")

    latest_data = historical_data.iloc[-1]
    return latest_data

while True:
    symbol = input("Lütfen hisse senedi sembolünü girin (örn: AAPL, MSFT, TSLA): ")
    try:
        latest_data = get_stock_data(symbol)

        # Function to format prices to two decimal places
        def format_price(price):
            return f"{price:.2f}"

        print(f'Sembol: {symbol}')
        print(f'Tarih: {latest_data.name.date()}')
        print(f'Açılış Fiyatı: {format_price(latest_data["Open"])}')
        print(f'Yüksek Fiyat: {format_price(latest_data["High"])}')
        print(f'Düşük Fiyat: {format_price(latest_data["Low"])}')
        print(f'Kapanış Fiyatı: {format_price(latest_data["Close"])}')
        print(f'Hacim: {latest_data["Volume"]}')
        break  # Başarılı bir şekilde veri alındıysa döngüden çık
    except ValueError as e:
        print(e)
        print("Lütfen geçerli bir hisse senedi sembolü girin.")
