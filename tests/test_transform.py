import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from etl.facebook.extract import extraer_publicaciones
from etl.facebook.transform import transformar_publicaciones

posts = extraer_publicaciones("Claro Nicaragua")
transformados = transformar_publicaciones(posts, "Claro Nicaragua", "Facebook")

for pub in transformados:
    print(pub)