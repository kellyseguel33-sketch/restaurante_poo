from datos.modelos.direccion import Direccion
from auxiliares import mensaje_error
from datos.repositorio.repositorio_direccion import listado_direcciones

def listado_direcciones():
    try:
        direcciones = Direccion.select()
        if direcciones:
            return direcciones
    except Exception as error:
            print(f'{mensaje_error}{error}')

def obtener_direccion_por_id(id_direccion):
    try:
        direccion = Direccion.get(Direccion.id_direccion == id_direccion)
        if direccion:
            return direccion
    except Exception as error:
        print(f'{mensaje_error}{error}')

def guardar_direccion(calle, numero, ciudad, comuna, detalles):
    try:
        respuesta = Direccion.save(calle=calle, numero=numero, ciudad=ciudad, comuna=comuna, detalles=detalles)
        if respuesta:
            print(f'Dirección {calle} #{numero} guardada correctamente.')
    except Exception as error:
        print(f'{mensaje_error}{error}')
