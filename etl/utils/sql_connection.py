import pyodbc
import os
from dotenv import load_dotenv

# Se cargan las variables de conexion desde el archivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '../../config/.env')
load_dotenv(dotenv_path)

def get_sql_connection():
    try:
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={os.getenv('SQL_SERVER')};"
            f"DATABASE={os.getenv('SQL_DATABASE')};"
            f"UID={os.getenv('SQL_USER')};"
            f"PWD={os.getenv('SQL_PASSWORD')};"
            "TrustServerCertificate=yes;"
        )
        print("✅ Conexión a SQL Server exitosa.")
        return conn
    except Exception as e:
        print("❌ Error al conectar con SQL Server:", e)
        return None
