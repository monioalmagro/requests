from suds.client import Client


client = Client('http://webservice11.somee.com/WebService1.asmx?WSDL')

 
print(client)