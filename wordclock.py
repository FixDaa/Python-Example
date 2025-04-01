from datetime import datetime
import pytz

print("Hello World")

# Dünya saat dilimleri
timezones = [
    'America/New_York',   # New York
    'America/Los_Angeles', # Los Angeles
    'Europe/London',      # Londra
    'Europe/Paris',       # Paris
    'Asia/Tokyo',         # Tokyo
    'Australia/Sydney',   # Sydney
    'Asia/Istanbul'       # İstanbul
]

def print_current_times(timezones):
    for tz in timezones:
        timezone = pytz.timezone(tz)
        local_time = datetime.now(timezone)
        print(f"Time in {tz}: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")

print_current_times(timezones)
