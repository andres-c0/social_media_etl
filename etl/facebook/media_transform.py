import os
import requests

def transformar_multimedia(lista_multimedia, carpeta_base="data/multimedia"):
    resultados = []

    for item in lista_multimedia:
        id_publicacion = item["id_publicacion"]
        tipo_media = item["tipo_media"]
        url_media = item["url_media"]

        carpeta_destino = os.path.join(carpeta_base, id_publicacion)
        os.makedirs(carpeta_destino, exist_ok=True)

        nombre_archivo = url_media.split("/")[-1].split("?")[0]
        ruta_local = os.path.join(carpeta_destino, nombre_archivo)

        try:
            response = requests.get(url_media, timeout=10)
            response.raise_for_status()

            with open(ruta_local, 'wb') as f:
                f.write(response.content)

            resultados.append({
                "id_publicacion": id_publicacion,
                "tipo_media": tipo_media,
                "url_media": url_media,
                "ruta_local": ruta_local
            })

        except Exception as e:
            print(f"⚠️ Error al descargar {url_media}: {e}")
        
    return resultados

