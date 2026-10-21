from peewee import Model, AutoField, CharField
from datos.conexion import conectar

database = conectar()

class BaseModel(Model):
    class Meta:
        database = database

class HorarioAtencion(BaseModel):
    id_horario = AutoField()
    dias_semana = CharField(max_length=20)
    hora_apertura = CharField(max_length=10)
    hora_cierre = CharField(max_length=10)

