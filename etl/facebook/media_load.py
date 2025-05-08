import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from etl.utils.sql_connection import get_sql_connection

def cargar_multimedia(multimedia_transformada):
    conn = get_sql_connection()
    cursor = conn.cursor()

    for media in multimedia_transformada:
        try:
            cursor.execute("""
                INSERT INTO multimedia_publicacion (
                    id_publicacion,
                    url_media,
                    tipo_media,
                    ruta_local
                ) VALUES (?, ?, ?, ?)
            """, (
                #media["id_media"],
                media["id_publicacion"],
                media["url_media"],
                media["tipo_media"],
                media["ruta_local"]
            ))
        except Exception as e:
            print(f"❌ Error insertando multimedia {media['id_media']}: {e}")

    conn.commit()
    cursor.close()
    print("✅ Inserción de archivos multimedia completada.")

