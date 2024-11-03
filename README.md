# Análisis de Precios de Productos Relacionados con PlayStation 5 en Plataformas de Segunda Mano

Este proyecto realiza un análisis exploratorio de los precios de productos relacionados con la **PlayStation 5** en diversas plataformas de venta de segunda mano, como **Cash Converters**, **Mercado Libre**, **Wallapop** y **Vinted**. El objetivo es identificar las tendencias de precios, variabilidad entre plataformas y características de cada mercado. Las visualizaciones interactivas ayudan a entender mejor las dinámicas de precios y las estrategias de venta en cada plataforma.

## Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas y archivos:
```
├── data/
├── notebooks/
│ ├── 01_API's.ipynb
│ ├── 02_Scrapeo.ipynb
│ ├── 03_BBDD.ipynb
│ ├── 04_Filtros_y_notificaciones.ipynb
│ └── 05_EDA.ipynb ├── sql/
├── src/
├── .env
├── .gitignore
└── README.md
```


## Funcionalidad del Proyecto

1. **Extracción de Datos**:
   - **Wallapop (API)**: Se accede a la API de Wallapop para extraer productos relacionados con la PlayStation 5.
   - **Vinted (API)**: Se obtiene información sobre productos listados en Vinted usando su API.
   - **Cash Converters (Web Scraping)**: Se realiza scraping en el sitio web de Cash Converters para obtener datos de precios de productos de segunda mano.
   - **Mercado Libre (Web Scraping)**: Se extraen datos de Mercado Libre utilizando técnicas de web scraping.

2. **Transformación de Datos**:
   - Los datos extraídos se transforman para asegurar consistencia y estructura uniforme. Esto incluye limpiar, normalizar nombres de columnas, convertir precios a una misma divisa si es necesario y manejar valores nulos.
   - Los datos transformados se almacenan en una base de datos para facilitar consultas y análisis posteriores.

3. **Filtrado de Datos**:
   - Se aplica una consulta SQL para filtrar solo los productos relevantes, como consolas PlayStation 5 y artículos relacionados.
   - El filtrado elimina productos irrelevantes y garantiza que solo se analicen aquellos que cumplan ciertos criterios de interés.

4. **Generación de informes y Envío de Notificación**:
   - Los datos filtrados se convierten en un archivo PDF que contiene un resumen de los productos más interesantes.
   - Este archivo PDF se envía por correo electrónico a través de un sistema de notificaciones, para que los usuarios reciban información actualizada y relevante sobre los precios de productos de segunda mano.

## Visualizaciones

El proyecto incluye las siguientes visualizaciones interactivas:

- **Distribución de Precios por Plataforma**: Un boxplot que muestra la dispersión de precios en Cash Converters, Mercado Libre y Wallapop.

## Requisitos

Las siguientes bibliotecas de Python son necesarias para ejecutar el proyecto:

- [`pandas`](https://pandas.pydata.org/pandas-docs/stable/)
- [`numpy`](https://numpy.org/doc/stable/)
- [`matplotlib`](https://matplotlib.org/stable/contents.html) 
- [`plotly`](https://plotly.com/python/)
- [`SQLAlchemy`](https://docs.sqlalchemy.org/en/20/)
- [`psycopg2`](https://www.psycopg.org/docs/)
- [`fpdf`](https://pyfpdf.github.io/fpdf2/)
- [`smtplib`](https://docs.python.org/3/library/smtplib.html)
- [`requests`](https://docs.python-requests.org/en/latest/)
- [`beautifulsoup4`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [`MIMEMultipart`](https://docs.python.org/3/library/email.mime.multipart.html)
- [`MIMEText`](https://docs.python.org/3/library/email.mime.html#email.mime.text.MIMEText)
- [`MIMEBase`](https://docs.python.org/3/library/email.mime.html#email.mime.base.MIMEBase)
- [`encoders`](https://docs.python.org/3/library/email.html#module-email.encoders)
- [`os`](https://docs.python.org/3/library/os.html)  
   
```python
!pip install pandas numpy matplotlib plotly sqlalchemy psycopg2-binary fpdf requests beautifulsoup4
```
## Conlusiones

Este repositorio contiene el análisis de datos realizado para el proyecto, organizado en varios archivos que cubren diferentes etapas del proceso.

Para consultar las conclusiones derivadas del análisis, por favor revisa el archivo [`05_EDA_y_Conclusiones`](notebooks/05_EDA_y_Conculsiones.ipynb), donde se presentan los hallazgos finales y se discuten los resultados obtenidos a lo largo del proyecto.

## Next Steps

A continuación, se detallan algunos pasos futuros para mejorar y ampliar el alcance del proyecto:

- **Dockerizar el proyecto y lanzarlo desde una Raspberry Pi**: Permitir la ejecución periódica automática de la extracción de datos, así como el envío de notificaciones de forma continua.
- **Ampliar los filtros de búsqueda en Wallapop**: Incrementar la precisión de los resultados permitiendo una búsqueda más refinada según distintos parámetros.
- **Mejorar la calidad de los PDFs generados**: Optimizar la generación de documentos PDF para asegurar una mayor claridad y resolución en los informes.