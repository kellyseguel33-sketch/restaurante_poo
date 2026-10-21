from datos.modelos.estadoreserva import EstadoReserva
from auxiliares import mensaje_error

def listado_estadoreserva():
    try:
        estados = EstadoReserva.select()
        if estados:
            return estados
    except Exception as error:
            print(f'{mensaje_error}{error}')

def obtener_estadoreservas_por_id(id_estadoreservas):
    try:
        estado = EstadoReserva.get(EstadoReserva.id_estado_reserva == id_estadoreservas)
        if estado:
            return estado
    except Exception as error:
        print(f'{mensaje_error}{error}')


def guardar_estadoreserva(estado, descripcion):
    try:
        respuesta = EstadoReserva.save(estado=estado, descripcion=descripcion)
        if respuesta:
            print(f'Estado de reserva {estado} guardado correctamente.')
    except Exception as error:
        print(f'{mensaje_error}{error}')