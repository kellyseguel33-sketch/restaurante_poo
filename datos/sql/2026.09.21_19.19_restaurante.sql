create table restaurante (
    id_restaurante serial primary key,
    nombre varchar(255) not null,
    id_direccion int references direccion(id_direccion) on delete set null,
    id_horario int references horario_atencion(id_horario) on delete set null
);