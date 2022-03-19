CREATE SEQUENCE seq_pacientes;
CREATE SEQUENCE seq_detecciones;
CREATE SEQUENCE seq_det_img;
CREATE SEQUENCE seq_imagenes;
CREATE SEQUENCE seq_observaciones;
CREATE SEQUENCE seq_doctores;

CREATE TABLE "PACIENTES" 
(   
	id bigint PRIMARY KEY DEFAULT nextval('seq_pacientes'),
	str_nombres varchar(200) NOT NULL,
	str_apellidos varchar(200) NOT NULL,
	str_tipo_documento varchar(10) NOT NULL,
	str_identificacion varchar(100) NOT NULL,
	str_genero varchar(50) ,
	dt_fecha_insert timestamp NOT NULL,
	dt_fecha_update timestamp NOT NULL,
	bl_dlete numeric(1) DEFAULT 0
);

CREATE TABLE "DETECCIONES" 
(   
	id bigint PRIMARY KEY DEFAULT nextval('seq_detecciones'),
	paciente_id bigint NOT NULL,
	num_probabilidad float NOT NULL,
	str_tipo_bacteria varchar(100) NOT NULL,
	dt_fecha_insert timestamp NOT NULL,
	dt_fecha_update timestamp NOT NULL,
	bl_dlete numeric(1) DEFAULT 0
);

CREATE TABLE "IMAGENES" 
(  
	id bigint PRIMARY KEY DEFAULT nextval('seq_imagenes'),
	str_nombre varchar(500) NOT NULL,
	str_extension varchar(50) NOT NULL,
	str_path varchar(500) NOT NULL,
	num_tamano numeric(50) NOT NULL,
	dt_fecha_insert timestamp NOT NULL,
	dt_fecha_update timestamp NOT NULL,
	bl_dlete numeric(1) DEFAULT 0
);

CREATE TABLE "DET_IMG" 
(   
	id bigint PRIMARY KEY DEFAULT nextval('seq_det_img'),
	deteccion_id bigint NOT NULL,
	imagen_id bigint NOT NULL,
	dt_fecha_insert timestamp NOT NULL,
	dt_fecha_update timestamp NOT NULL,
	bl_dlete numeric(1) DEFAULT 0
);

CREATE TABLE "DOCTORES" 
( 
	id bigint PRIMARY KEY DEFAULT nextval('seq_doctores'),
	str_nombres varchar(200) NOT NULL,
	str_apellidos varchar(200) NOT NULL,
	str_tipo_documento varchar(10) NOT NULL,
	str_identificacion varchar(100) NOT NULL,
	str_genero varchar(50),
	str_cargo varchar(50),
	dt_fecha_insert timestamp NOT NULL,
	dt_fecha_update timestamp NOT NULL,
	bl_dlete numeric(1) DEFAULT 0
);


CREATE TABLE "OBSERVACIONES" 
( 
	id bigint PRIMARY KEY DEFAULT nextval('seq_observaciones'),
	doctor_id bigint NOT NULL,
	deteccion_id bigint NOT NULL,
	str_observacion varchar(4000) NOT NULL,
	dt_fecha_insert timestamp NOT NULL,
	dt_fecha_update timestamp NOT NULL,
	bl_dlete numeric(1) DEFAULT 0
);
COMMIT;
