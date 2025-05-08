import os
import requests
import sys
from dotenv import load_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from utils.sql_connection import get_sql_connection

# En este archivo se almacenan funcionan de logica general que son de utilidad, no esta estrictamente relacionado con la base de datos.

# Facebook
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

