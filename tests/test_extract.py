import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from etl.facebook.extract import extraer_publicaciones

posts = extraer_publicaciones("Claro Nicaragua")
for post in posts:
    print(post)