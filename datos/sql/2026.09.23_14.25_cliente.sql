create table cliente (
    id_cliente serial primary key,
    nombre varchar(255) not null,
    rut varchar(20) unique not null,
    telefono varchar(20),
    correo varchar(255)
);