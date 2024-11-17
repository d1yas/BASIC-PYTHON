import requests

# Eskiz API credentials
EMAIL = 'mominovsharif12@gmail.com'  # Eskiz account emailingizni kiriting
PASSWORD = 'aHyZIGgDHv69tQO5pE9LAL8n6V1FztWMEnwDGBpT'  # Eskiz account parolingizni kiriting
BASE_URL = 'https://notify.eskiz.uz/api'

# Function to authenticate and get a token
def get_token():
    url = f'{BASE_URL}/auth/login'
    data = {
        'email': EMAIL,
        'password': PASSWORD
    }
    response = requests.post
    (url, data=data)

    if response.status_code == 200:
        print("Login successful")
        return response.json().get('data')['token']
    else:
        print(f"Error logging in. Status code: {response.status_code}")
        print(f"Response: {response.text}")
        raise Exception("Failed to authenticate")

# Function to send SMS
def send_sms(token, phone_number, message):
    url = f'{BASE_URL}/message/sms/send'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {
        'mobile_phone': phone_number,  # SMS qabul qiluvchining telefon raqami
        'message': message,  # SMS mazmuni
        'from': '4546'  # Eskiz tomonidan berilgan sender ID (shart emas)
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("SMS successfully sent")
        return response.json()
    else:
        print(f"Failed to send SMS. Status code: {response.status_code}")
        print(f"Response: {response.text}")
        raise Exception("SMS sending failed")

# Main function to send one SMS
def send_one_sms():
    try:
        token = get_token()
        phone_number = '998908292928'  # Qabul qiluvchi telefon raqamini kiriting
        message = 'Bu Eskiz dan test'  # Eskiz uchun ruxsat etilgan test xabari
        result = send_sms(token, phone_number, message)
        print(f"SMS send result: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    send_one_sms()
