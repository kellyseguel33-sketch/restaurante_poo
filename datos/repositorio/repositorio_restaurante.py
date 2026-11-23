from datos.modelos.restaurante import Restaurante
from auxiliares import mensaje_error

def listado_restaurante():
    try:
        restaurantes = Restaurante.select()
        if restaurantes:
            return restaurantes
    except Exception as error:
        print(f'{mensaje_error}{error}')

def obtener_restaurante_nombre(nombre):
    try:
        restaurante = Restaurante.get(Restaurante.nombre == nombre)
        if restaurante:
            return restaurante
    except Exception as error:
        print(f'{mensaje_error}{error}')

def guardar_restaurante(nombre, id_direccion, id_horario_atencion):
    try:
        restaurante = Restaurante.create(
            nombre=nombre, 
            id_direccion=id_direccion, 
            id_horario_atencion=id_horario_atencion
        )
        if restaurante:
            print(f'Restaurante {nombre} guardado correctamente.')
            return restaurante
    except Exception as error:
        print(f'{mensaje_error}{error}')

def buscar_restaurantes(nombre_restaurante: str):
    try:
        restaurantes = Restaurante.select().where(Restaurante.nombre.contains(nombre_restaurante))
        if restaurantes:
            return restaurantes
    except Exception as error:
        print(f'{mensaje_error}{error}')


def obtener_restaurante_id(id_restaurante: int):
    try:
        restaurante = Restaurante.get_or_none(Restaurante.id_restaurante == id_restaurante)
        if restaurante:
            return restaurante
    except Exception as error:
        print(f'{mensaje_error}{error}')


def actualizar_restaurante(restaurante: Restaurante):
    try:
        respuesta = restaurante.save()
        if respuesta:
            print(f'Restaurante "{restaurante.nombre}" actualizado correctamente.')
            return restaurante
    except Exception as error:
        print(f'{mensaje_error}{error}')


def eliminar_restaurante(restaurante: Restaurante):
    try:
        eliminados = restaurante.delete_instance()
        if eliminados:
            print(f'Restaurante "{restaurante.nombre}" eliminado correctamente.')
            return True
    except Exception as error:
        print(f'{mensaje_error}{error}')
    return False