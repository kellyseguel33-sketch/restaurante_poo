from prettytable import PrettyTable
from auxiliares import mensaje_error
from negocio import procesar_listado_horarios
from datos.repositorio.repositorio_horarioatencion import obtener_horario_por_id
from negocio import crear_objeto_horario, modificar_objeto_horario


def mostrar_listado_horarios():
    try:
        tabla_horarios = PrettyTable()
        tabla_horarios = procesar_listado_horarios(tabla_horarios)
        print(tabla_horarios)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_horario():
    hora_apertura, hora_cierre, dias_semana = '', '', ''
    
    while hora_apertura == '':
        hora_apertura = input('Ingrese hora de apertura (ej. 12:00): ')
    while hora_cierre == '':
        hora_cierre = input('Ingrese hora de cierre (ej. 23:00): ')
    while dias_semana == '':
        dias_semana = input('Ingrese días de semana (ej. Lunes a Viernes): ')
        
    crear_objeto_horario(hora_apertura, hora_cierre, dias_semana)


def modificar_horario():
    mostrar_listado_horarios()
    id_horario = input('Ingrese ID del horario a modificar: ')
    horario = obtener_horario_por_id(id_horario)
    
    if horario:
        print('Horario Encontrado:')
        print(f'Apertura: {horario.hora_apertura} | Cierre: {horario.hora_cierre} | Días: {horario.dias_semana}')
        
        hora_apertura, hora_cierre, dias_semana = '', '', ''
        
        while hora_apertura == '':
            hora_apertura = input('Ingrese nueva hora de apertura [o ENTER para conservar]: ')
        while hora_cierre == '':
            hora_cierre = input('Ingrese nueva hora de cierre [o ENTER para conservar]: ')
        while dias_semana == '':
            dias_semana = input('Ingrese nuevos días de semana [o ENTER para conservar]: ')
            
        modificar_objeto_horario(hora_apertura, hora_cierre, dias_semana, horario)


def eliminar_horario():
    mostrar_listado_horarios()
    id_horario = input('Ingrese ID del horario a eliminar: ')
    horario = obtener_horario_por_id(id_horario)
    
    if horario:
        print('Se eliminará el horario:')
        print(f'Apertura: {horario.hora_apertura} | Cierre: {horario.hora_cierre}')
        confirmacion = input('¿Está seguro de eliminar? (s/n): ').lower()
        
        if confirmacion == 's':
            try:
                horario.delete_instance()
                print('¡Horario eliminado con éxito!')
            except Exception as error:
                print(f'{mensaje_error}{error}')
        else:
            print('Operación cancelada.')