import psycopg2
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import pandas as pd

def obtener_datos_vinted_sql():
    """
    Conecta a la base de datos y extrae los datos filtrados de Wallapop.
    Retorna un DataFrame con los datos.
    """
    # Conectar a la base de datos
    conn = psycopg2.connect(
        dbname="proyecto_5",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )
    
    query = "SELECT url_producto FROM vinted_interesante"
    df = pd.read_sql_query(query, conn)
    
    # Cerrar conexión
    conn.close()
    
    return df

def generar_pdf(df, output_path="../data/informes_interesantes"):
    """
    Genera un PDF a partir de un DataFrame y lo guarda en output_path.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    
    # Título
    pdf.cell(200, 10, txt="Datos de Vinted - Productos PS5", ln=True, align='C')
    pdf.ln(10)  # Salto de línea
    
    # Agregar filas de datos
    for i, row in df.iterrows():
        pdf.cell(200, 10, txt=", ".join(str(value) for value in row.values), ln=True)
    
    # Guardar el PDF
    pdf.output(output_path)

def enviar_correo_con_adjunto(destinatario, asunto, cuerpo, archivo_adj):
    """
    Envía un correo electrónico con un archivo adjunto.
    """
    remitente = "mdlflucas@gmail.com"
    contraseña = "slak evdq fdek farx"
    
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    
    # Adjuntar archivo PDF
    with open(archivo_adj, "rb") as adjunto:
        mime_base = MIMEBase('application', 'octet-stream')
        mime_base.set_payload(adjunto.read())
        encoders.encode_base64(mime_base)
        mime_base.add_header('Content-Disposition', f'attachment; filename={os.path.basename(archivo_adj)}')
        mensaje.attach(mime_base)
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(remitente, contraseña)
            server.send_message(mensaje)
        print("Correo enviado exitosamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")