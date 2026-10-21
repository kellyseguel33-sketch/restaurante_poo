from prettytable import PrettyTable
from datos.repositorio.repositorio_mesa import listado_mesa, guardar_mesa
from datos.modelos.mesa import Mesa, guardar_mesa
from auxiliares import mensaje_error


def procesar_listado_mesas(tabla: PrettyTable):
    if tabla:
        tabla.field_names = ['Id', 'Restaurante', 'Número', 'Capacidad', 'Ubicación']
        lista_mesas = listado_mesa()
        if lista_mesas:
            for mesa in lista_mesas:
                tabla.add_row([
                    mesa.id_mesa,
                    mesa.id_restaurante,
                    mesa.numero,
                    mesa.capacidad,
                    mesa.ubicacion
                ])
            return tabla


def crear_objeto_mesa(id_restaurante: int, numero: int, capacidad: int, ubicacion: str):
    try:
        mesa = Mesa(
            id_restaurante=id_restaurante,
            numero=numero,
            capacidad=capacidad,
            ubicacion=ubicacion
        )
        guardar_mesa(mesa)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def modificar_objeto_mesa(id_restaurante: int, numero: int, capacidad: int, ubicacion: str, mesa: Mesa):
    try:
        if mesa.id_restaurante != id_restaurante and id_restaurante != '':
            mesa.id_restaurante = id_restaurante
        if mesa.numero != numero and numero != '':
            mesa.numero = numero
        if mesa.capacidad != capacidad and capacidad != '':
            mesa.capacidad = capacidad
        if mesa.ubicacion != ubicacion and ubicacion != '':
            mesa.ubicacion = ubicacion
            
        guardar_mesa(mesa)
    except Exception as error:
        print(f'{mensaje_error}{error}')