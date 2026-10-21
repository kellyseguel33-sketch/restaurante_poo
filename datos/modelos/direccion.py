from peewee import SQL, Model, AutoField, CharField, IntegerField, TextField
from datos.conexion import conectar

database = conectar()

class basemodel(Model):
    class meta:
        database = database 

class Direccion(basemodel):
    id_direccion = AutoField()
    calle = CharField(max_length = 255)
    numero = IntegerField()
    ciudad = CharField(max_length = 150)
    comuna = CharField(max_length = 150)
    detalles = TextField(null = True)

