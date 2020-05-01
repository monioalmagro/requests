#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import sys

class webService:

    def __init__(self):
        self.url = "http://webservice11.somee.com/WebService1.asmx?WSDL"

    def validar(self):
        
        self.r = requests.get(self.url )  
        return self.r 

    def info(self):
        print(self.r.status_code)
        print(self.r.headers)
        print(self.r.encoding)    
        print(self.r.text)  

if __name__ == "__main__":
    ws = webService()
    ws.validar()
    ws.info()