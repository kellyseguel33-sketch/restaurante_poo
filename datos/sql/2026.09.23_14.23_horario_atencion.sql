CREATE TABLE horario_atencion(
id_direccion SERIAL PRIMARY KEY,
hora_apertura varchar(10) NOT NULL,
hora_cierre VARCHAR(10) NOT NULL,
dias_semana VARCHAR(20) NOT NULL
);