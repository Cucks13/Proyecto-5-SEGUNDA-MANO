import os
import requests
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

api_key_wallapop = os.getenv("api_key_wallapop")
endpont_wallpop = os.getenv("endpont_wallpop")

def busqueda_wallapop(producto, precio_min, precio_max):

	url = "https://wallapop3.p.rapidapi.com/search"

	querystring = {f"query":{producto},"minPrice":{precio_min},"maxPrice":{precio_max},"sort":"mostRecent"}

	headers = {
	"x-rapidapi-key": api_key_wallapop,
	"x-rapidapi-host": "wallapop3.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	data_response = (response.json())

     
	return data_response


def obtener_datos_wallapop(producto, precio_min, precio_max):
    datos_wallapop = busqueda_wallapop(producto, precio_min, precio_max)
    
    if not isinstance(datos_wallapop, list):
        print("Error: 'busqueda_wallapop' no devolvió una lista. Verifica la función.")
        return None
    
    df_datos_wallapop = pd.DataFrame(datos_wallapop)
    
    print("Vista previa de los datos:")
    print(df_datos_wallapop.head(1))
    
    columnas_a_eliminar = ["favorited", "created_at", "modified_at", "taxonomy", "is_favoriteable"]
    df_datos_wallapop = df_datos_wallapop.drop(columnas_a_eliminar, axis=1, errors='ignore')
    
    return df_datos_wallapop