import requests


client_id = '942f5537f14dd2d3cd7b'
client_secret = '6e001cfd30e66cb17c30dc17ed407aee8e398a27' 
code='31b222839b409a5ee5c9'


if __name__ == "__main__":
    url = 'https://github.com/login/oauth/access_token'
    payload = {'client_id':client_id,'client_secret':client_secret,'code':code}
    headers = {'Accept': 'application/json'}
    response =  requests.post(url,json=payload, headers=headers)

    if response.status_code == 200:
        response_json = response.json()
        
        
        access_token = response_json['access_token']
        print(access_token)