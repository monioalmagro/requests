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
        self.x = requests.post(self.url,headers=headers,data = self.dic)
        return  self.x

    def show(self):
        """ RESPONSE retorna y muestra status, Headers y Body """
        
        status = self.x.status_code
        head = self.x.headers
        body = self.x.text

        print('HTTP code : '+str(status)  )

        print('----------------------------------------------')        
        
        for n in head:
            if n == 'Content-Type':
                print('Headers : '+str(n)+(' : ')+str(head[n]) )
        
        print('----------------------------------------------')                          
        
        print('Body (Json): '+ str(body))

        return status,head,body
        

          
            




if __name__ == "__main__":
    
    eddesa_t = Api()
    eddesa_t.build_dic('ivr','ivr_vis2020', 'password')
    eddesa_t.test()
    eddesa_t.show()