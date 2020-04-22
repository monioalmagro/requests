#!/usr/bin/env python3
#requeriments request

import requests


class Api:
    """  Clase que interactua con la API wapitest. """

    def __init__(self):
        """ Constructor url """

        self.url = "https://wapitest.edessa.com.ar/token"
        

    def build_dic(self,u,p,t):
        """ Solicita usuario & password y construye diccionario """

        self.dic = {
            'UserName': u ,
            'Password': p , 
            'grant_type' : t} 
        return self.dic     

    def test(self):
        """ Realiza una peticion HTTP GET psandole datos y header """
        
        headers={'Content-Type':'multipart/form-data'}
        x = requests.post(self.url,headers=headers,data = self.dic)
        return  x.text

    



if __name__ == "__main__":
    
    eddesa_t = Api()
    eddesa_t.build_dic('ivr','ivr_vis2020', 'password')
    result = eddesa_t.test()
    print(result)