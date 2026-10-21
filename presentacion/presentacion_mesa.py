from prettytable import PrettyTable
from auxiliares import mensaje_error
from negocio import procesar_listado_mesas
from datos.repositorio.repositorio_mesa import obtener_mesa_por_id
from negocio import crear_objeto_mesa, modificar_objeto_mesa

def mostrar_listado_mesas():
    try:
        tabla_mesas = PrettyTable()
        tabla_mesas = procesar_listado_mesas(tabla_mesas)
        print(tabla_mesas)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def crear_mesa():
    id_restaurante, numero, capacidad, ubicacion = '', '', '', ''
    
    while id_restaurante == '':
        id_restaurante = input('Ingrese ID del restaurante: ')
    while numero == '':
        numero = input('Ingrese número de mesa: ')
    while capacidad == '':
        capacidad = input('Ingrese capacidad de personas: ')
        
    ubicacion = input('Ingrese ubicación [o ENTER para omitir]: ')
    
    crear_objeto_mesa(
        int(id_restaurante), 
        int(numero), 
        int(capacidad), 
        ubicacion if ubicacion != '' else None
    )

def modificar_mesa():
    mostrar_listado_mesas()
    id_m = input('Ingrese ID de la mesa a modificar: ')
    mesa = obtener_mesa_por_id(id_m)
    if mesa:
        print('Mesa Encontrada:')
        print(f'Mesa N° {mesa.numero} - Capacidad: {mesa.capacidad}')
        
        id_restaurante, numero, capacidad, ubicacion = '', '', '', ''
        
        while id_restaurante == '':
            id_restaurante = input('Ingrese nuevo ID de restaurante [o ENTER para conservar]: ')
        while numero == '':
            numero = input('Ingrese nuevo número de mesa [o ENTER para conservar]: ')
        while capacidad == '':
            capacidad = input('Ingrese nueva capacidad [o ENTER para conservar]: ')
        while ubicacion == '':
            ubicacion = input('Ingrese nueva ubicación [o ENTER para conservar]: ')
            
        modificar_objeto_mesa(
            int(id_restaurante) if id_restaurante != '' else mesa.id_restaurante,
            int(numero) if numero != '' else mesa.numero,
            int(capacidad) if capacidad != '' else mesa.capacidad,
            ubicacion,
            mesa
        )

def eliminar_mesa():
    mostrar_listado_mesas()
    id_m = input('Ingrese ID de la mesa a eliminar: ')
    mesa = obtener_mesa_por_id(id_m)
    if mesa:
        print('Se eliminará la mesa:')
        print(f'Mesa N° {mesa.numero} - Capacidad: {mesa.capacidad}')
        confirmacion = input('¿Está seguro de eliminar? (s/n): ').lower()
        if confirmacion == 's':
            try:
                mesa.delete_instance()
                print('¡Mesa eliminada con éxito!')
            except Exception as error:
                print(f'{mensaje_error}{error}')
        else:
            print('Operación cancelada.')