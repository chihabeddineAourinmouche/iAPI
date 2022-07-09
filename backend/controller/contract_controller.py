from backend.controller.controller import Controller

class Contract_Controller(Controller):

	def insert_contract(self, type, parties, start_date, end_date, signed_in, file_path):
		"""
			EXPECTS DATES IN THE FORM dd-mm-yyyy, i.e. "1-2-1990", "20-11-2022"
		"""
		start_date = "-".join(list(map(lambda e: e[1] if e[0] == "0" else e, start_date.split("-"))))
		end_date = "-".join(list(map(lambda e: e[1] if e[0] == "0" else e, end_date.split("-"))))
		query_string_1 = "INSERT INTO CONTRACT(type, start_date, end_date, signed_in, file_path);"
		query_string_2 = f'INSERT INTO CONTRACT_PARTIES(party) VALUES {",".join(list(map(lambda p: f"(?)", parties)))};'
		try:
			self.database.cud(query_string_1, [type, start_date, end_date, signed_in, file_path])
			self.database.cud(query_string_2, parties)
		except Exception as e:
			print("backend", "contract_controller", "insert_contract", e)
	
	def get_contract_by_start_date(self, start_date):
		start_date = "-".join(list(map(lambda e: e[1] if e[0] == "0" else e, start_date.split("-"))))
		query_string = "SELECT * FROM CONTRACT WHERE start_date LIKE ?;"
		return self.database.r_item(query_string, [start_date])
	
	def get_contract_by_end_date(self, end_date):
		end_date = "-".join(list(map(lambda e: e[1] if e[0] == "0" else e, end_date.split("-"))))
		query_string = "SELECT * FROM CONTRACT WHERE end_date LIKE ?;"
		return self.database.r_item(query_string, [end_date])
	
	def get_contracts_by_signed_in(self, signed_in):
		query_string = "SELECT * FROM CONTRACT WHERE signed_in LIKE ?;"
		return self.database.r_list(query_string, [signed_in])
	
	def get_contract_by_party(self, party):
		query_string = "SELECT CONTRACT.* FROM CONTRACT JOIN CONTRACT_PARTIES WHERE CONTRACT.id LIKE CONTRACT_PARTIES.contract_id AND CONTRACT_PARTIES.party LIKE ?;"
		return self.database.r_item(query_string, [party])
	
	def get_contracts_by_type(self, type):
		query_string = "SELECT * FROM CONTRACT WHERE type LIKE ?;"
		return self.database.r_list(query_string, [type])
	
	def get_contract_file_path_by_start_date(self, start_date):
		start_date = "-".join(list(map(lambda e: e[1] if e[0] == "0" else e, start_date.split("-"))))
		query_string = "SELECT file_path FROM CONTRACT WHERE start_date LIKE ?;"
		return self.database.r_item(query_string, [start_date])
	
	def get_contract_file_paths_by_signed_in(self, signed_in):
		query_string = "SELECT file_path FROM CONTRACT WHERE signed_in LIKE ?;"
		return self.database.r_list(query_string, [signed_in])
	
	def get_contract_file_path_by_end_date(self, end_date):
		end_date = "-".join(list(map(lambda e: e[1] if e[0] == "0" else e, end_date.split("-"))))
		query_string = "SELECT file_path FROM CONTRACT WHERE end_date LIKE ?;"
		return self.database.r_item(query_string, [end_date])
	
	def get_contract_file_path_by_party(self, party):
		query_string = "SELECT CONTRACT.file_path FROM CONTRACT JOIN CONTRACT_PARTIES WHERE CONTRACT.id LIKE CONTRACT_PARTIES.contract_id AND CONTRACT_PARTIES.party LIKE ?;"
		return self.database.r_item(query_string, [party])