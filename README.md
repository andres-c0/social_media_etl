# 🚀 ETL Automatizado de Redes Sociales para Reportes Presidenciales y de Competencia

Este proyecto tiene como objetivo centralizar, automatizar y estructurar la extracción de datos desde diversas plataformas sociales para generar reportes de alto nivel solicitados por el cliente. Los cuales muestran información acerca del rendimiento que la empresa esta obteniendo en las campañas de marketing por el canal mencionado.

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
- **Email Octopus API** (para análisis de campañas de marketing)

### ✉️ Email Octopus (Automatización de Campañas)

Además de redes sociales, el proyecto también integra el rendimiento de campañas de email marketing realizadas con Email Octopus, incluyendo:

- Número de aperturas
- Número de clics
- Desuscripciones
- Rebotes
- Link de visualización del correo

Esto permitirá eliminar el proceso manual de toma de screenshots y generación de presentaciones. Toda esta información será capturada por medio de la API oficial y cargada al Data Warehouse para alimentar los dashboards en Power BI.

---

## 🧱 Esquema del Data Warehouse

📂 [sql/00_crear_tablas_dw.sql](sql/00_crear_tablas_dw.sql): Script para crear todas las tablas del Data Warehouse.
🖼️ [`sql/modelo_ER.png`](sql/modelo_ER.png): Diagrama Entidad-Relación del esquema.


Se crearán tablas estructuradas para:

- 📄 Publicaciones por red social
- 💬 Comentarios clasificados por sentimiento
- 🎯 Métricas de alcance, impresiones, engagement
- 📸 Archivos multimedia descargados por publicación
- 🧠 Sentimiento cruzado entre Talkwalker y redes sociales
- ✉️ Métricas de campañas de marketing via Mail

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
├── sql/
├── .env.example
└── README.md
```
---

## 🔧 Configuración del entorno (`.env`)

Antes de ejecutar, se debera crear un archivo  `.env` en la raíz del proyecto basado en el `.env.example`:

```env
SQL_SERVER=localhost
SQL_DATABASE=digitas_dw
SQL_USER=usuario
SQL_PASSWORD=contraseña
FB_TOKEN=tu_token_de_facebook
```

---

## 💻 Requerimientos minimos

El equipo en donde se ejecutaran los scripts escritos en este repositorio debera contar con los siguientes requerimientos minimos:

- Visual Studio Code `v1.98.0`

- SQL Server 2022

- SQL Server Management Studio	`v20.2.30.0`

- Python `v3.13`


---

## 🛡️ Seguridad del Repositorio

- 🔒 .env no está versionado (configurado en .gitignore)

- ✅ No se expone ningún token o credencial

- 🧪 Secret scanning activado en GitHub

- 👤 Solo el autor tiene permisos de push a main

---

## 📬 Contacto

Este proyecto fue desarrollado como parte de mi experiencia profesional en automatización de datos y marketing digital.  
Podés ver más proyectos en [mi perfil de GitHub](https://github.com/andres-c0) o contactarme en caso de interés profesional.



