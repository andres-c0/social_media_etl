import requests
import os
import time
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from etl.utils.helpers import obtener_ids_publicaciones
from etl.utils.helpers import obtener_tokens_paginas
from etl.utils.helpers import extraer_page_id
from dotenv import load_dotenv

# Cargar las variables del archivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '../../config/.env')
load_dotenv(dotenv_path)
FB_TOKEN  = os.getenv("FB_TOKEN")

# def extraer_page_id(id_publicacion):
#     return id_publicacion.split("_")[0]

# def obtener_tokens_paginas():
#     url = "https://graph.facebook.com/v19.0/me/accounts"
#     params = {
#         "access_token": FB_TOKEN
#     }

#     response = requests.get(url, params=params)
#     data = response.json()

#     tokens = {}
#     for pagina in data.get("data", []):
#         tokens[pagina["id"]] = pagina["access_token"]
    
#     return tokens


def extraer_comentarios():
    publicaciones_ids = obtener_ids_publicaciones()
    print(f"🗂️ Se encontraron {len(publicaciones_ids)} publicaciones para procesar comentarios.")

    tokens_paginas = obtener_tokens_paginas(FB_TOKEN)

    todos_los_comentarios = []

    for id_pub in publicaciones_ids:
        page_id = extraer_page_id(id_pub)
        page_token = tokens_paginas.get(page_id)

        if not page_token:
            print(f"⚠️ No se encontró token para la página {page_id}. Se omite la publicación {id_pub}")
            continue 
       
        url = f"https://graph.facebook.com/v19.0/{id_pub}/comments"
        params = {
            "access_token": page_token,
            "limit": 100
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            for comentario in data.get("data", []):
                todos_los_comentarios.append({
                    "id_comentario": comentario.get("id"),
                    "id_publicacion": id_pub,
                    "texto_comentario": comentario.get("message", ""),
                    "fecha_comentario": comentario.get("created_time")
                })
            
            print(f"💬 {len(data.get('data', []))} comentarios extraídos de {id_pub}")

        except requests.exceptions.RequestException as e:
            print(f"❌ Error en {id_pub}: {e}")

    return todos_los_comentarios




