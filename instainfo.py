# ///////////////////////////////////

import subprocess
import sys

def install_package(package_name):
    """Belirtilen paketi yükler."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

try:
    import instaloader
except ImportError:
    print("Görünüşe göre 'instaloader' kütüphanesi yüklenmemiş. Yükleniyor...")
    install_package('instaloader')
    import instaloader  # Kütüphaneyi yükledikten sonra tekrar import ediyoruz

# /////////////////////////////////////////////


def get_instagram_profile_info(username):
    # Instaloader'ı başlat
    loader = instaloader.Instaloader()

    try:
        # Profil bilgilerini çek
        profile = instaloader.Profile.from_username(loader.context, username)

        # Profil bilgilerini düzenle
        profile_info = {
            'username': profile.username,
            'full_name': profile.full_name,
            'bio': profile.biography,
            'followers': profile.followers,
            'following': profile.followees,
            'posts': profile.mediacount,
            'is_private': profile.is_private,
            'is_verified': profile.is_verified,
        }

        return profile_info
    except instaloader.exceptions.InstaloaderException as e:
        return {'error': str(e)}

# Kullanıcıdan Instagram kullanıcı adını al
username = input('Instagram kullanıcı adını girin: ')

# Bilgileri al ve ekrana yazdır
info = get_instagram_profile_info(username)

print(info)