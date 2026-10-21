from datos.modelos.cliente import Cliente
from auxiliares import mensaje_error

def listado_clientes():
    try:
        clientes = Cliente.select()
        if clientes:
            return clientes
    except Exception as error:
            print(f'{mensaje_error}{error}')

def obtener_cliente_nombre(nombre):
    try:
        cliente = Cliente.get(Cliente.nombre == nombre)
        if cliente:
            return cliente
    except Exception as error:
        print(f'{mensaje_error}{error}')

def guardar_cliente(nombre, rut, correo, telefono):
    try:
        respuesta = Cliente.save(nombre=nombre, rut=rut, correo=correo, telefono=telefono)
        if respuesta == 1:
            print(f'Cliente {nombre} guardado correctamente.')
    except Exception as error:
        print(f'{mensaje_error}{error}')

