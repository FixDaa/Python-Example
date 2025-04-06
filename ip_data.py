import requests
import socket
import platform

def get_ip_info():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_info = response.json()
        public_ip = ip_info['ip']
        
        # Coğrafi bilgi almak için ipinfo API kullanımı
        geo_response = requests.get(f'https://ipinfo.io/{public_ip}/json')
        geo_info = geo_response.json()
        
        print(f"Kamu IP Adresiniz: {public_ip}")
        print(f"Coğrafi Konum: {geo_info.get('city', 'Bilinmiyor')}, {geo_info.get('region', 'Bilinmiyor')}, {geo_info.get('country', 'Bilinmiyor')}")
        print(f"ISP: {geo_info.get('org', 'Bilinmiyor')}")
        
    except Exception as e:
        print(f"IP bilgilerini alırken hata oluştu: {e}")

def get_dns_info():
    try:
        dns_servers = socket.getaddrinfo(socket.gethostname(), None)
        print("DNS Bilgileri:")
        for info in dns_servers:
            print(f"Hostname: {info[0]}, IP: {info[4][0]}")
        
        # Sistemdeki DNS sunucularını görmek için
        dns_resolvers = []
        if platform.system() == "Windows":
            with open(r'C:\Windows\System32\drivers\etc\hosts') as f:
                lines = f.readlines()
                for line in lines:
                    if not line.startswith("#") and line.strip():
                        dns_resolvers.append(line.strip())
        else:
            # Linux ve macOS için
            with open('/etc/resolv.conf') as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith("nameserver"):
                        dns_resolvers.append(line.split()[1])
        
        print("\nSistem DNS Sunucuları:")
        for dns in dns_resolvers:
            print(dns)

    except Exception as e:
        print(f"DNS bilgilerini alırken hata oluştu: {e}")

def get_proxy_info():
    try:
        proxy_response = requests.get('https://www.proxy-list.download/api/v1/get?type=https')
        proxies = proxy_response.text.split('\r\n')
        proxies = list(filter(None, proxies))  # Boş satırları filtrele
        
        print(f"Kullanılabilir Proxy Sayısı: {len(proxies)}")
        print("Proxy Listesi:")
        for proxy in proxies:
            print(proxy)
        
    except Exception as e:
        print(f"Proxy bilgilerini alırken hata oluştu: {e}")

if __name__ == "__main__":
    print("IP Bilgileri:")
    get_ip_info()
    print("\nDNS Bilgileri:")
    get_dns_info()
    print("\nProxy Bilgileri:")
    get_proxy_info()
