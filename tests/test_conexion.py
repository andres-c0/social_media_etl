import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from etl.utils.sql_connection import get_sql_connection

conn = get_sql_connection()

if conn:
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 5  * FROM fuentes")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close


#PRUEBA