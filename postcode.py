import requests

def get_postal_code_info(postal_code, country_code='US'):
    # Zippopotam.us API URL'si
    url = f'http://api.zippopotam.us/{country_code}/{postal_code}'

    try:
        # API'ye istek gönder
        response = requests.get(url)
        # İstek başarılı mı kontrol et
        if response.status_code == 200:
            data = response.json()
            # Posta kodu bilgilerini al
            place_info = data['places'][0]
            return {
                'postal_code': postal_code,
                'country': data['country abbreviation'],
                'state': place_info['state'],
                'city': place_info['place name'],
                'latitude': place_info['latitude'],
                'longitude': place_info['longitude']
            }
        else:
            return {'error': 'Bilgi bulunamadı veya geçersiz posta kodu'}
    except Exception as e:
        return {'error': str(e)}

# Kullanıcıdan posta kodunu al
postal_code = input('Posta kodunu girin: ')
country_code = input('Ülke kodunu girin (örneğin, US için Amerika Birleşik Devletleri): ')

# Bilgileri al ve ekrana yazdır
info = get_postal_code_info(postal_code, country_code)
print(info)
