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

def guardar_restaurante(nombre, id_direccion, id_horarios_atencion):
    try:
        respuesta = Restaurante.save(nombre=nombre, id_direccion=id_direccion, id_horarios_atencion=id_horarios_atencion)
        if respuesta:
            print(f'Restaurante {nombre} guardado correctamente.')
    except Exception as error:
        print(f'{mensaje_error}{error}')
