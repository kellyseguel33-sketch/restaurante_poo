from negocio.negocio_restaurante import obtener_info_restaurante

def mostrar_menu_restaurante():
    print("=" * 40)
    print("SISTEMA DE RESERVAS - RESTAURANTE")
    print("=" * 40)
    
    datos = obtener_info_restaurante("Restaurante")
    
    if datos:
        restaurante = datos["restaurante"]
        direccion = datos["direccion"]
        
        print(f"Nombre: {restaurante.nombre}")
        print(f"Dirección: {direccion.calle} #{direccion.numero}")
        print(f"Comuna: {direccion.comuna}")
        print(f"Ciudad: {direccion.ciudad}")
        if direccion.detalles:
            print(f"Detalles: {direccion.detalles}")
    else:
        print("No se encontró información del restaurante.")
    
    print("=" * 40)
    print("[1] Hacer una reserva")
    print("[2] Ver horarios de atención")
    print("[3] Salir")
    print("=" * 40)