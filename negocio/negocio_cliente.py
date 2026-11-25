from prettytable import PrettyTable
from datos.repositorio.repositorio_cliente import (
    listado_clientes_habilitado,
    guardar_cliente,
    obtener_cliente_rut,
    obtener_correo_cliente
)
from datos.modelos.cliente import Cliente
from auxiliares import mensaje_error
import bcrypt

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
        hashed_password = bcrypt.hashpw(
            str_contrasenia.encode('utf-8'), bcrypt.gensalt()
        ).decode('utf-8')
        cliente = Cliente(
            rut=str_rut,
            nombre=str_nombre.title(),
            correo=str_correo.lower() if str_correo else None,
            telefono=str_telefono if str_telefono else None,
            password=hashed_password
        )
        return guardar_cliente(cliente)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def modificar_objeto_cliente(str_nombre, rut_str, telefono_str, correo_str, cliente: Cliente):
    try:
        if str_nombre != '':
            cliente.nombre = str_nombre.title()
        if rut_str != '':
            cliente.rut = rut_str
        if telefono_str != '':
            cliente.telefono = telefono_str
        if correo_str != '':
            cliente.correo = correo_str.lower()
        return guardar_cliente(cliente)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def procesar_obtener_cliente_rut(rut_str):
    try:
        cliente = obtener_cliente_rut(rut_str)
        if cliente:
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

def autenticar_cliente(correo: str, contrasenia: str):
    try:
        cliente = obtener_correo_cliente(correo.strip().lower())
        if not cliente:
            return None, 'Correo o contraseña incorrectos.'
        if not cliente.habilitado:
            return None, 'El cliente se encuentra deshabilitado.'
        if not cliente.password:
            return None, 'El cliente no tiene contraseña registrada.'

        hash_password = (
            cliente.password.encode('utf-8')
            if isinstance(cliente.password, str)
            else bytes(cliente.password)
        )

        if bcrypt.checkpw(contrasenia.encode('utf-8'), hash_password):
            return cliente, f'Bienvenido/a, {cliente.nombre}.'

        return None, 'Correo o contraseña incorrectos.'
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None, 'Error al intentar iniciar sesión.'