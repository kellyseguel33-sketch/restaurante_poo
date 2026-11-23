from datos.repositorio.repositorio_direccion import guardar_direccion
from datos.repositorio.repositorio_restaurante import guardar_restaurante, obtener_restaurante_nombre
from datos.repositorio.repositorio_horarioatencion import guardar_horario

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
                id_horario_atencion=nuevo_horario.id_horario
            )
            return restaurante_creado
            
    except Exception as error:
        print(f"Error al inicializar el restaurante: {error}")