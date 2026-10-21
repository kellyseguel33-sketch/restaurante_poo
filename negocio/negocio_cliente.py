from prettytable import PrettyTable
from datos.repositorio.repositorio_cliente import listado_clientes
from datos import Cliente, guardar_cliente
from auxiliares import mensaje_error


def procesar_listado_clientes(tabla: PrettyTable):
    if tabla:
        tabla.field_names = ['Id', 'Nombre', 'RUT', 'Teléfono', 'Correo']
        lista_clientes = listado_clientes()
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

def crear_objeto_cliente(nombre: str, rut: str, telefono: str, correo: str):
    try:
        cliente = Cliente(nombre, rut, telefono, correo)
        guardar_cliente(cliente)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def modificar_objeto_cliente(nombre: str, rut: str, telefono: str, correo: str, cliente: Cliente):
    try:
        if cliente.nombre != nombre and nombre != '':
            cliente.nombre = nombre
        if cliente.rut != rut and rut != '':
            cliente.rut = rut
        if cliente.telefono != telefono and telefono != '':
            cliente.telefono = telefono
        if cliente.correo != correo and correo != '':
            cliente.correo = correo

        guardar_cliente(cliente)
    except Exception as error:
        print(f'{mensaje_error}{error}')