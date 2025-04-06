import tkinter as tk
from tkinter import messagebox, font
import yfinance as yf

def fetch_stock_data():
    symbol = entry_symbol.get().strip().upper()
    
    if not symbol:
        messagebox.showerror("Hata", "Lütfen bir hisse senedi sembolü girin.")
        return

    try:
        stock = yf.Ticker(symbol)
        historical_data = stock.history(period='1d')

        if historical_data.empty:
            messagebox.showerror("Hata", "Geçersiz hisse senedi sembolü.")
            return

        latest_data = historical_data.iloc[-1]

        label_result.config(text=(
            f'Sembol: {symbol}\n\n'
            f'Tarih: {latest_data.name.date()}\n\n'
            f'Açılış Fiyatı: {format_price(latest_data["Open"])}\n\n'
            f'Yüksek Fiyat: {format_price(latest_data["High"])}\n\n'
            f'Düşük Fiyat: {format_price(latest_data["Low"])}\n\n'
            f'Kapanış Fiyatı: {format_price(latest_data["Close"])}\n\n'
            f'Hacim: {latest_data["Volume"]}'
        ))
        
        # Kalın font ayarları
        formatted_text = (
            f'Sembol: {symbol}\n\n'
            f'Tarih: {latest_data.name.date()}\n\n'
            f'Açılış Fiyatı: {format_price(latest_data["Open"])}\n\n'
            f'Yüksek Fiyat: {format_price(latest_data["High"])}\n\n'
            f'Düşük Fiyat: {format_price(latest_data["Low"])}\n\n'
            f'Kapanış Fiyatı: {format_price(latest_data["Close"])}\n\n'
            f'Hacim: {latest_data["Volume"]}'
        )
        
        label_result.config(text=formatted_text)
    except Exception as e:
        messagebox.showerror("Hata", f"Veri alınırken hata oluştu: {str(e)}")

def format_price(price):
    return f"{price:.2f}"

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Hisse Senedi Verileri")
root.geometry("400x350")  # Pencere boyutu
root.configure(bg="#f0f0f0")  # Arka plan rengi

# Yazı tipi ayarları
header_font = font.Font(family="Helvetica", size=14, weight="bold")
label_font = font.Font(family="Helvetica", size=12)

# Kullanıcıdan hisse senedi sembolü girişi
label_prompt = tk.Label(root, text="Hisse Senedi Sembolü (ör. AAPL, MSFT):", bg="#f0f0f0", font=header_font)
label_prompt.pack(pady=10)

entry_symbol = tk.Entry(root, font=label_font, width=20)
entry_symbol.pack(pady=5)

# Verileri al butonu
button_fetch = tk.Button(root, text="Verileri Al", command=fetch_stock_data, bg="#4CAF50", fg="white", font=label_font, relief=tk.RAISED)
button_fetch.pack(pady=10)

# Sonuçları göstermek için etiket
label_result = tk.Label(root, text="", justify=tk.LEFT, bg="#f0f0f0", font=label_font)
label_result.pack(pady=10)

# Ana döngüyü başlat
root.mainloop()
