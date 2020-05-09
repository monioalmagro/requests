import requests


client_id = '942f5537f14dd2d3cd7b'
client_secret = '6e001cfd30e66cb17c30dc17ed407aee8e398a27' 
code='31b222839b409a5ee5c9'
access_token = '975d993aa901617def14c6e5a82bd2f30081e0c9'


if __name__ == "__main__":
    url = 'http://api.github.com/user/repos'
    headers = { 'Authorization': 'token 975d993aa901617def14c6e5a82bd2f30081e0c9' }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        payload = response.json()

        for project in payload:
            name = project['name']
            print(name)
    else:
        print(response.content)
   