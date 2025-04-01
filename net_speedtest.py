import speedtest

def test_internet_speed():
    st = speedtest.Speedtest()

    print("Sunucular yükleniyor...")
    st.get_best_server()

    print("İndirme hızı test ediliyor...")
    download_speed = st.download() / 1_000_000  # Mbps cinsine dönüştür
    print("Yükleme hızı test ediliyor...")
    upload_speed = st.upload() / 1_000_000  # Mbps cinsine dönüştür
    ping = st.results.ping

    print(f"İndirme Hızı: {download_speed:.2f} Mbps")
    print(f"Yükleme Hızı: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")

if __name__ == "__main__":
    test_internet_speed()
