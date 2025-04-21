import requests
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from datetime import datetime
from etl.utils.helpers import obtener_ids_publicaciones
from etl.utils.helpers import extraer_page_id
from dotenv import load_dotenv

# Cargar las variables del archivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '../../config/.env')
load_dotenv(dotenv_path)
FB_TOKEN  = os.getenv("FB_TOKEN")

def obtener_tokens_paginas():
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

def extraer_metricas():
    print("✅ Conexión a SQL Server exitosa.")
    ids_publicaciones = obtener_ids_publicaciones()
    print(f"🗂️ Se encontraron {len(ids_publicaciones)} publicaciones para procesar métricas.")

    tokens_paginas = obtener_tokens_paginas()
    metricas_extraidas = []

    metricas_insights = ["post_impressions", "post_reach", "post_reactions_by_type_total"]

    for post_id in ids_publicaciones:
        page_id = post_id.split('_')[0]
        page_token = tokens_paginas.get(page_id)

        if not page_token:
            print(f"⚠️ No se encontró token para la página {page_id}")
            continue

        print(f"\n🔐 Token usado para la página {page_id[:8]}...")

        # --- 1. Métricas desde /insights ---
        impresiones = alcance = likes = 0

        for metrica in metricas_insights:
            url_individual = f"https://graph.facebook.com/v19.0/{post_id}/insights"
            params = {
                "metric": metrica,
                "access_token": page_token
            }

            try:
                res = requests.get(url_individual, params=params)
                res.raise_for_status()
                datos = res.json().get("data", [])
                if not datos:
                    continue

                valor = datos[0].get("values", [{}])[0].get("value", 0)

                if metrica == "post_impressions":
                    impresiones = valor
                elif metrica == "post_reach":
                    alcance = valor
                elif metrica == "post_reactions_by_type_total":
                    likes = sum(valor.values()) if isinstance(valor, dict) else 0

                print(f"📊 {metrica}: {valor}")

            except Exception as e:
                print(f"⚠️ Métrica fallida ({metrica}) para publicación {post_id}: {e}")

        # --- 2. Comentarios y compartidos desde endpoint directo ---
        comentarios = shares = 0
        url_post = f"https://graph.facebook.com/v19.0/{post_id}"
        params_post = {
            "fields": "comments.summary(true),shares",
            "access_token": page_token
        }

        try:
            res_post = requests.get(url_post, params=params_post)
            res_post.raise_for_status()
            data_post = res_post.json()

            comentarios = data_post.get("comments", {}).get("summary", {}).get("total_count", 0)
            shares = data_post.get("shares", {}).get("count", 0)

            print(f"💬 Comentarios: {comentarios} | 🔁 Shares: {shares}")

        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error extrayendo comentarios/shares de {post_id}: {e}")

        # --- 3. Agregamos a lista final ---
        metricas_extraidas.append({
            "id_publicacion": post_id,
            "alcance": alcance,
            "impresiones": impresiones,
            "vistas": 0,  # se calculará si es video en transform
            "interacciones": likes + comentarios + shares,
            "likes": likes,
            "shares": shares,
            "comentarios": comentarios
        })

    return metricas_extraidas
    
