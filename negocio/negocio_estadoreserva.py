from prettytable import PrettyTable
from datos.repositorio.repositorio_estadoreserva import listado_estadoreserva, guardar_estadoreserva
from datos.modelos.estadoreserva import EstadoReserva
from auxiliares import mensaje_error


def procesar_listado_estadosreserva(tabla: PrettyTable):
    if tabla:
        tabla.field_names = ['Id', 'Estado', 'Descripción']
        lista_estados = listado_estadoreserva()
        if lista_estados:
            for est in lista_estados:
                tabla.add_row([
                    est.id_estado_reserva,
                    est.estado,
                    est.descripcion
                ])
            return tabla


def crear_objeto_estadoreserva(estado: str, descripcion: str):
    try:
        estado_reserva = EstadoReserva(
            estado=estado,
            descripcion=descripcion
        )
        guardar_estadoreserva(estado_reserva)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def modificar_objeto_estadoreserva(estado: str, descripcion: str, estado_reserva: EstadoReserva):
    try:
        if estado_reserva.estado != estado and estado != '':
            estado_reserva.estado = estado
        if estado_reserva.descripcion != descripcion and descripcion != '':
            estado_reserva.descripcion = descripcion
            
        guardar_estadoreserva(estado_reserva)
    except Exception as error:
        print(f'{mensaje_error}{error}')