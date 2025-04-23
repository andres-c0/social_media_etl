import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from etl.utils.lookup import obtener_ids_videos

def transformar_metricas(metricas_json):
    ids_videos = obtener_ids_videos()
    metricas_transformadas = []
    
    for metrica in metricas_json:
        id_publicacion = metrica.get("id_publicacion")
        vistas = 0

        # Si la publicacion corresponde a un video, se extrae el numero de vistas
        if id_publicacion in ids_videos:
            vistas = metrica.get("vistas",0)

        metricas_transformadas.append({      
            "id_publicacion": id_publicacion,
            "alcance": metrica.get("alcance", 0),
            "impresiones": metrica.get("impresiones", 0),
            "vistas": vistas,
            "interacciones": metrica.get("interacciones", 0),
            "likes": metrica.get("likes", 0),
            "shares": metrica.get("shares", 0),
            "comentarios": metrica.get("comentarios", 0),
        })
    
    return metricas_transformadas



