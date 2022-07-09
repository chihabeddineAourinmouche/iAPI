import eel
import os
import base64

from backend.controller.controller import Controller

class ID_Card_Controller(Controller):
	
	def insert_id_card(self, country_name, number, issue_date, expiry_date, first_name, last_name, birthdate, address, file_path):
		"""
			EXPECTS DATES IN THE FORM dd-mm-yyyy, i.e. "1-2-1990", "20-11-2022"
		"""
		issue_date = "-".join(list(map(lambda e: e[1] if e[0] == "0" else e, issue_date.split("-"))))
		expiry_date = "-".join(list(map(lambda e: e[1] if e[0] == "0" else e, expiry_date.split("-"))))
		query_string = "INSERT INTO ID_CARD(country_name, number, issue_date, expiry_date, first_name, last_name, birthdate, address, file_path) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
		self.database.cud(query_string, [country_name, number, issue_date, expiry_date, first_name, last_name, birthdate, address, file_path])
	
	def get_id_card_by_country_name(self, country_name):
		query_string = "SELECT * FROM ID_CARD WHERE country_name LIKE ?;"
		return self.database.r_item(query_string, [country_name])
	
	def get_id_card_number_by_country_name(self, country_name):
		query_string = "SELECT number FROM ID_CARD WHERE country_name LIKE ?;"
		return self.database.r_item(query_string, [country_name])
	
	def get_id_card_expiry_date_by_country_name(self, country_name):
		query_string = "SELECT expiry_date FROM ID_CARD WHERE country_name LIKE ?;"
		return self.database.r_item(query_string, [country_name])
	
	def get_id_card_file_path_by_country_name(self, country_name):
		query_string = "SELECT file_path FROM ID_CARD WHERE country_name LIKE ?;"
		return self.database.r_item(query_string, [country_name])
	
	def get_id_card_image_data_by_country_name(self, country_name):
		img_unavailable_binary = b'R0lGODlh4wDjAJEAAAAAAP///////wAAACH5BAEAAAIALAAAAADjAOMAAAL/hI+py+0Po5y02ouz3rz7D4biSJbmiabqyrbuC8fyTNf2jef6zvf+DwwKh8Si8YhMKpfMpvMJjUqn1Kr1is1qt9yu9wsOi8fksvmMTqvX7Lb7DY/L5/S6/Y7P6/f8vv8PGCg4SFhoeIiYqLjI2Oj4CBkpOUlZaXmJmam5ydnp+QkaKjpKWmp6ipqqusra6voKGys7S1tre4ubq7vL2+v7CxwsPExcbHyMnKy8zNzs/AwdLT1NXW19jZ2tvc3d7f0NHi4+Tl5ufo6err7O3u7+Dh8vP09fb3+Pn6+/z9/v/w8woMCBBAsaPIgwocKFDBs6fAgxosSJFCtavIgxo8aNMRw7evwIMqTIkSRLmjyJMqXKlSxbunwJM6bMmTRr2ryJM6fOnTx7+vwJNKjQoURbFQAAOw=='
		result = self.get_id_card_file_path_by_country_name(country_name)
		if result.get("file_path"):
			current_dir = os.path.dirname(os.path.abspath(__file__))
			try:
				os.chdir(os.path.dirname(result.get("file_path")))
				binary_data_obj = {
					"img_binary_data": str(base64.b64encode(open(result.get("file_path"), "rb").read())).split("'")[1],
					"img_alt": country_name
				}
				os.chdir(current_dir)
				return binary_data_obj
			except:
				return {
					"img_binary_data": str(img_unavailable_binary).split("'")[1],
					"img_alt": "Image Unavailable"
				}
	
	def get_expired_id_cards(self, date):
		query_string = "SELECT * FROM ID_CARD WHERE expiry_date > ?;"
		return self.database.r_list(query_string, [date])
	
	def update_id_card_by_country_name(self, country_name, number, issue_date, expiry_date, address, file_path):
		query_string = "UPDATE ID_CARD SET number = ?, issue_date = ?, expiry_date = ?, address = ?, file_path = ? WHERE country_name like ?;"
		return self.database.r_item(query_string, [number, issue_date, expiry_date, address, file_path, country_name])