import requests


class Api:
    """  Clase que interactua con la API wapitest. """

    def __init__(self):
        """ Constructor url """

        self.url = "http://webservice11.somee.com/WebService1.asmx"
        

    def build_dic(self,u,p,):
        """ Solicita usuario & password y construye diccionario """

        self.dic = {
            'UserName': u ,
            'Password': p , 
            } 
        return self.dic     

    def test(self):
        """ Realiza una peticion HTTP GET psandole datos y header """

        headers={'Content-Type':'multipart/form-data'}
        x = requests.post(self.url,headers=headers,data = self.dic)
        print(x)
        return  x.text, x.status_code
        

    



if __name__ == "__main__":
    
    eddesa_t = Api()
    eddesa_t.build_dic('usuario','123456')
    result = eddesa_t.test()
    print(result)

    """ user == usuario y password == 123456 """