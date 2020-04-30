from suds.client import Client
client = Client("https://www.w3schools.com/xml/tempconvert.asmx?WSDL")
print (client)
print(type(client))