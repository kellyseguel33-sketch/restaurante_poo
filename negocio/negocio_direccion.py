from prettytable import PrettyTable
from datos.repositorio.repositorio_direccion import (
    listado_direcciones,
    guardar_direccion,
    actualizar_direccion
)
from datos.modelos.direccion import Direccion
from auxiliares import mensaje_error

def procesar_listado_direcciones(tabla: PrettyTable):
    if tabla:
        tabla.field_names = ['Id', 'Calle', 'Número', 'Ciudad', 'Comuna', 'Detalles']
        lista = listado_direcciones()
        if lista:
            for d in lista:
                tabla.add_row([d.id_direccion, d.calle, d.numero, d.ciudad, d.comuna, d.detalles])
        return tabla

def crear_objeto_direccion(calle: str, numero: int, ciudad: str, comuna: str, detalles: str = None):
    try:
        return guardar_direccion(calle, numero, ciudad, comuna, detalles)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def modificar_objeto_direccion(calle: str, numero, ciudad: str, comuna: str, detalles: str, direccion: Direccion):
    try:
        if calle != '':
            direccion.calle = calle
        if numero != '':
            direccion.numero = int(numero)
        if ciudad != '':
            direccion.ciudad = ciudad
        if comuna != '':
            direccion.comuna = comuna
        if detalles != '':
            direccion.detalles = detalles
        return actualizar_direccion(direccion)
    except Exception as error:
        print(f'{mensaje_error}{error}')