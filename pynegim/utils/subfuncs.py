from fuzzywuzzy import process

from pynegim.utils.globales import ESTADOS, MUNICIPIOS, URL_API_IND

from urllib.parse import quote

def buscar_areas_geograficas(estado, municipio = None):
    
    estado_resultado = process.extractOne(estado, ESTADOS)
    estado = estado_resultado[0]
    if municipio is not None:
        

        municipios = MUNICIPIOS[estado]["municipios"].keys()

        municipio_resultado = process.extractOne(municipio, municipios)

        area = {
            "estado":MUNICIPIOS[estado]["id_estado"],
            "municipio":MUNICIPIOS[estado]["municipios"][municipio_resultado]
        }

    else:
        area = {
            "estado":MUNICIPIOS[estado]["id_estado"],
            "municipio":None
        }

    return area

def constructor_de_consultas(parametros, area):
    parametros = parametros
 
    indicadores = parametros.indicadores

    construccion_indicadores = 'INDICATOR/'
    
    for indicador in indicadores:

        construccion_indicadores += f'{indicador},'
    
    construccion_indicadores[-1] = '/'

    reciente = parametros.reciente
    fuente = parametros.fuente
    version = parametros.version
    token = parametros.token

    idioma = parametros.idioma

    area = area["estado"] + area["municipio"] if area["municipio"] is not None else area["estado"]

    consulta_base = URL_API_IND + construccion_indicadores  + f'{idioma}/{area}/{reciente}/{fuente}/{version}/'
    api_key = token
    query_string = "?type=json"

    consulta = consulta_base +quote(api_key) + query_string

    return consulta 