import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from etl.utils.sql_connection import get_sql_connection


# En este archivo se almacenan funciones de busqueda o consulta a la base de datos para obteners IDs, claves foránes, nombres o mmapings

def obtener_id_fuente(nombre_fuente):
    conn = get_sql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id_fuente FROM fuentes WHERE nombre_fuente = ?", nombre_fuente)
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def obtener_id_red_social(nombre_red):
    conn = get_sql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id_red_social FROM redes_sociales WHERE nombre_red = ?", nombre_red)
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def obtener_ids_videos():
    conn = get_sql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id_publicacion FROM publicaciones WHERE tipo_contenido = 'video'")
    result = cursor.fetchall()
    conn.close()
    return [row[0] for row in result] if result else[]