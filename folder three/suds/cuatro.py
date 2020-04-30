from suds.client import Client
import sys


url = 'http://webservice11.somee.com/WebService1.asmx?WSDL'
client = Client(url)
print(url) 
user=sys.argv[1]
password=sys.argv[2]
""" print(user)
print(password) """
d = client.service.Verificar(str(user),str(password))
print(d)