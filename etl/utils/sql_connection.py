import pyodbc
import os
import requests
from dotenv import load_dotenv

# Se cargan las variables de conexion desde el archivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '../../config/.env')
load_dotenv(dotenv_path)

def get_sql_connection():
    try:
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={os.getenv('SQL_SERVER')};"
            f"DATABASE={os.getenv('SQL_DATABASE')};"
            f"UID={os.getenv('SQL_USER')};"
            f"PWD={os.getenv('SQL_PASSWORD')};"
            "TrustServerCertificate=yes;"
        )
        print("✅ Conexión a SQL Server exitosa.")
        return conn
    except Exception as e:
        print("❌ Error al conectar con SQL Server:", e)
        return None
    
def obtener_ids_publicaciones():
    conn = get_sql_connection()
    cursor = conn.cursor()

    query = "SELECT id_publicacion FROM publicaciones"
    cursor.execute(query)

    ids = [row[0] for row in cursor.fetchall()]

    conn.close()

    return ids

def obtener_tokens_paginas(FB_TOKEN):
    url = "https://graph.facebook.com/v19.0/me/accounts"
    params = {
        "access_token": FB_TOKEN
    }

    response = requests.get(url, params=params)
    data = response.json()

    tokens = {}
    for pagina in data.get("data", []):
        tokens[pagina["id"]] = pagina["access_token"]
    
    return tokens

def extraer_page_id(id_publicacion):
    return id_publicacion.split("_")[0]
