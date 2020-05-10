# -*- coding: utf-8 -*-
import requests

if __name__ == "__main__":
    url = 'https://api.github.com/user'

    session =  requests.session()
    session.auth = ('emazzurque@gmail.com', 'Githubalmagro10')

    response = session.get(url)
    if response.ok:
        """ print(response.content)
    else:
        print(response.content) """    

            #visualizo el html
        """ response=session.get('https://github.com/monioalmagro')
        if response.ok:                                  
            print(response.content) """

            # obtener las cookies de la sesión
        response=session.get('https://github.com/monioalmagro')
        if response.ok:                                  
            print(response.cookies)    