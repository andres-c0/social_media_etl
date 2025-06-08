import requests
import os
import sys
from dotenv import load_dotenv
from etl.utils.helpers import obtener_tokens_paginas, obtener_ids_publicaciones

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

dotenv_path = os.path.join(os.path.dirname(__file__), '../../config/.env')
load_dotenv(dotenv_path)
FB_TOKEN  = os.getenv("FB_TOKEN")

def extraer_multimedia():
    ids_publicaciones = obtener_ids_publicaciones()
    tokens_paginas = obtener_tokens_paginas(FB_TOKEN)
    multimedia = []

    for post_id in ids_publicaciones:
        page_id = post_id.split("_")[0]
        page_token = tokens_paginas.get(page_id)
    
        if not page_token:
            print(f"⚠️ No se encontró token para la página {page_id}")
            continue

        url = f"https://graph.facebook.com/v19.0/{post_id}?fields=attachments{{media_type,media,url}}"
        params = {"access_token": page_token}

        try:
            response = requests.get(url,params=params)
            response.raise_for_status()
            data = response.json()

            attachments = data.get("attachments",{}).get("data",[])
            for item in attachments:
                tipo = item.get("media_type", "desconocido").lower()
                url_media = item.get("media", {}).get("source") or item.get("media", {}).get("image", {}).get("src")
                if url_media:
                    multimedia.append({
                        "id_publicacion": post_id,
                        "tipo_media": tipo,
                        "url_media": url_media
                    })
        except Exception as e:
            print(f"❌ Error extrayendo multimedia de {post_id}: {e}")
    return multimedia


