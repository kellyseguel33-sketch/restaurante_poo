import bcrypt
import re
from datos.modelos.cliente import Cliente

def pedir_rut():
    while  True:
        rut = input('RUT (ej: 12345678-9):').strip()
        if not rut:
            print('el RUT no puede estar vacio.')
            continue
        elif Cliente.select().where(Cliente.rut == rut).exists():
            print('este RUT ya se encuentra registrado, ingrese otro.')
        return rut

def pedir_nombre():
    while nombre == '':
        nombre = input('nombre completo: ').strip()
        if not nombre:
            print('el nombre no puede estar vacio.')

    while correo == '':
        correo = input('correo electronico:').strip()
        patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron_correo, correo):
            print('correo electronoco invalido, intente nuevamente.')
            correo = ''
        elif Cliente.select().where(Cliente.correo == correo).exists():
            print('este correo ya esta regitrao.')
            correo = ''

    while telefono == '':
        telefono = input('telefono (ej: +56912345678):').strip()
        if len(telefono) < 8:
            print('telefono muy corto o invalido.')
            telefono = ''

    while contrasenia == '':
        contrasenia = input('cree su contraseña de acceso:').strip()
        if len(contrasenia) < 4:
            print('la contraseña es muy corta. intente nuevamente.')
            contrasenia = ''

    hashed_password = bcrypt.hashpw(contrasenia.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    try:
        nuevo_cliente = Cliente.create(

            nombre = nombre.title(),
            rut = rut,
            correo = correo,
            telefono = telefono,
            password = hashed_password
        )
        print(f'\n cliente "{nombre.title()}" registrado exitosamente con id: {nuevo_cliente.id_cliente}!')
    except Exception as error:
        print(f'error al guardar el cliente: {error}')

def login_cliente():
    print(f'\n{nombre_app} - {version_app}')
    print(f'{"=" * (len(nombre_app) + len(version_app) + 3)}\n')

    correo = solicitar_correo('Correo: ')
    contrasenia = maskpass.askpass(prompt='Contraseña: ', mask='*')

    cliente, mensaje = neg.autenticar_cliente(correo, contrasenia)
    print(mensaje)
    return cliente