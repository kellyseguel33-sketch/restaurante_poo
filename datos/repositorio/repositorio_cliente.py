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
        cliente = Cliente.get(Cliente.rut == rut_cliente)
        if cliente:
            return cliente
    except Exception as error:
        print(f'{mensaje_error}{error}')

def guardar_cliente(cliente:Cliente):
    try:
        respuesta = Cliente.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito, ID: {cliente.id_cliente}')
    except Exception as error:
        print(f'{mensaje_error}{error}')

def obtener_cliente_nombre(nombre_cliente):
    try:
        cliente = Cliente.get(Cliente.nombre == nombre_cliente)
        if cliente:
            return Cliente
    except Exception as error:
        print(f'{mensaje_error}{error}')

def obtener_correo_cliente(nombre_cliente):
    try:
        cliente = Cliente.get(Cliente.nombre == nombre_cliente)
        if cliente:
            return cliente.correo
    except Exception as error:
        print(f'{mensaje_error}{error}')