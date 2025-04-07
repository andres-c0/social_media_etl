import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from etl.utils.sql_connection import get_sql_connection

def cargar_comentarios(comentarios):
    if not comentarios:
        print("⚠️ No hay comentarios para cargar.")
        return
    
    conn = get_sql_connection()
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO comentarios (
            id_comentario,
            id_publicacion,
            texto_comentario,
            sentimiento_meta,
            sentimiento_talkwalker,
            fecha_comentario
        )
        VALUES(?,?,?,?,?,?)
    """

    for com in comentarios:
        try:
            cursor.execute(insert_query, (
                com["id_comentario"],
                com["id_publicacion"],
                com["texto_comentario"],
                com["sentimiento_meta"],
                com["sentimiento_talkwalker"],
                com["fecha_comentario"]
            ))
        except Exception as e:
            print(f"❌ Error insertando comentario {com['id_comentario']}: {e}")

    conn.commit()
    cursor.close()
    conn.close()
    print(f"✅ Comentarios insertados: {len(comentarios)}")

