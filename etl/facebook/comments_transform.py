from datetime import datetime

def transformar_comentarios(comentarios_json):
    comentarios_transformados = []

    for com in comentarios_json:
        fecha_raw = com.get("fecha_comentario")

        fecha_convertida = None
        if fecha_raw:
            fecha_convertida = datetime.strptime(fecha_raw, "%Y-%m-%dT%H:%M:%S%z").replace(tzinfo=None)
        
        comentarios_transformados.append({
            "id_comentario": com.get("id_comentario"),
            "id_publicacion": com.get("id_publicacion"),
            "texto_comentario": com.get("texto_comentario", "").strip(),
            "sentimiento_meta": None,
            "sentimiento_talkwalker": None,
            "fecha_comentario": fecha_convertida
        })

    return comentarios_transformados