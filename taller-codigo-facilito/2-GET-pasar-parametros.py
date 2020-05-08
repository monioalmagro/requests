import requests 

""" Metodo get envia argumentos en la url por ejemplo:
http://httpbin.org/get?name=emiliano&curso=python """


if __name__ == "__main__":
    url = "http://httpbin.org/get"
    args = {'nombre':'Emiliano','curso':'python'}
    response = requests.get(url,params=args)
    print(response.url)

    

    if response.status_code == 200:
        """ Imprime todo el contenido html """
        print(response.content)

        
        