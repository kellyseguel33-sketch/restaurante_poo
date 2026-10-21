from datos.modelos.horarioatencion import HorarioAtencion
from auxiliares import mensaje_error

def listado_horariosatencion():
    try:
        horarios = HorarioAtencion.select()
        if horarios:
            return horarios
    except Exception as error:
            print(f'{mensaje_error}{error}')

def obtener_horario_por_id(id_horario):
    try:
        horario = HorarioAtencion.get(HorarioAtencion.id_horario == id_horario)
        if horario:
            return horario
    except Exception as error:
        print(f'{mensaje_error}{error}')

def guardar_horario(dias_semana, hora_apertura, hora_cierre):
    try:
        respuesta = HorarioAtencion.save(dias_semana=dias_semana, hora_apertura=hora_apertura, hora_cierre=hora_cierre)
        if respuesta:
            print(f'Horario de atención ({dias_semana}) guardado correctamente.')
    except Exception as error:
        print(f'{mensaje_error}{error}')