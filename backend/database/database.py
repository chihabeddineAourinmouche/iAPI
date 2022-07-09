# import sqlite3
from sqlite3 import connect, DatabaseError
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

class Database:

	def __init__(self, db_filename=os.path.join(current_dir, "database.db")):
		self.db_filename = db_filename
		self.connection = connect(self.db_filename)
	
	# R FROM CRUD
	def r_list(self, query_string, query_parameters=[]):
		cursor = self.connection.cursor()
		try:
			cursor.execute(query_string, query_parameters)
		except DatabaseError as e:
			raise e
		column_names = list(map(lambda c: c[0], cursor.description))
		results = cursor.fetchall()
		self.connection.commit()
		cursor.close()
		return [dict(zip(column_names, results[i])) for i in range(len(results))]
	
	# R FROM CRUD
	def r_item(self, query_string, query_parameters=[]):
		cursor = self.connection.cursor()
		try:
			cursor.execute(query_string, query_parameters)
		except DatabaseError as e:
			raise e
		column_names = list(map(lambda c: c[0], cursor.description))
		results = cursor.fetchone()
		self.connection.commit()
		cursor.close()
		return dict(zip(column_names, results))
	
	# CUD FROM CRUD
	def cud(self, query_string, query_parameters=[]):
		cursor = self.connection.cursor()
		try:
			cursor.execute(query_string, query_parameters)
		except DatabaseError as e:
			raise e
		self.connection.commit()
		cursor.close()