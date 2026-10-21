from prettytable import PrettyTable
from datos.repositorio.repositorio_horarioatencion import listado_horariosatencion, guardar_horario
from datos.modelos.horarioatencion import HorarioAtencion , guardar_horario
from auxiliares import mensaje_error


def procesar_listado_horarios(tabla: PrettyTable):
    if tabla:
        tabla.field_names = ['Id', 'Día', 'Hora apertura', 'Hora cierre', 'Habilitado']
        lista_horarios = listado_horariosatencion()
        if lista_horarios:
            for horario in lista_horarios:
                tabla.add_row([
                    horario.id_horario,
                    horario.dia,
                    horario.hora_inicio,
                    horario.hora_fin,
                    horario.habilitado
                ])
            return tabla


def crear_objeto_horario(dia: str, hora_inicio: str, hora_fin: str):
    try:
        horario = HorarioAtencion(dia=dia, hora_inicio=hora_inicio, hora_fin=hora_fin)
        guardar_horario(horario)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def modificar_objeto_horario(dia: str, hora_inicio: str, hora_fin: str, habilitado: bool, horario: HorarioAtencion):
    try:
        if horario.dia != dia and dia != '':
            horario.dia = dia
        if horario.hora_inicio != hora_inicio and hora_inicio != '':
            horario.hora_inicio = hora_inicio
        if horario.hora_fin != hora_fin and hora_fin != '':
            horario.hora_fin = hora_fin
        if horario.habilitado != habilitado:
            horario.habilitado = habilitado

        guardar_horario(horario)
    except Exception as error:
        print(f'{mensaje_error}{error}')