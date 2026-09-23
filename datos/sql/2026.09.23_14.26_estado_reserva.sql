create table estado_reserva (
    id_estado_reserva serial primary key,
    estado varchar(50) not null,
    descripcion text
);