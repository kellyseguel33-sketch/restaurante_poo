from prettytable import PrettyTable
from datos.repositorio.repositorio_mesa import listado_mesa, guardar_mesa
from datos.modelos.mesa import Mesa
from auxiliares import mensaje_error

id_restaurante_por_defecto = 1

def inicializar_mesa_ricacomida():
    try:
        for i in range(1, 11):
            capacidad = 4 if i <= 6 else 6
            guardar_mesa(
                id_restautante = id_restaurante_por_defecto,
                numero = i,
                capacidad = capacidad,
                ubicacion = "salon principal"
            )
        print("se han creado las 10 mesas para 'ricacomida' correctamente.")
    except Exception as error:
        print(f"error al inicializar las mesas:{error}")

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
            
        mesa.save()
        print('¡Mesa actualizada correctamente!')
    except Exception as error:
        print(f'{mensaje_error}{error}')