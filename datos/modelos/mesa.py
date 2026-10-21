from peewee import Model, AutoField, IntegerField, CharField
from datos.conexion import conectar

database = conectar()

class BaseModel(Model):
    class Meta:
        database = database

class Mesa(BaseModel):
    id_mesa = AutoField()
    id_restaurante = IntegerField() 
    numero = IntegerField()
    capacidad = IntegerField()
    ubicacion = CharField(max_length=100, null=True)

