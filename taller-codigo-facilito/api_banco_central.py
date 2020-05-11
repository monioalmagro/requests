# -*- coding: utf-8 -*-
import requests 
import json



token ='eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MjA2MjYzMzMsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJlbWF6enVycXVlQGdtYWlsLmNvbSJ9.7OcIFK4TivgRE8fjErZo9I8VEjq4FEQUiXiJKv4mAY7zUuImaDkNXWgPakdgVsSRentKhDzySSUdtQCaWDlucA'
url = "https://api.estadisticasbcra.com/m2_privado_variacion_mensual"
lista=[]
listaordenada=[]

if __name__ == "__main__":
    
      
    headers = {'Authorization': 'Bearer ' + token}

    res = requests.get( url, headers=headers)

    if res.ok:       
        print(res.url)
        response_json = res.json() #Dic
        for x in response_json:
            valor=x['v']
            
            
            
            lista.append(valor)

            
            #print(x['v'])
            #print(x['d'])
            #print("************************")
        lista.sort()
        print(lista[0])
        print('mas barato')
      
        
