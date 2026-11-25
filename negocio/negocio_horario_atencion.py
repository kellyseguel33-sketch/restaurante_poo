from prettytable import PrettyTable
from datos.repositorio.repositorio_horarioatencion import listado_horariosatencion, guardar_horario
from datos.modelos.horarioatencion import HorarioAtencion
from auxiliares import mensaje_error

def procesar_listado_horarios(tabla: PrettyTable):
    if tabla:
        tabla.field_names = ['Id', 'Días', 'Hora apertura', 'Hora cierre']
        lista_horarios = listado_horariosatencion()
        if lista_horarios:
            for horario in lista_horarios:
                tabla.add_row([
                    horario.id_horario,
                    horario.dias_semana,
                    horario.hora_apertura,
                    horario.hora_cierre
                ])
        return tabla

def crear_objeto_horario(dias_semana: str, hora_apertura: str, hora_cierre: str):
    try:
        return guardar_horario(dias_semana, hora_apertura, hora_cierre)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def modificar_objeto_horario(dias_semana: str, hora_apertura: str, hora_cierre: str, horario: HorarioAtencion):
    try:
        if dias_semana != '' and horario.dias_semana != dias_semana:
            horario.dias_semana = dias_semana
        if hora_apertura != '' and horario.hora_apertura != hora_apertura:
            horario.hora_apertura = hora_apertura
        if hora_cierre != '' and horario.hora_cierre != hora_cierre:
            horario.hora_cierre = hora_cierre
        horario.save()
        print('¡Horario actualizado correctamente!')
        return horario
    except Exception as error:
        print(f'{mensaje_error}{error}')