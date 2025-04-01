# 🚀 ETL Automatizado de Redes Sociales para Reportes Presidenciales y de Competencia

Este proyecto tiene como objetivo centralizar, automatizar y estructurar la extracción de datos desde diversas plataformas sociales para generar reportes de alto nivel solicitados por el cliente **CLARO**, tales como el **Reporte Presidencial** (mensual y semanal) y el **Reporte de Competencia**.

---

## 🎯 Propósito del Proyecto

Actualmente, los reportes solicitados por el cliente se generan de forma manual, extrayendo información de múltiples plataformas (como Meta, LinkedIn, X y Talkwalker), filtrando manualmente los datos, copiándolos en Excel y posteriormente creando presentaciones en PowerPoint. Este proceso es lento, propenso a errores y difícil de escalar.

Este proyecto busca resolver esa problemática mediante:

- Extracción automatizada de datos desde APIs oficiales
- Estandarización de datos en un Data Warehouse (SQL Server)
- Orquestación de los procesos con Apache Airflow
- Generación de dashboards en Power BI para visualización de KPIs

---

## 🧩 Fuentes de Datos Integradas (APIs)

- **Meta Graph API** (Facebook + Instagram)
- **X (ex Twitter) API**
- **LinkedIn API**
- **Talkwalker API** (para análisis de sentimiento y métricas)

---

## 🧱 Esquema del Data Warehouse

Se crearán tablas estructuradas para:

- 📄 Publicaciones por red social
- 💬 Comentarios clasificados por sentimiento
- 🎯 Métricas de alcance, impresiones, engagement
- 📸 Archivos multimedia descargados por publicación
- 🧠 Sentimiento cruzado entre Talkwalker y redes sociales

> El diseño del esquema permitirá crear reportes dinámicos y comparativos, como:
> - Evolución de métricas por canal
> - Volumen de publicaciones por tipo
> - Análisis de competencia (post a post)
> - Percepción del sentimiento público

---

## ⚙️ Automatización con Airflow

El proyecto se orquesta mediante **Apache Airflow**, permitiendo:

- Ejecución automática de tareas ETL por red social
- Registro de logs y errores
- Control de versiones y modularidad
- Tareas escalables y mantenibles

---

## 📊 Visualización con Power BI

Una vez los datos estén estructurados en el Data Warehouse, se construirán dashboards en Power BI, conectados directamente a SQL Server, lo que permitirá:

- Reportes actualizados automáticamente
- Visualización comparativa entre canales y periodos
- Paneles separados para el cliente y el equipo interno

---

## 📂 Estructura del Proyecto

```plaintext
proyecto_etl/
├── etl/
│   ├── facebook/
│   ├── linkedin/
│   ├── talkwalker/
│   ├── x/
│   └── utils/
├── dags/
├── config/
├── data/
├── logs/
└── README.md
