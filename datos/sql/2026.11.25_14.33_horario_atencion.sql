CREATE TABLE horario_atencion(
    id_horario SERIAL PRIMARY KEY,
    hora_apertura VARCHAR(10) NOT NULL,
    hora_cierre VARCHAR(10) NOT NULL,
    dias_semana VARCHAR(20) NOT NULL
);