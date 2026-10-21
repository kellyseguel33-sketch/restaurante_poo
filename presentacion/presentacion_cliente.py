from prettytable import PrettyTable
from auxiliares import mensaje_error
from negocio import procesar_listado_clientes
from datos import obtener_cliente_nombre
from negocio import crear_objeto_cliente, modificar_objeto_cliente


def mostrar_listado_clientes():
    try:
        tabla_clientes = PrettyTable()
        tabla_clientes = procesar_listado_clientes(tabla_clientes)
        print(tabla_clientes)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_cliente():
    nombre, rut, telefono, correo = '', '', '', ''
    
    while nombre == '':
        nombre = input('Ingrese nombre: ')
    while rut == '':
        rut = input('Ingrese RUT: ')
    while telefono == '':
        telefono = input('Ingrese teléfono: ')
    while correo == '':
        correo = input('Ingrese correo: ')
        
    crear_objeto_cliente(nombre, rut, telefono, correo)


def modificar_cliente():
    mostrar_listado_clientes()
    nombre_buscar = input('Ingrese el nombre del cliente a modificar: ')
    cliente = obtener_cliente_nombre(nombre_buscar)
    
    if cliente:
        print('Cliente Encontrado:')
        print(f'Nombre: {cliente.nombre} | RUT: {cliente.rut}')
        
        nombre, rut, telefono, correo = '', '', '', ''
        
        while nombre == '':
            nombre = input('Ingrese nuevo nombre [o ENTER para conservar]: ')
        while rut == '':
            rut = input('Ingrese nuevo RUT [o ENTER para conservar]: ')
        while telefono == '':
            telefono = input('Ingrese nuevo teléfono [o ENTER para conservar]: ')
        while correo == '':
            correo = input('Ingrese nuevo correo [o ENTER para conservar]: ')
            
        modificar_objeto_cliente(nombre, rut, telefono, correo, cliente)


def eliminar_cliente():
    mostrar_listado_clientes()
    nombre_buscar = input('Ingrese el nombre del cliente a eliminar: ')
    cliente = obtener_cliente_nombre(nombre_buscar)
    
    if cliente:
        print(f'Se eliminará el cliente: {cliente.nombre}')
        confirmacion = input('¿Está seguro de eliminar? (s/n): ').lower()
        
        if confirmacion == 's':
            try:
                cliente.delete_instance()
                print('¡Cliente eliminado con éxito!')
            except Exception as error:
                print(f'{mensaje_error}{error}')
        else:
            print('Operación cancelada.')

