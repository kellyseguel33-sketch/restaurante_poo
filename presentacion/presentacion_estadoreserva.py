from prettytable import PrettyTable
from auxiliares import mensaje_error
from negocio.negocio_estadoreserva import (procesar_listado_estadosreserva, crear_objeto_estadoreserva, modificar_objeto_estadoreserva)
from datos.repositorio.repositorio_estadoreserva import obtener_estadoreservas_por_id

def mostrar_listado_estados_reserva():
    try:
        tabla_estados = PrettyTable()
        tabla_estados = procesar_listado_estadosreserva(tabla_estados)
        print(tabla_estados)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_estadoreserva():
    estado, descripcion = '', ''
    
    while estado == '':
        estado = input('Ingrese estado: ')
    while descripcion == '':
        descripcion = input('Ingrese descripción: ')
        
    crear_objeto_estadoreserva(estado, descripcion)


def modificar_estadoreserva():
    mostrar_listado_estados_reserva()
    estado_buscar = input('Ingrese el estado a modificar: ')
    estado_reserva = obtener_estadoreservas_por_id(estado_buscar)
    
    if estado_reserva:
        print('Estado de Reserva Encontrado:')
        print(f'Estado: {estado_reserva.estado} | Descripción: {estado_reserva.descripcion}')
        
        estado, descripcion = '', ''
        
        while estado == '':
            estado = input('Ingrese nuevo estado [o ENTER para conservar]: ')
        while descripcion == '':
            descripcion = input('Ingrese nueva descripción [o ENTER para conservar]: ')
            
        modificar_objeto_estadoreserva(estado, descripcion, estado_reserva)


def eliminar_estadoreserva():
    mostrar_listado_estados_reserva()
    estado_buscar = input('Ingrese el estado a eliminar: ')
    estado_reserva = obtener_estadoreservas_por_id(estado_buscar)
    
    if estado_reserva:
        print(f'Se eliminará el estado de reserva: {estado_reserva.estado}')
        confirmacion = input('¿Está seguro de eliminar? (s/n): ').lower()
        
        if confirmacion == 's':
            try:
                estado_reserva.delete_instance()
                print('¡Estado de reserva eliminado con éxito!')
            except Exception as error:
                print(f'{mensaje_error}{error}')
        else:
            print('Operación cancelada.')