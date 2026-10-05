from peewee import SQL,  Model, AutoField, CharField
from datos.conexion import conectar

base_datos= conectar()

class BaseModel(Model):
    class meta:
        database = base_datos

class Cliente(BaseModel):
    id_cliente = AutoField()
    nombre = CharField(max_length=100)
    rut = CharField(max_length=20, unique=True)
    correo = CharField(null=True)
    telefono = CharField(max_length=20, null=True)
