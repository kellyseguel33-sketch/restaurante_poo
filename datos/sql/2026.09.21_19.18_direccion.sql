CREATE TABLE direccion(
    id_direccion serial primary key,
    calle varchar(255) not null,
    numero int not null,
    ciudad varchar(100) not null,
    comuna varchar(100) not null,
    detalles text
);