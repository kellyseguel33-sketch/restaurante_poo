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