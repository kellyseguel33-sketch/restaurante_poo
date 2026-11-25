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
        return EstadoReserva.get_or_none(EstadoReserva.id_estadoreserva == id_estadoreservas)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def guardar_estadoreserva(estado_reserva: EstadoReserva):
    try:
        if estado_reserva.save():
            print(f'Estado de reserva "{estado_reserva.estado}" guardado correctamente.')
            return estado_reserva
    except Exception as error:
        print(f'{mensaje_error}{error}')
