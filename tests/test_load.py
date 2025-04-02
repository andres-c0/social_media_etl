import sys
import os
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from etl.facebook.extract import extraer_publicaciones
from etl.facebook.transform import transformar_publicaciones
from etl.facebook.load import cargar_publicaciones

inicio = datetime(2025, 3, 1)
fin = datetime(2025, 3, 10)

posts = extraer_publicaciones("Claro Nicaragua", inicio, fin)
transformados = transformar_publicaciones(posts, "Claro Nicaragua", "Facebook")
cargar_publicaciones(transformados)



