import socket
import whois

def get_domain_info(domain):
    try:
        # IP adresini al
        ip_address = socket.gethostbyname(domain)
        print(f"Domain: {domain}\n")
        print(f"IP Address: {ip_address}\n")

        # WHOIS bilgilerini al
        whois_info = whois.whois(domain)
        print("WHOIS Bilgileri:")
        print(f"Registrar: {whois_info.registrar}\n")
        print(f"Creation Date: {whois_info.creation_date}\n")
        print(f"Expiration Date: {whois_info.expiration_date}\n")
        print(f"Name Servers: {whois_info.name_servers}\n")
        print(f"Status: {whois_info.status}\n")

    except socket.gaierror:
        print(f"'{domain}' için IP adresi bulunamadı.")
    except Exception as e:
        print(f"Hata: {e}")

# Kullanım
domain_name = input("Enter Domain.. : ")
get_domain_info(domain_name)
