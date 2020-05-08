import requests 


if __name__ == "__main__":
    url = "https://www.google.com.ar/"
    response = requests.get(url)

    print(response)
    """ <Response [200]> """

    if response.status_code == 200:
        """ Imprime todo el contenido html """
        print(response.content)
        """ Guarda un html de la pagina """
        content = response.content
        file = open('google.html','wb')
        file.write(content)
        file.close()