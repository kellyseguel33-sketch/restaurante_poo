CREATE TABLE direccion(
    id_direccion int not null primary key,
    calle varchar(250) not null,
    numero int not null,
    ciudad varchar(100) not null,
    comuna varchar(100) not null,
    detalles text
);