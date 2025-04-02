import requests
import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '../../config/.env')
load_dotenv(dotenv_path)

ACCESS_TOKEN = os.getenv("FB_TOKEN")


def obtener_paginas():
    url = f"https://graph.facebook.com/v19.0/me/accounts?access_token={ACCESS_TOKEN}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print("❌ Error al obtener las páginas:", response.text)
        return []

def obtener_datos_pagina(nombre_objetivo):
    paginas = obtener_paginas()

    for pagina in paginas:
        if pagina["name"].lower() == nombre_objetivo.lower():
            return pagina["id"], pagina["access_token"]
    
    print(f"❌ No se encontró la página '{nombre_objetivo}' en la cuenta.")
    return None, None

def obtener_publicaciones(page_id, page_token, fecha_inicio, fecha_fin, limite = 100):
    url = f"https://graph.facebook.com/v19.0/{page_id}/posts"
    params = {
        "access_token": page_token,
        "fields": "message,created_time,permalink_url",
        "limit": limite
    }

    if fecha_inicio and fecha_fin:
        params["since"] = int(fecha_inicio.timestamp())
        params["until"] = int(fecha_fin.timestamp())
    else:
        params["limit"] = limite

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print("❌ Error al obtener publicaciones:", response.text)
        return []

def extraer_publicaciones(nombre_pagina, fecha_inicio = None, fecha_fin = None):
    page_id, page_token = obtener_datos_pagina(nombre_pagina)
    if not page_id or not page_token:
        return []
    
    return obtener_publicaciones(page_id, page_token, fecha_inicio, fecha_fin)

    
