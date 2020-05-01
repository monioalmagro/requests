#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from suds.client import Client
import sys

class WebService:

    def __init__(self):
        self.user = sys.argv[1]
        self.password = sys.argv[2]
        self.url = 'http://webservice11.somee.com/WebService1.asmx?WSDL'

    def cliente(self):
        self.client = Client(self.url)
        return self.client

    def info(self):
        print(self.client)

    def isStaff(self): 
        self.staff = self.client.service.Verificar(self.user,self.password)
        return self.staff

    def status(self):
        if self.staff:
            print("Usuario Verificado")
        else:
            print("Usuario no verificado")    
      



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Ingrese usuario y contraseña al correr este programa")
        print("ejemplo :python web_service_prueba.py user password")
        sys.exit(1)

    q = WebService()
    q.cliente()
    q.info()
    q.isStaff()
    q.status()