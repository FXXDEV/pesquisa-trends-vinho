import peewee

mysql_db = MySQLDatabase('trends_vinho')

class BaseModel(Model):

    class Meta:
        database = mysql_db

class Busca(BaseModel):
    termo = CharField()
    # etc, etc"
