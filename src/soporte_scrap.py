from bs4 import BeautifulSoup
import requests
import numpy as np

def traer_productos_cash_converter(url):
    productos = {
        'titulo': [],
        'descripcion': [],
        'precio': [],
    }

    try:
        print(f"call url: {url}")
        res = requests.get(url)
        print(f"respuesta url: {res.status_code}")

        if res.status_code == 200:
            list_titulos = []
            list_descripciones = []
            list_precios = []

            sopa = BeautifulSoup(res.content, "html.parser")
            lista_productos = sopa.findAll("div", {"class": "product-tile"})

            if len(lista_productos) > 0:
                for producto in lista_productos:
                    # Extraer el título del producto
                    titulo_elemento = producto.find("div", {"class": "pdp-link"})
                    titulo = titulo_elemento.find("a").text.strip() if titulo_elemento else np.nan
                    list_titulos.append(titulo)

                    # Extraer la descripción del producto (si hay alguna disponible)
                    descripcion_elemento = producto.find("div", {"class": "status"})
                    descripcion = descripcion_elemento.text.strip() if descripcion_elemento else np.nan
                    list_descripciones.append(descripcion)

                    # Extraer el precio del producto
                    precio_elemento = producto.find("div", {"class": "principal"})
                    if precio_elemento:
                        # Intentamos obtener el precio desde el atributo `data-price`
                        precio = precio_elemento.get("data-price", "").strip()
                        if not precio:  # Si no hay `data-price`, tomamos el texto directamente
                            precio = precio_elemento.text.strip().replace("€", "").replace(",", ".")
                    else:
                        precio = np.nan
                    list_precios.append(precio)

                productos['titulo'] = list_titulos
                productos['descripcion'] = list_descripciones
                productos['precio'] = list_precios

    except Exception as e:
        print(f"Error al traer_productos(): {e}")
 
    return productos


def traer_productos_mercado_libre(url):
    productos = {
        'titulo': [],
        'descripcion': [],
        'precio': [],
        'link': []
    }

    try:
        print(f"Llamando a la URL: {url}")
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        print(f"Respuesta del servidor: {res.status_code}")

        if res.status_code == 200:
            list_titulos = []
            list_descripciones = []
            list_precios = []
            list_links = []

            sopa = BeautifulSoup(res.content, "html.parser")
            lista_productos = sopa.find_all("li", {"class": "ui-search-layout__item"})

            if lista_productos:
                for producto in lista_productos:
                    # Extraer el título del producto
                    titulo_elemento = producto.find("h2", {"class": "ui-search-item__title"})
                    titulo = titulo_elemento.text.strip() if titulo_elemento else "Título no disponible"
                    list_titulos.append(titulo)

                    # Extraer el enlace del producto
                    link_elemento = producto.find("a", {"class": "ui-search-link"})
                    link = link_elemento['href'] if link_elemento else "Enlace no disponible"
                    list_links.append(link)

                    # Extraer la descripción del producto (usualmente no está presente en Mercado Libre, usamos el título como descripción alternativa)
                    descripcion = titulo  # Usamos el título como descripción para simplificar
                    list_descripciones.append(descripcion)

                    # Extraer el precio del producto
                    precio_elemento = producto.find("div", {"class": "poly-price__current"})
                    if precio_elemento:
                        precio_texto = precio_elemento.find("span", {"class": "andes-money-amount__fraction"})
                        precio = precio_texto.text.strip() if precio_texto else "Precio no disponible"
                    else:
                        precio = "Precio no disponible"
                    list_precios.append(precio)

                productos['titulo'] = list_titulos
                productos['descripcion'] = list_descripciones
                productos['precio'] = list_precios
                productos['link'] = list_links
            else:
                print("No se encontraron productos en la página.")

    except Exception as e:
        print(f"Error en traer_productos(): {e}")

    return productos