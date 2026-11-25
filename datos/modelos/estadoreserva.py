from peewee import Model, AutoField, CharField, TextField
from datos.conexion import conectar

database = conectar()

class BaseModel(Model):
    class Meta:
        database = database

class EstadoReserva(BaseModel):
    id_estado_reserva = AutoField()
    estado = CharField(max_length=50)
    descripcion = TextField(null=True)

    class Meta:
        table_name = 'estado_reserva'