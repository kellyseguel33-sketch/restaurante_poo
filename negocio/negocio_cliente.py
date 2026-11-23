from prettytable import PrettyTable
from datos.repositorio.repositorio_cliente import (
    listado_clientes_habilitado, 
    guardar_cliente, 
    obtener_cliente_rut
)
from datos.modelos.cliente import Cliente
from auxiliares import mensaje_error

def procesar_listado_clientes(tabla: PrettyTable):
    if tabla:
        tabla.field_names = ['Id', 'Nombre completo', 'RUT', 'Teléfono', 'Correo']
        lista_clientes = listado_clientes_habilitado()
        if lista_clientes:
            for cliente in lista_clientes:
                tabla.add_row([
                    cliente.id_cliente,
                    cliente.nombre,
                    cliente.rut,
                    cliente.telefono,
                    cliente.correo
                ])
            return tabla

def crear_objeto_cliente(str_rut, str_nombre, str_correo, str_telefono, str_contrasenia):
    try:
        cliente = Cliente(str_rut,
                        str_nombre,
                        str_correo, 
                        str_telefono,
                        password=str_contrasenia)
        guardar_cliente(cliente)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def modificar_objeto_cliente(str_nombre, rut_str, telefono_str, correo_str, cliente:Cliente):
    try:
        if str_nombre != '':
            cliente.nombre = str_nombre
        if rut_str != '':
            cliente.rut = rut_str
        if telefono_str != '':
            cliente.telefono = telefono_str
        if correo_str != '':
            cliente.correo = correo_str

        guardar_cliente(cliente)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def procesar_obtener_cliente_rut(rut_str):
    try:
        cliente = obtener_cliente_rut(rut_str)
        if Cliente:
            return cliente 
    except Exception as error:
        print(f'{mensaje_error}{error}')

def verificar_rut_existente(rut_str):
    try:
        cliente = obtener_cliente_rut(rut_str)
        return cliente is not None
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return False