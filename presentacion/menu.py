from auxiliares import (
    nombre_app,
    version_app,
    mensaje_error_opcion,
    menu_principal, diccionario_menu_principal,
    menu_configuracion, diccionario_menu_configuracion,
    menu_configurar_parametros, diccionario_menu_configurar_parametros,
    menu_clientes, diccionario_menu_clientes
)
from presentacion.presentacion_cliente import mostrar_listado_clientes, crear_cliente, modificar_cliente, eliminar_cliente

TEXTO_OPCION = 'Seleccione su opción: '

def mostrar_menu(titulo, opciones):
    print(titulo)
    print(f'{"=" * len(titulo)}\n')

    for clave, valor in opciones.items():
        print(f'[{clave}] - {valor}')

def cargar_menu_clientes():
    while True:
        mostrar_menu(menu_clientes, diccionario_menu_clientes)
        opcion = input(TEXTO_OPCION)
        print()

        match opcion:
            case '1':
                mostrar_listado_clientes()
            case '2':
                crear_cliente()
            case '3':
                modificar_cliente()
            case '4':
                eliminar_cliente()
            case '0':
                print('Volviendo al Menú Principal...\n')
                break
            case _:
                print(mensaje_error_opcion)

def cargar_menu_configurar_parametros():
    while True:
        mostrar_menu(
            menu_configurar_parametros,
            diccionario_menu_configurar_parametros
        )
        opcion = input(TEXTO_OPCION)
        print()

        match opcion:
            case '1':
                print('Gestión de Estados de Reserva (Próximamente)')
            case '0':
                print('Volviendo al Menú Configuración Sistema...\n')
                break
            case _:
                print(mensaje_error_opcion)

def cargar_menu_configuracion():
    while True:
        mostrar_menu(menu_configuracion, diccionario_menu_configuracion)
        opcion = input(TEXTO_OPCION)
        print()

        match opcion:
            case '1':
                print('Cargando datos iniciales...')
            case '2':
                print(f'Aplicación: {nombre_app} - Versión: {version_app}')
            case '3':
                cargar_menu_configurar_parametros()
            case '4':
                print('Ayuda del Sistema de Reservas')
            case '0':
                print('Volviendo al Menú Principal...\n')
                break
            case _:
                print(mensaje_error_opcion)

def cargar_menu():
    print(f'\n{nombre_app} - {version_app}')
    print(f'{"=" * (len(nombre_app) + len(version_app) + 3)}\n')

    while True:
        mostrar_menu(menu_principal, diccionario_menu_principal)
        opcion = input(TEXTO_OPCION)
        print()

        match opcion:
            case '1':
                cargar_menu_clientes()
            case '2':
                print('Gestión de Mesas (Próximamente)')
            case '3':
                print('Gestión de Reservas (Próximamente)')
            case '4':
                print('Reportes (Próximamente)')
            case '5':
                cargar_menu_configuracion()
            case '0':
                print('Saliendo del sistema. ¡Hasta luego!')
                break
            case _:
                print(mensaje_error_opcion)