 USE digitas_dw

 CREATE TABLE fuentes(
	id_fuente INT NOT NULL,
	nombre_fuente NVARCHAR(255) NOT NULL,
	tipo_fuente NVARCHAR(255) NOT NULL,
	fecha_creacion DATETIME DEFAULT GETDATE()

	CONSTRAINT pk_fuentes PRIMARY KEY (id_fuente)
 )

 CREATE TABLE redes_sociales(
	id_red_social INT NOT NULL,
	nombre_red NVARCHAR(255) NOT NULL,
	fecha_creacion DATETIME DEFAULT GETDATE()

	CONSTRAINT pk_redes_sociales PRIMARY KEY (id_red_social)
 )

 CREATE TABLE publicaciones(
	id_publicacion NVARCHAR(200) NOT NULL,
	id_fuente INT NOT NULL,
	id_red_social INT NOT NULL,
	texto NVARCHAR(MAX) NOT NULL,
	tipo_contenido NVARCHAR(55) NOT NULL,
	fecha_publicacion DATETIME NOT NULL,
	enlace NVARCHAR(MAX) NOT NULL,
	fecha_creacion DATETIME DEFAULT GETDATE()

	CONSTRAINT pk_publicaciones PRIMARY KEY (id_publicacion),
	CONSTRAINT fk_publicaciones_fuentes FOREIGN KEY (id_fuente) REFERENCES fuentes(id_fuente),
	CONSTRAINT fk_publicaciones_redes_sociales FOREIGN KEY (id_red_social) REFERENCES redes_sociales(id_red_social)
 )

 CREATE TABLE comentarios(
	id_comentario NVARCHAR(255) NOT NULL,
	id_publicacion NVARCHAR(200) NOT NULL,
	texto_comentario NVARCHAR(MAX) NOT NULL,
	sentimiento_meta NVARCHAR(55),
	sentimiento_talkwalker NVARCHAR(55),
	fecha_comentario DATETIME NOT NULL,
	fecha_creacion DATETIME DEFAULT GETDATE()

	CONSTRAINT pk_comentarios PRIMARY KEY (id_comentario),
	CONSTRAINT pk_comentarios_publicaciones FOREIGN KEY (id_publicacion) REFERENCES publicaciones(id_publicacion)
 )

 CREATE TABLE metricas_publicacion(
	id_publicacion NVARCHAR(MAX) NOT NULL,
	alcance INT NOT NULL,
	impresiones INT NOT NULL,
	vistas INT NOT NULL,
	engagement INT NOT NULL,
	likes INT NOT NULL,
	shares INT NOT NULL,
	comentarios INT NOT NULL,
	fecha_extraccion DATETIME DEFAULT GETDATE()

	CONSTRAINT pk_metricas_publicacion_publicaciones FOREIGN KEY(id_publicacion) REFERENCES publicaciones(id_publicacion)
 )

 CREATE TABLE multimedia_publicacion(
	id_media INT NOT NULL,
	id_publicacion NVARCHAR(MAX) NOT NULL,
	url_media NVARCHAR(MAX) NOT NULL,
	tipo_media NVARCHAR(55) NOT NULL,
	ruta_local NVARCHAR(MAX) NOT NULL,
	fecha_extraccion DATETIME DEFAULT GETDATE()
	
	CONSTRAINT pk_multimedia_publicacion PRIMARY KEY (id_media),
	CONSTRAINT fk_multimedia_publicacion_publicaciones FOREIGN KEY (id_publicacion) REFERENCES publicaciones(id_publicacion)
 )

 CREATE TABLE audiencia_demografica(
	id_audiencia INT NOT NULL,
	id_fuente INT NOT NULL,
	id_red_social INT NOT NULL,
	pais VARCHAR(255) NOT NULL,
	ciudad VARCHAR(255) NOT NULL,
	genero VARCHAR(2) NOT NULL,
	rango_edad NVARCHAR(55) NOT NULL,
	cantidad_seguidores INT NOT NULL,
	fecha_extraccion DATETIME DEFAULT GETDATE()

	CONSTRAINT pk_audiencia_demografica PRIMARY KEY (id_audiencia),
	CONSTRAINT fk_audiencia_demografica_fuentes FOREIGN KEY (id_fuente) REFERENCES fuentes(id_fuente),
	CONSTRAINT fk_audiencia_demografica_redes_sociales FOREIGN KEY(id_red_social) REFERENCES redes_sociales(id_red_social)
 )

 CREATE TABLE campanias_email_octopus(
	id_campania INT NOT NULL,
	nombre_campania NVARCHAR(255) NOT NULL,
	asunto NVARCHAR(MAX) NOT NULL,
	fecha_envio DATETIME NOT NULL,
	total_enviados INT NOT NULL,
	total_abiertos INT NOT NULL,
	total_clicks INT NOT NULL,
	total_desuscritos INT NOT NULL,
	total_rebotes INT NOT NULL,
	url_preview NVARCHAR(MAX) NOT NULL,
	fecha_creacion DATETIME DEFAULT GETDATE()

	CONSTRAINT pk_campanias_email_octopus PRIMARY KEY (id_campania)
 )








