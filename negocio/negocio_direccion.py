from prettytable import PrettyTable
from datos.repositorio.repositorio_direccion import listado_direcciones, guardar_direccion
from datos.modelos.direccion import Direccion, guardar_direccion
from auxiliares import mensaje_error


def procesar_listado_direcciones(tabla: PrettyTable):
    if tabla:
        tabla.field_names = ['Id', 'Calle', 'Número', 'Ciudad', 'Comuna', 'Detalles']
        lista_direcciones = listado_direcciones()
        if lista_direcciones:
            for direccion in lista_direcciones:
                tabla.add_row([
                    direccion.id_direccion,
                    direccion.calle,
                    direccion.numero,
                    direccion.ciudad,
                    direccion.comuna,
                    direccion.detalles
                ])
            return tabla


def crear_objeto_direccion(calle: str, numero: int, ciudad: str, comuna: str, detalles: str):
    try:
        direccion = Direccion(
            calle=calle,
            numero=numero,
            ciudad=ciudad,
            comuna=comuna,
            detalles=detalles
        )
        guardar_direccion(direccion)
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
            
        guardar_direccion(direccion)
    except Exception as error:
        print(f'{mensaje_error}{error}')