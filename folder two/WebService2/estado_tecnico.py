#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
import requests
import os
import sys
from   dotenv       import load_dotenv

class ET:
  """
  Clase que interactua con la API REST de EDES.

  Dado un numero de NIS, devuelve el estado técnico en que se encuentra el servicio.
  """

  token = ""

  def __init__(self, t):
    """
    Metodo contructor de la clase.
    """

    dotenv_path = os.path.dirname(os.path.abspath(__file__)) + '/.env'
    load_dotenv(dotenv_path=dotenv_path)

    self.token = t

  def get(self, nis):
    """
    Obtiene el estado técnico del NIS.

    Parámetros:
      nis (int): Numero de NIS a consultar.

    Retorna:
      object: Objeto que contiene la propiedad 'EstadoTecnico'.
    """

    # Encabezados HTTP a enviar
    headers = {'Authorization': 'Bearer ' + self.token}

    # URL
    url = os.getenv('API_URL') + '/api/data/ugo/suministro/' + nis + '/estadotecnico'

    # Send the request
    res = requests.get( url, headers=headers)

    # Return la respuesta en JSON o un objeto vacio.
    if res.status_code == 200 :
      return res.json()

    else:
      return {}



if __name__== "__main__":

  if len(sys.argv) != 3:
    print('Uso: ' + sys.argv[0] + ' nis token')
    sys.exit(1)

  t_status = ET( sys.argv[2] )
  print( t_status.get(sys.argv[1]) )
  #help(Token)
