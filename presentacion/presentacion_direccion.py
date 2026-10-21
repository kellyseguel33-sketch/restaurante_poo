from prettytable import PrettyTable
from auxiliares import mensaje_error
from negocio import procesar_listado_direcciones
from datos.repositorio.repositorio_direccion import obtener_direccion_por_id
from negocio import crear_objeto_direccion, modificar_objeto_direccion

def mostrar_listado_direcciones():
    try:
        tabla_direcciones = PrettyTable()
        tabla_direcciones = procesar_listado_direcciones(tabla_direcciones)
        print(tabla_direcciones)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def crear_direccion():
    calle, numero, ciudad, comuna, detalles = '', '', '', '', ''
    
    while calle == '':
        calle = input('Ingrese calle: ')
    while numero == '':
        numero = input('Ingrese número: ')
    while ciudad == '':
        ciudad = input('Ingrese ciudad: ')
    while comuna == '':
        comuna = input('Ingrese comuna: ')
        
    detalles = input('Ingrese detalles [o ENTER para omitir]: ')

    crear_objeto_direccion(calle, numero, ciudad, comuna, detalles)

def modificar_direccion():
    mostrar_listado_direcciones()
    id_dir = input('Ingrese el ID de la dirección a modificar: ')
    direccion = obtener_direccion_por_id(id_dir)
    
    if direccion:
        print('Dirección Encontrada:')
        print(f'Calle: {direccion.calle} #{direccion.numero}, {direccion.ciudad}')
        
        calle, numero, ciudad, comuna, detalles = '', '', '', '', ''
        
        while calle == '':
            calle = input('Ingrese nueva calle [o ENTER para conservar]: ')
        while numero == '':
            numero = input('Ingrese nuevo número [o ENTER para conservar]: ')
        while ciudad == '':
            ciudad = input('Ingrese nueva ciudad [o ENTER para conservar]: ')
        while comuna == '':
            comuna = input('Ingrese nueva comuna [o ENTER para conservar]: ')
        while detalles == '':
            detalles = input('Ingrese nuevos detalles [o ENTER para conservar]: ')
            
        modificar_objeto_direccion(calle, numero, ciudad, comuna, detalles, direccion)

def eliminar_direccion():
    mostrar_listado_direcciones()
    id_dir = input('Ingrese el ID de la dirección a eliminar: ')
    direccion = obtener_direccion_por_id(id_dir)
    
    if direccion:
        print('Se eliminará la siguiente dirección:')
        print(f'Calle: {direccion.calle} #{direccion.numero}, {direccion.comuna}')
        confirmacion = input('¿Está seguro de eliminar? (s/n): ').lower()
        
        if confirmacion == 's':
            try:
                direccion.delete_instance()
                print('¡Dirección eliminada con éxito!')
            except Exception as error:
                print(f'{mensaje_error}{error}')
        else:
            print('Operación cancelada.')