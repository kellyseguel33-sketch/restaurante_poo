from datos.modelos.cliente import Cliente

def listado_clientes():
    cliente = cliente.select()
    if cliente:
        return cliente