from prettytable import PrettyTable
from auxiliares import mensaje_error
from negocio import procesar_listado_reservas
from datos.repositorio.repositorio_reserva import obtener_reserva_por_id
from negocio import crear_objeto_reserva, modificar_objeto_reserva

def mostrar_listado_reservas():
    try:
        tabla_reservas = PrettyTable()
        tabla_reservas = procesar_listado_reservas(tabla_reservas)
        print(tabla_reservas)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def crear_reserva():
    fecha, hora, cantidad_personas, id_restaurante, id_cliente, id_mesa, id_estado_reserva = '', '', '', '', '', '', ''
    
    while fecha == '':
        fecha = input('Ingrese fecha (YYYY-MM-DD): ')
    while hora == '':
        hora = input('Ingrese hora (ej. 20:00): ')
    while cantidad_personas == '':
        cantidad_personas = input('Ingrese cantidad de personas: ')
    while id_restaurante == '':
        id_restaurante = input('Ingrese ID del restaurante: ')
    while id_cliente == '':
        id_cliente = input('Ingrese ID del cliente: ')
    while id_estado_reserva == '':
        id_estado_reserva = input('Ingrese ID del estado de reserva: ')
        
    id_mesa = input('Ingrese ID de la mesa [o ENTER para omitir]: ')
    
    crear_objeto_reserva(
        fecha, 
        hora, 
        int(cantidad_personas), 
        int(id_restaurante), 
        int(id_cliente), 
        int(id_mesa) if id_mesa != '' else None, 
        int(id_estado_reserva)
    )

def modificar_reserva():
    mostrar_listado_reservas()
    id_r = input('Ingrese ID de la reserva a modificar: ')
    reserva = obtener_reserva_por_id(id_r)
    if reserva:
        print('Reserva Encontrada:')
        print(f'Reserva N° {reserva.id_reserva} - Fecha: {reserva.fecha} - Hora: {reserva.hora}')
        
        fecha, hora, cantidad_personas, id_restaurante, id_cliente, id_mesa, id_estado_reserva = '', '', '', '', '', '', ''
        
        while fecha == '':
            fecha = input('Ingrese nueva fecha [o ENTER para conservar]: ')
        while hora == '':
            hora = input('Ingrese nueva hora [o ENTER para conservar]: ')
        while cantidad_personas == '':
            cantidad_personas = input('Ingrese nueva cantidad de personas [o ENTER para conservar]: ')
        while id_restaurante == '':
            id_restaurante = input('Ingrese nuevo ID de restaurante [o ENTER para conservar]: ')
        while id_cliente == '':
            id_cliente = input('Ingrese nuevo ID de cliente [o ENTER para conservar]: ')
        while id_mesa == '':
            id_mesa = input('Ingrese nuevo ID de mesa [o ENTER para conservar]: ')
        while id_estado_reserva == '':
            id_estado_reserva = input('Ingrese nuevo ID de estado de reserva [o ENTER para conservar]: ')
            
        modificar_objeto_reserva(
            fecha if fecha != '' else reserva.fecha,
            hora if hora != '' else reserva.hora,
            int(cantidad_personas) if cantidad_personas != '' else reserva.cantidad_personas,
            int(id_restaurante) if id_restaurante != '' else reserva.id_restaurante,
            int(id_cliente) if id_cliente != '' else reserva.id_cliente,
            int(id_mesa) if id_mesa != '' else reserva.id_mesa,
            int(id_estado_reserva) if id_estado_reserva != '' else reserva.id_estado_reserva,
            reserva
        )

def eliminar_reserva():
    mostrar_listado_reservas()
    id_r = input('Ingrese ID de la reserva a eliminar: ')
    reserva = obtener_reserva_por_id(id_r)
    if reserva:
        print('Se eliminará la reserva:')
        print(f'Reserva N° {reserva.id_reserva} - Fecha: {reserva.fecha} a las {reserva.hora}')
        confirmacion = input('¿Está seguro de eliminar? (s/n): ').lower()
        if confirmacion == 's':
            try:
                reserva.delete_instance()
                print('¡Reserva eliminada con éxito!')
            except Exception as error:
                print(f'{mensaje_error}{error}')
        else:
            print('Operación cancelada.')