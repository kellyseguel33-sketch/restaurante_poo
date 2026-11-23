from peewee import SQL,  Model, AutoField, CharField, BooleanField
from datos.conexion import conectar
from auxiliares.datos_app import defecto

base_datos= conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Cliente(BaseModel):
    id_cliente = AutoField()
    nombre = CharField(max_length=100)
    rut = CharField(max_length=20, unique=True)
    correo = CharField(null=True)
    telefono = CharField(max_length=20, null=True)
    password = CharField(max_length=60, null=True)
    habilitado = BooleanField(default=True)
class Meta:
        table_name = 'cliente'