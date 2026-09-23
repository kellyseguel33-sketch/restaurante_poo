create table mesa (
    id_mesa serial primary key,
    id_restaurante int not null references restaurante(id_restaurante) on delete cascade,
    numero int not null,
    capacidad int not null,
    ubicacion varchar(100)
);