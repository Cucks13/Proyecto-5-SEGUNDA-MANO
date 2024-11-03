import os
import json
import requests
import pandas as pd
from dotenv import load_dotenv
import pandas as pd
load_dotenv()


api_key_wallapop = os.getenv("api_key_wallapop")
endpont_wallpop = os.getenv("endpont_wallpop")
api_key_vinted = os.getenv("api_key_vinted")

def busqueda_wallapop(producto, precio_min, precio_max, nombre_archivo="resultado.json"):
    url = "https://wallapop3.p.rapidapi.com/search"
    
    querystring = {
        "query": producto,
        "minPrice": precio_min,
        "maxPrice": precio_max,
        "sort": "mostRecent"
    }
    
    headers = {
        "x-rapidapi-key": api_key_wallapop,
        "x-rapidapi-host": "wallapop3.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        data_response = response.json()
        
        with open(nombre_archivo, "w", encoding="utf-8") as file:
            json.dump(data_response, file, indent=4)
    
        return data_response
    else:
        return None



def procesar_datos_wallapop(df_datos_wallapop):
    
    if not isinstance(df_datos_wallapop, pd.DataFrame):
        print("Error: El argumento proporcionado no es un DataFrame.")
        return None
    
    df_datos_wallapop['url_completa'] = "https://es.wallapop.com/item/" + df_datos_wallapop['web_slug']
    df_datos_wallapop['user_allows_shipping'] = df_datos_wallapop['shipping'].apply(lambda x: x['user_allows_shipping'] if isinstance(x, dict) else x)
    columnas_a_eliminar = ["favorited", "created_at", "modified_at", "taxonomy", "is_favoriteable", "shipping", "web_slug"]
    df_datos_wallapop = df_datos_wallapop.drop(columnas_a_eliminar, axis=1, errors='ignore')
    df_datos_wallapop['price'] = df_datos_wallapop['price'].apply(lambda x: x['amount'] if isinstance(x, dict) else x)
    df_datos_wallapop['is_refurbished'] = df_datos_wallapop['is_refurbished'].apply(lambda x: x['flag'] if isinstance(x, dict) else x)
    df_datos_wallapop['location'] = df_datos_wallapop['location'].apply(lambda x: x['city'] if isinstance(x, dict) else None)
    df_datos_wallapop['bump'] = df_datos_wallapop['bump'].apply(lambda x: x['type'] if isinstance(x, dict) else None)
    df_datos_wallapop['reserved'] = df_datos_wallapop['reserved'].apply(lambda x: x['flag'] if isinstance(x, dict) else None)
    nuevos_nombres = {
    'id': 'id',
    'user_id': 'user_id',
    'title': 'título',
    'description': 'descripcion',
    'category_id': 'categoria_id',
    'price': 'precio(€)',
    'images': 'imagenes',
    'reserved': 'reservado',
    'location': 'localización',
    'bump': 'golpe',
    'is_refurbished': 'reacondicionado',
    'user_allows_shipping': 'posibilidad_envio',
    'url_completa': 'url_producto'
    }

    df_datos_wallapop = df_datos_wallapop.rename(columns = nuevos_nombres)
    df_datos_wallapop.to_csv("../data/datos_wallpop_limpios.csv")

    return df_datos_wallapop





def buscar_vinted(query, country="es", sort="price_high_to_low", page="1", nombre_archivo="vinted_ps5"):

    url = "https://vinted6.p.rapidapi.com/search"
    querystring = {
        "country": country,
        "sort": sort,
        "page": page,
        "query": query
    }
    headers = {
        "x-rapidapi-key": api_key_vinted,
        "x-rapidapi-host": "vinted6.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        datos = response.json()
        
        if nombre_archivo:
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4)
        
        return datos
    else:
        return 
    
def procesar_datos_vinted(df):
    df_filtrado = df[df['title'].str.contains("Play Station 5|PS5", case=False, na=False)]
    
    columnas_a_eliminar = [
        "discount", "conversion", "badge", "service_fee", "price", "view_count", 
        "size_title", "content_source", "icon_badges", "item_box", 
        "search_tracking_params", "photo"
    ]
    df_filtrado.drop(columnas_a_eliminar, axis=1, inplace=True)
    
    df_filtrado.to_csv("../data/datos_vinted_filtrados.csv", index=False)
    
    return df_filtrado
