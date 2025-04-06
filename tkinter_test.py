import tkinter as tk

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Gelişmiş Tkinter Uygulaması")
root.geometry("400x300")

# Etiket ekle
label = tk.Label(root, text="Merhaba, Tkinter!")
label.pack(pady=20)

# Giriş kutusu
entry_label = tk.Label(root, text="Bir metin girin:")
entry_label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

# Onay kutusu
check_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(root, text="Bu seçeneği işaretle", variable=check_var)
checkbutton.pack(pady=5)

# Radyo butonları
radio_var = tk.StringVar(value="Seçenek 1")
radio_label = tk.Label(root, text="Bir seçenek belirleyin:")
radio_label.pack(pady=5)

radio1 = tk.Radiobutton(root, text="Seçenek 1", variable=radio_var, value="Seçenek 1")
radio1.pack(pady=2)

radio2 = tk.Radiobutton(root, text="Seçenek 2", variable=radio_var, value="Seçenek 2")
radio2.pack(pady=2)

# Buton fonksiyonu
def button_clicked():
    entered_text = entry.get()
    check_status = "İşaretli" if check_var.get() else "İşaretli değil"
    selected_option = radio_var.get()

    result_text = f"Girdiğiniz Metin: {entered_text}\nOnay Kutusu: {check_status}\nSeçilen Seçenek: {selected_option}"
    label.config(text=result_text)

# Buton ekle
button = tk.Button(root, text="Gönder", command=button_clicked)
button.pack(pady=20)

# Pencereyi çalıştır
root.mainloop()
