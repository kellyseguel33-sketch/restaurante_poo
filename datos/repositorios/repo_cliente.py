from datos.modelos.cliente import Cliente

def listado_clientes():
    cliente = Cliente.select()
    if cliente:
        return cliente 