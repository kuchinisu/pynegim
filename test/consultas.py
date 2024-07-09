from urllib.parse import quote
import requests

base_url = "https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/1002000001/es/070000050018/true/BISE/2.0/"
api_key = "59525305-2c33-46e3-62c1-d5ad9b3b03b1"
query_string = "?type=json"

full_url = base_url + quote(api_key) + query_string

try:
    response = requests.get(full_url)
    response.raise_for_status()
    data = response.json()
    print('---------------------')
    print(data)
    print(f'\n consulta realizada')
except requests.exceptions.RequestException as e:
    print(f"Error al realizar la solicitud: {e}")


print(base_url)