import peewee
from peewee import *
import mysql.connector
from mysql.connector import errorcode

class Banco(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(Banco, self).__init__()
		self.arg = arg
		
# Verificacao de conexao com o banco atraves do Mysql connector
def conexao(self):
	try:
	  cnx = mysql.connector.connect(user='root',
	                                database='trends_vinho',
	                                port=3306,
	                                host='127.0.0.1'
	                                )
	except mysql.connector.Error as err:
	  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
	    print("Algo errado com seu usuario/senha")
	  elif err.errno == errorcode.ER_BAD_DB_ERROR:
	    print("Banco de Dados nao existente")
	  else:
	    print(err)
	else:
	  cnx.close()



	mysql_db = MySQLDatabase(cnx) #conexao peweee


