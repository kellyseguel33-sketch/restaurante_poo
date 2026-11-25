from datos.modelos.cliente import Cliente
from auxiliares import mensaje_error

def listado_clientes_habilitado():
    try:
        clientes = Cliente.select().where(Cliente.habilitado == True)
        if clientes:
            return clientes
    except Exception as error:
        print(f'{mensaje_error}{error}')

def listado_clientes_vetado():
    try:
        clientes = Cliente.select().where(Cliente.habilitado == False)
        if clientes:
            return clientes
    except Exception as error:
        print(f'{mensaje_error}{error}')

def listado_clientes():
    try:
        clientes = Cliente.select()
        if clientes:
            return clientes
    except Exception as error:
        print(f'{mensaje_error}{error}')

def obtener_cliente_rut(rut_cliente):
    try:
        return Cliente.get_or_none(Cliente.rut == rut_cliente)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def guardar_cliente(cliente: Cliente):
    try:
        respuesta = cliente.save()
        if respuesta:
            print(f'Cliente guardado con éxito, ID: {cliente.id_cliente}')
            return cliente
    except Exception as error:
        print(f'{mensaje_error}{error}')

def obtener_cliente_nombre(nombre_cliente):
    try:
        return Cliente.get_or_none(Cliente.nombre == nombre_cliente)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def obtener_correo_cliente(correo_cliente):
    try:
        return Cliente.get_or_none(Cliente.correo == correo_cliente)
    except Exception as error:
        print(f'{mensaje_error}{error}')