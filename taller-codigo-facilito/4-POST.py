import requests 
import json

""" Con el methodo post obtenemos recursos, con el post lo creamos"""


if __name__ == "__main__":
    url = "http://httpbin.org/post"
    payload = {'nombre':'Emiliano','curso':'python'}

    response = requests.post(url,json=payload)
    """ response = requests.post(url,data=payload) """ # lo guarda en el form
    """ response = requests.post(url,data=json.dumps(payload)) """ # lo guarda en data
    
    #json post se encarga de serializarlos
    #data nosotros nos encargamos de serializarlos
        
    print(response.url)

    if response.status_code == 200:
        print(response.content)

       