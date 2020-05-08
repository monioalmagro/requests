import requests

""" delete borra --- put actualiza """
if __name__ == "__main__":
    url = "http://httpbin.org/put"
    payload = {'nombre':'Emiliano','curso':'python'}
    headers = { 'Content-Type':'application/json','access-token':'12345'}

    response = requests.put(url,data=json.dumps(payload) , headers= headers )
           
    print(response.url)
    print(response.status_code)

    if response.status_code == 200:
        """ print(response.content) """
        headers_resaponse = response.headers # Dic
        print(headers_resaponse)
        print (headers_resaponse['Server'])

       