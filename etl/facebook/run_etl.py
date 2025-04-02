import sys
import os
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from etl.facebook.extract import extraer_publicaciones
from etl.facebook.transform import transformar_publicaciones
from etl.facebook.load import cargar_publicaciones


def ejecutar_etl_facebook(nombre_pagina, nombre_fuente, nombre_red_social,
                          fecha_inicio=None, fecha_fin=None,
                          extraer_publicaciones=True,
                          extraer_comentarios=False,
                          extraer_metricas=False,
                          extraer_multimedia=False,
                          extraer_audiencia=False):
    print(f"\n🚀 Iniciando ETL para la página: {nombre_pagina}")

    if extraer_publicaciones:
        print("📥 Extrayendo publicaciones...")
        publicaciones_crudas = extraer_publicaciones(nombre_pagina, fecha_inicio, fecha_fin)
        print(f"📄 Publicaciones extraídas: {len(publicaciones_crudas)}")

        if not publicaciones_crudas:
            print("⚠️ No se encontraron publicaciones. Proceso detenido.")
            return

        print("🧼 Transformando publicaciones...")
        publicaciones_transformadas = transformar_publicaciones(publicaciones_crudas, nombre_fuente, nombre_red_social)
        print(f"🧾 Publicaciones transformadas: {len(publicaciones_transformadas)}")

        print("💾 Cargando publicaciones en SQL Server...")
        cargar_publicaciones(publicaciones_transformadas)
        print("✅ Publicaciones insertadas correctamente.")

    if extraer_comentarios:
        print("💬 Extrayendo y cargando comentarios... (pendiente desarrollo)")

    if extraer_metricas:
        print("📊 Extrayendo y cargando métricas... (pendiente desarrollo)")

    if extraer_multimedia:
        print("🖼️ Descargando y cargando multimedia... (pendiente desarrollo)")

    if extraer_audiencia:
        print("🌍 Extrayendo y cargando audiencia demográfica... (pendiente desarrollo)")

    print("🏁 ETL de Facebook finalizado.\n")


if __name__ == "__main__":
    # Podés probar con fechas reales o por defecto
    fecha_inicio = None
    fecha_fin = None

    ejecutar_etl_facebook(
        nombre_pagina="Claro Nicaragua",
        nombre_fuente="Claro Nicaragua",
        nombre_red_social="Facebook",
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        extraer_publicaciones=True,
        extraer_comentarios=False,
        extraer_metricas=False,
        extraer_multimedia=False,
        extraer_audiencia=False
    )
