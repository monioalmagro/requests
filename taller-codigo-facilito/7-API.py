import requests

if __name__ == "__main__":
    url = 'https://www.hola.com/imagenes/estar-bien/20190410140226/mejores-razas-perro-defensa-personal-cs/0-666-608/perrodefensa-m.jpg'

    response = requests.get(url,stream=True)
    # stream Realiza la peticion sin cerrar la conexion.
    with open('imagen.jpg','wb') as file:
        for chunk in response.iter_content():#descarga el contenido poco a poco
            file.write(chunk)
    response.close()