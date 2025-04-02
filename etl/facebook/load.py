import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from etl.utils.sql_connection import get_sql_connection

def cargar_publicaciones(publicaciones):
    if not publicaciones:
        print("⚠️ No hay publicaciones para insertar.")
        return
    
    try:
        conn = get_sql_connection()
        cursor = conn.cursor()

        for pub in publicaciones:
            try:
                cursor.execute("""
                    IF NOT EXISTS (
                        SELECT 1 FROM publicaciones WHERE id_publicacion = ?
                    )
                    INSERT INTO publicaciones (
                        id_publicacion,
                        id_fuente,
                        id_red_social,
                        texto,
                        tipo_contenido,
                        fecha_publicacion,
                        enlace
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    pub["id_publicacion"],
                    pub["id_publicacion"],
                    pub["id_fuente"],
                    pub["id_red_social"],
                    pub["texto"],
                    pub["tipo_contenido"],
                    pub["fecha_publicacion"],
                    pub["enlace"],
                ))
            except Exception as e:
                print(f"❌ Error insertando publicación {pub['id_publicacion']}: {e}")

        conn.commit()
        print("✅ Inserción de publicaciones completada.")
    except Exception as e:
        print("❌ Error general al conectar o insertar:", e)
    finally:
        if conn:
            conn.close()



