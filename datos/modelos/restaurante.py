from peewee import Model, AutoField, CharField, IntegerField
from datos.conexion import conectar

database = conectar()

class BaseModel(Model):
    class Meta:
        database = database

class Restaurante(BaseModel):
    id_restaurante = AutoField()
    nombre = CharField(max_length=255)
    id_direccion = IntegerField(null=True)
    id_horario = IntegerField(null=True)

    class Meta:
        table_name = 'restaurante'