import requests

if __name__ == "__main__":
    client_id = '942f5537f14dd2d3cd7b'
    client_secret = '6e001cfd30e66cb17c30dc17ed407aee8e398a27' 
    code='31b222839b409a5ee5c9'
    access_token = '975d993aa901617def14c6e5a82bd2f30081e0c9'

    url = 'http://api.github.com/user/repos'
    payload = {'name':'repo_creado_con_API_2'}
    headers = {'Accept': 'application/json', 'Authorization': 'token '+access_token}

    responce = requests.post(url,headers=headers, json=payload)

    if responce.status_code == 200 :
        print("aca")
        print(responce.json())
        
    else:
        print("aca abajo")
        print(responce.content)
