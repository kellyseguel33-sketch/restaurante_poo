from prettytable import PrettyTable
from datos.repositorio.repositorio_restaurante import listado_restaurante, guardar_restaurante
from datos.modelos.restaurante import Restaurante
from auxiliares import mensaje_error


def procesar_listado_restaurantes(tabla: PrettyTable):
    if tabla:
        tabla.field_names = ['Id', 'Nombre', 'Id Dirección', 'Id Horario']
        lista_restaurantes = listado_restaurante()
        if lista_restaurantes:
            for res in lista_restaurantes:
                tabla.add_row([
                    res.id_restaurante,
                    res.nombre,
                    res.id_direccion,
                    res.id_horarios_atencion
                ])
            return tabla


def crear_objeto_restaurante(nombre: str, id_direccion: int, id_horarios_atencion: int):
    try:
        restaurante = Restaurante(
            nombre=nombre,
            id_direccion=id_direccion,
            id_horarios_atencion=id_horarios_atencion
        )
        guardar_restaurante(restaurante)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def modificar_objeto_restaurante(nombre: str, id_direccion: int, id_horarios_atencion: int, restaurante: Restaurante):
    try:
        if restaurante.nombre != nombre and nombre != '':
            restaurante.nombre = nombre
        if restaurante.id_direccion != id_direccion and id_direccion != '':
            restaurante.id_direccion = id_direccion
        if restaurante.id_horarios_atencion != id_horarios_atencion and id_horarios_atencion != '':
            restaurante.id_horarios_atencion = id_horarios_atencion
            
        guardar_restaurante(restaurante)
    except Exception as error:
        print(f'{mensaje_error}{error}')