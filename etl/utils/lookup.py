import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from etl.utils.sql_connection import get_sql_connection

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