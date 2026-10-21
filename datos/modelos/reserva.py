from peewee import Model, AutoField, DateField, CharField, IntegerField
from datos.conexion import conectar

database = conectar()

class BaseModel(Model):
    class Meta:
        database = database

class Reserva(BaseModel):
    id_reserva = AutoField()
    fecha = DateField()
    hora = CharField(max_length=10)
    cantidad_personas = IntegerField()
    id_restaurante = IntegerField()
    id_cliente = IntegerField()
    id_mesa = IntegerField(null=True)
    id_estado_reserva = IntegerField()