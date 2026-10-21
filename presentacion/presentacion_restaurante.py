from prettytable import PrettyTable
from auxiliares import mensaje_error
from negocio import procesar_listado_restaurantes
from datos.repositorio.repositorio_restaurante import obtener_restaurante_por_id
from negocio import crear_objeto_restaurante, modificar_objeto_restaurante

def mostrar_listado_restaurantes():
    try:
        tabla_restaurantes = PrettyTable()
        tabla_restaurantes = procesar_listado_restaurantes(tabla_restaurantes)
        print(tabla_restaurantes)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def crear_restaurante():
    nombre, id_direccion, id_horarios_atencion = '', '', ''
    
    while nombre == '':
        nombre = input('Ingrese nombre del restaurante: ')
    while id_direccion == '':
        id_direccion = input('Ingrese ID de la dirección: ')
    while id_horarios_atencion == '':
        id_horarios_atencion = input('Ingrese ID del horario de atención: ')
        
    crear_objeto_restaurante(
        nombre, 
        int(id_direccion), 
        int(id_horarios_atencion)
    )

def modificar_restaurante():
    mostrar_listado_restaurantes()
    id_r = input('Ingrese ID del restaurante a modificar: ')
    restaurante = obtener_restaurante_por_id(id_r)
    
    if restaurante:
        print('Restaurante Encontrado:')
        print(f'Restaurante: {restaurante.nombre} | ID Dirección: {restaurante.id_direccion}')
        
        nombre, id_direccion, id_horarios_atencion = '', '', ''
        
        while nombre == '':
            nombre = input('Ingrese nuevo nombre [o ENTER para conservar]: ')
        while id_direccion == '':
            id_direccion = input('Ingrese nuevo ID de dirección [o ENTER para conservar]: ')
        while id_horarios_atencion == '':
            id_horarios_atencion = input('Ingrese nuevo ID de horario de atención [o ENTER para conservar]: ')
            
        modificar_objeto_restaurante(
            nombre if nombre != '' else restaurante.nombre,
            int(id_direccion) if id_direccion != '' else restaurante.id_direccion,
            int(id_horarios_atencion) if id_horarios_atencion != '' else restaurante.id_horarios_atencion,
            restaurante
        )

def eliminar_restaurante():
    mostrar_listado_restaurantes()
    id_r = input('Ingrese ID del restaurante a eliminar: ')
    restaurante = obtener_restaurante_por_id(id_r)
    
    if restaurante:
        print('Se eliminará el restaurante:')
        print(f'Restaurante: {restaurante.nombre}')
        confirmacion = input('¿Está seguro de eliminar? (s/n): ').lower()
        
        if confirmacion == 's':
            try:
                restaurante.delete_instance()
                print('¡Restaurante eliminado con éxito!')
            except Exception as error:
                print(f'{mensaje_error}{error}')
        else:
            print('Operación cancelada.')