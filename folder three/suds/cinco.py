#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import sys

class webService:

    def __init__(self):
        self.url = "https://www.cultura.gob.ar/api/v2.0/organismos/?WSDL "

    def validar(self):
        
        self.r = requests.get(self.url )  
        return self.r 

    def info(self):
        #print(self.r.status_code)
        #print(self.r.headers)
        #print(self.r.encoding)    
        #print(self.r.text)  
        #print(self.r.content)
        thisdict=self.r.json()
        
        
        #x=thisdict.get('results')
        #l=x[0]
        #m=l.get('nombre')
        #print(m) 
        
        x= thisdict.get('results')
        print(len(x))
        for i in x:
            print(i['nombre'])



if __name__ == "__main__":
    ws = webService()
    ws.validar()
    ws.info()
