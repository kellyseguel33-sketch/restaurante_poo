from datos.modelos.mesa import Mesa
from auxiliares import mensaje_error

def listado_mesa():
    try:
        mesas = Mesa.select()
        if mesas:
            return mesas
    except Exception as error:
            print(f'{mensaje_error}{error}')

def obtener_mesa_por_id(id_mesa):
    try:
        mesa = Mesa.get(Mesa.id_mesa == id_mesa)
        if mesa:
            return mesa
    except Exception as error:
        print(f'{mensaje_error}{error}')


def guardar_mesa(id_restaurante, numero , capacidad , ubicacion ):
    try:
        mesa = Mesa(
            id_restaurante=id_restaurante,
            numero=numero,
            capacidad=capacidad,
            ubicacion=ubicacion
        )
        mesa.save()
        if mesa:
            print('¡Mesa guardada correctamente!')
    except Exception as error:
        print(f'{mensaje_error}{error}')
