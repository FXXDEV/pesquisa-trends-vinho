from peewee import *

mysql_db = MySQLDatabase('trends_vinho')

print(mysql_db.connect())

class BaseModel(Model):

    class Meta:
        database = mysql_db

class Busca(BaseModel):
    termo = CharField()
    # etc, etc"
