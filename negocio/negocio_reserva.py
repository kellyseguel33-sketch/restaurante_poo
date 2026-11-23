from prettytable import PrettyTable
from datos.repositorio.repositorio_reserva import listado_reservas, guardar_reserva
from datos.modelos.reserva import Reserva
from datos.modelos.mesa import Mesa
from auxiliares import mensaje_error
from datetime import datetime
from datos.repositorio.repositorio_reserva import obtener_reserva_por_id
from datos.repositorio.repositorio_restaurante import obtener_restaurante_id
from datos.repositorio.repositorio_mesa import obtener_mesa_por_id
from datos.repositorio.repositorio_direccion import obtener_direccion_por_id
from auxiliares import mensaje_error

def procesar_listado_reservas(tabla: PrettyTable):
    if tabla:
        tabla.field_names = ['Id', 'Fecha', 'Hora', 'Personas', 'Restaurante', 'Cliente', 'Mesa', 'Estado']
        lista_reservas = listado_reservas()
        if lista_reservas:
            for reserva in lista_reservas:
                tabla.add_row([
                    reserva.id_reserva,
                    reserva.fecha,
                    reserva.hora,
                    reserva.cantidad_personas,
                    reserva.id_restaurante,
                    reserva.id_cliente,
                    reserva.id_mesa,
                    reserva.id_estado_reserva
                ])
            return tabla


def obtener_mesas_disponibles(fecha, hora):
    try:
        # Corregido: Se envuelven todas las condiciones correctamente dentro del .where(...)
        mesas_ocupadas_ids = (
            Reserva.select(Reserva.id_mesa)
            .where(
                (Reserva.fecha == fecha) & 
                (Reserva.hora == hora) & 
                (Reserva.id_mesa.is_null(False))
            )
        ) 
        ids_ocupados = [r.id_mesa for r in mesas_ocupadas_ids]

        # Si hay mesas ocupadas, las filtramos; si no, trae todas las mesas
        if ids_ocupados:
            mesas_disponibles = Mesa.select().where(~Mesa.id_mesa.in_(ids_ocupados))
        else:
            mesas_disponibles = Mesa.select()
            
        return mesas_disponibles
    except Exception as error:
        print(f'Error al consultar mesas disponibles: {error}')
        return []


def crear_objeto_reserva(fecha, hora: str, cantidad_personas: int, id_restaurante: int, id_cliente: int, id_mesa: int, id_estado_reserva: int):
    try:
        guardar_reserva(
            id_restaurante=id_restaurante,
            fecha=fecha,
            hora=hora,
            cantidad_personas=cantidad_personas,
            id_cliente=id_cliente,
            id_estado_reserva=id_estado_reserva,
            id_mesa=id_mesa
        )
    except Exception as error:
        print(f'{mensaje_error}{error}')


def modificar_objeto_reserva(fecha, hora: str, cantidad_personas: int, id_restaurante: int, id_cliente: int, id_mesa: int, id_estado_reserva: int, reserva: Reserva):
    try:
        if fecha != '':
            reserva.fecha = fecha
        if hora != '':
            reserva.hora = hora
        if cantidad_personas != '':
            reserva.cantidad_personas = cantidad_personas
        if id_restaurante != '':
            reserva.id_restaurante = id_restaurante
        if id_cliente != '':
            reserva.id_cliente = id_cliente
        if id_mesa != '':
            reserva.id_mesa = id_mesa
        if id_estado_reserva != '':
            reserva.id_estado_reserva = id_estado_reserva
            
        reserva.save()
        print('¡Reserva actualizada correctamente!')
    except Exception as error:
        print(f'{mensaje_error}{error}')

def generar_boleta_reserva(id_reserva: int, precio_por_persona: int = 0):
    try:
        reserva = obtener_reserva_por_id(id_reserva)
        if not reserva:
            return None

        restaurante = obtener_restaurante_id(reserva.id_restaurante)
        mesa = obtener_mesa_por_id(reserva.id_mesa) if reserva.id_mesa else None
        direccion = (
            obtener_direccion_por_id(restaurante.id_direccion)
            if restaurante and getattr(restaurante, 'id_direccion', None)
            else None
        )

        total = reserva.cantidad_personas * precio_por_persona

        lineas = [
            '=' * 44,
            '          BOLETA / COMPROBANTE DE RESERVA',
            '=' * 44,
            f'N° Reserva : {reserva.id_reserva}',
            f'Emitida el : {datetime.now().strftime("%d/%m/%Y %H:%M")}',
            '-' * 44,
            f'Restaurante: {restaurante.nombre if restaurante else f"ID {reserva.id_restaurante}"}',
        ]

        if direccion:
            lineas.append(f'Dirección  : {direccion.calle} #{direccion.numero}, {direccion.comuna}')

        lineas.extend([
            f'Fecha      : {reserva.fecha}',
            f'Hora       : {reserva.hora}',
            f'Personas   : {reserva.cantidad_personas}',
            f'Mesa       : {f"N° {mesa.numero} ({mesa.ubicacion or \"Sin ubicación\"})" if mesa else "Por asignar"}',
            f'Estado ID  : {reserva.id_estado_reserva}',
            f'Cliente ID : {reserva.id_cliente}',
        ])

        if precio_por_persona > 0:
            lineas.extend([
                '-' * 44,
                f'Valor por persona : ${precio_por_persona:,}'.replace(',', '.'),
                f'Total estimado    : ${total:,}'.replace(',', '.'),
            ])

        lineas.extend([
            '=' * 44,
            '     ¡Gracias por preferir nuestro restaurante!',
            '=' * 44,
        ])

        return '\n'.join(lineas)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None