CREATE TABLE reserva(
    id_reserva SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    hora VARCHAR(10) NOT NULL,
    cantidad_personas INT NOT NULL,
    id_restaurante INT NOT NULL REFERENCES restaurante(id_restaurante),
    id_cliente INT NOT NULL REFERENCES cliente(id_cliente),
    id_mesa INT REFERENCES mesa(id_mesa) ON DELETE SET NULL,
    id_estado_reserva INT NOT NULL REFERENCES estado_reserva(id_estado_reserva)
);