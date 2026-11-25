from datos.repositorio.repositorio_direccion import guardar_direccion
from datos.repositorio.repositorio_restaurante import guardar_restaurante, obtener_restaurante_nombre
from datos.repositorio.repositorio_horarioatencion import guardar_horario
from prettytable import PrettyTable
from datos.modelos.restaurante import Restaurante
from datos.repositorio.repositorio_restaurante import (
    listado_restaurante,
    buscar_restaurantes,
    obtener_restaurante_nombre,
    obtener_restaurante_id,
    guardar_restaurante,
    actualizar_restaurante,
    eliminar_restaurante,
)
from datos.repositorio.repositorio_direccion import obtener_direccion_por_id
from auxiliares import mensaje_error

def inicializar_restaurante_por_defecto():
    try:
        restaurante_existente = obtener_restaurante_nombre("Restaurante")
        
        if restaurante_existente:
            print("El restaurante por defecto ya se encuentra registrado.")
            return restaurante_existente

        nueva_direccion = guardar_direccion(
            calle="Avenida Alemania",
            numero=825,
            ciudad="Temuco",
            comuna="Temuco",
            detalles="local principal"
        )

        nuevo_horario = guardar_horario(
            dias_semana = "lunes a viernes",
            hora_apertura = "09:00",
            hora_cierre = "23:00"
        )

        if nueva_direccion and nuevo_horario:
            restaurante_creado = guardar_restaurante(
                nombre="ricacomida",
                id_direccion=nueva_direccion.id_direccion,
                id_horario=nuevo_horario.id_horario
            )
            return restaurante_creado
            
    except Exception as error:
        print(f"Error al inicializar el restaurante: {error}")

def procesar_listado_restaurantes(tabla: PrettyTable):
    if tabla:
        tabla.field_names = ['Id', 'Nombre', 'ID Dirección', 'ID Horario']
        lista_restaurantes = listado_restaurante()
        if lista_restaurantes:
            for restaurante in lista_restaurantes:
                tabla.add_row([
                    restaurante.id_restaurante,
                    restaurante.nombre,
                    restaurante.id_direccion,
                    restaurante.id_horario,
                ])
    return tabla


def listado_restaurantes_nombre(tabla: PrettyTable, nombre_restaurante: str):
    id_restaurantes = []
    if tabla:
        tabla.field_names = ['Id', 'Nombre', 'ID Dirección', 'ID Horario']
        lista_restaurantes = buscar_restaurantes(nombre_restaurante)
        if lista_restaurantes:
            for restaurante in lista_restaurantes:
                tabla.add_row([
                    restaurante.id_restaurante,
                    restaurante.nombre,
                    restaurante.id_direccion,
                    restaurante.id_horario,
                ])
                id_restaurantes.append(restaurante.id_restaurante)
    return tabla, id_restaurantes


def crear_objeto_restaurante(nombre: str, id_direccion: int, id_horario: int):
    try:
        return guardar_restaurante(
            nombre=nombre.strip(),
            id_direccion=int(id_direccion),
            id_horario=int(id_horario),
        )
    except Exception as error:
        print(f'{mensaje_error}{error}')


def modificar_objeto_restaurante(
    nombre: str,
    id_direccion,
    id_horario,
    restaurante: Restaurante,
):
    try:
        if nombre != '' and restaurante.nombre != nombre:
            restaurante.nombre = nombre
        if id_direccion != '' and restaurante.id_direccion != int(id_direccion):
            restaurante.id_direccion = int(id_direccion)
        if id_horario != '' and restaurante.id_horario != int(id_horario):
            restaurante.id_horario = int(id_horario)
        return actualizar_restaurante(restaurante)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def eliminar_objeto_restaurante(restaurante: Restaurante):
    try:
        return eliminar_restaurante(restaurante)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def obtener_info_restaurante(nombre: str):
    try:
        restaurante = obtener_restaurante_nombre(nombre)
        if not restaurante:
            return None
        direccion = obtener_direccion_por_id(restaurante.id_direccion)
        return {
            'restaurante': restaurante,
            'direccion': direccion,
        }
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None