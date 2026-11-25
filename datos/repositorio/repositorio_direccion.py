from datos.modelos.direccion import Direccion
from auxiliares import mensaje_error

def listado_direcciones():
    try:
        direcciones = Direccion.select()
        if direcciones:
            return direcciones
    except Exception as error:
        print(f'{mensaje_error}{error}')

def obtener_direccion_por_id(id_direccion):
    try:
        return Direccion.get_or_none(Direccion.id_direccion == id_direccion)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def guardar_direccion(calle, numero, ciudad, comuna, detalles):
    try:
        direccion = Direccion.create(
            calle=calle, numero=numero, ciudad=ciudad, comuna=comuna, detalles=detalles
        )
        if direccion:
            print(f'Dirección {calle} #{numero} guardada correctamente.')
            return direccion
    except Exception as error:
        print(f'{mensaje_error}{error}')

def actualizar_direccion(direccion: Direccion):
    try:
        if direccion.save():
            print('Dirección actualizada correctamente.')
            return direccion
    except Exception as error:
        print(f'{mensaje_error}{error}')

