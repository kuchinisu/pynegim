from utils.globales import URL_API_IND

class ConstructorDeIndicadores:
    
    def __init__(self, token):
        self.URL_API = URL_API_IND
        self.token = token
    
    def buscar_indicadires(self):
        return

    def obtener_direccion_de_indicadores(self, ):
        direccion_indicadores = {}
        
        return direccion_indicadores

    def obtener_configuracion_de_indicadores(self, direccion_de_indicadores):
        return
    

class ConfiguracionDeParametros:
    def __init__(self, indicadores, idioma, reciente, fuente, version):
        
        self.indicadores = indicadores.indicadires
        self.token = indicadores.token

        self.idioma = idioma
        self.reciente = reciente
        self.fuente = fuente
        
        self.version = version

        