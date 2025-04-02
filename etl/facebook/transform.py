import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from datetime import datetime
from etl.utils.lookup import obtener_id_fuente, obtener_id_red_social


def transformar_publicaciones(publicaciones_json, nombre_fuente, nombre_red_social):
    id_fuente = obtener_id_fuente(nombre_fuente)
    id_red_social = obtener_id_red_social(nombre_red_social)

    if id_fuente is None or id_red_social is None:
        print(f"❌ No se encontraron IDs para '{nombre_fuente}' o '{nombre_red_social}'")
        return []

    publicaciones_transformadas = []

    for pub in publicaciones_json:
        texto = pub.get("message", "").strip()
        fecha_raw = pub.get("created_time")
        enlace = pub.get("permalink_url", "")
        id_facebook = pub.get("id")
        tipo_contenido = clasificar_tipo(enlace)

        fecha_convertida = None
        if fecha_raw:
            fecha_convertida = datetime.strptime(fecha_raw, "%Y-%m-%dT%H:%M:%S%z").replace(tzinfo=None)

        publicaciones_transformadas.append({
            "id_publicacion": id_facebook,
            "id_fuente": id_fuente,
            "id_red_social": id_red_social,
            "texto": texto,
            "tipo_contenido": tipo_contenido,
            "fecha_publicacion": fecha_convertida,
            "enlace": enlace
        })

    return publicaciones_transformadas


def clasificar_tipo(enlace):
    if "video" in enlace:
        return "video"
    elif "photo" in enlace or "photos" in enlace:
        return "imagen"
    elif "story" in enlace:
        return "historia"
    elif "posts" in enlace:
        return "texto"
    elif "reel" in enlace:
        return "reel"
    elif "link" in enlace:
        return "enlace"
    else:
        return "desconocido"
    

