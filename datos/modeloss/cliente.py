from peewee import sql,  model AutoField, charfield

base_datos= conectar()
class basemodel(model):
    class meta:
        database = base_datos
class cliente(basemodel):
    id_cliente = AutoField()
    nombre = CharField()
    rut = CharField(max_length=20, unique=True)
    correo = CharField(null=True)
    telefono = CharField(max_length=20, null=True)
