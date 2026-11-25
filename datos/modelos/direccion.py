from peewee import Model, AutoField, CharField, IntegerField, TextField
from datos.conexion import conectar

database = conectar()

class BaseModel(Model):
    class Meta:
        database = database

class Direccion(BaseModel):
    id_direccion = AutoField()
    calle = CharField(max_length=255)
    numero = IntegerField()
    ciudad = CharField(max_length=150)
    comuna = CharField(max_length=150)
    detalles = TextField(null=True)

    class Meta:
        table_name = 'direccion'