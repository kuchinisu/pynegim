from utils.subfuncs import buscar_areas_geograficas, constructor_de_consultas



import requests

class AreaGeografica:
    
    def __init__(self, estado = None, municipio = None):

        if estado is not None:
            self.area = buscar_areas_geograficas(estado=estado, municipio=municipio)
        else: self.area = 0

        self.ultima_consulta = None
        self.ultima_salida = None
    
    def obtener_datos(self, parametros):
 
        self.ultima_consulta = constructor_de_consultas(parametros, self.area)
        try:
            response = requests.get(self.ultima_consulta)
            response.raise_for_status()
            data = response.json()
            print('---------------------')
            print(data)
            self.ultima_salida = data
            print(f'\n consulta realizada')

            
        except requests.exceptions.RequestException as e:
            print(f"Error al realizar la solicitud: {e}")

        
        return data
    

