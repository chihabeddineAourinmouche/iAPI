import eel

from backend.controller.id_card_controller import ID_Card_Controller
from backend.controller.contract_controller import Contract_Controller


eel.init("./frontend", allowed_extensions=[".html", ".css", ".js"])





# INITIALIZING CONTROLLERS
id_card_controller = ID_Card_Controller()
contract_controller = Contract_Controller()


# EXPOSING CONTROLLER METHODS
insert_id_card = eel.expose(id_card_controller.insert_id_card)
get_id_card_by_country_name = eel.expose(id_card_controller.get_id_card_by_country_name)
get_id_card_number_by_country_name = eel.expose(id_card_controller.get_id_card_number_by_country_name)
get_id_card_expiry_date_by_country_name = eel.expose(id_card_controller.get_id_card_expiry_date_by_country_name)
get_id_card_file_path_by_country_name = eel.expose(id_card_controller.get_id_card_file_path_by_country_name)
get_id_card_image_data_by_country_name = eel.expose(id_card_controller.get_id_card_image_data_by_country_name)
get_expired_id_cards = eel.expose(id_card_controller.get_expired_id_cards)
update_id_card_by_country_name = eel.expose(id_card_controller.update_id_card_by_country_name)


insert_contract = eel.expose(contract_controller.insert_contract)
get_contract_by_start_date = eel.expose(contract_controller.get_contract_by_start_date)
get_contract_by_end_date = eel.expose(contract_controller.get_contract_by_end_date)
get_contracts_by_signed_in = eel.expose(contract_controller.get_contracts_by_signed_in)
get_contract_by_party = eel.expose(contract_controller.get_contract_by_party)
get_contracts_by_type = eel.expose(contract_controller.get_contracts_by_type)
get_contract_file_path_by_start_date = eel.expose(contract_controller.get_contract_file_path_by_start_date)
get_contract_file_paths_by_signed_in = eel.expose(contract_controller.get_contract_file_paths_by_signed_in)
get_contract_file_path_by_end_date = eel.expose(contract_controller.get_contract_file_path_by_end_date)
get_contract_file_path_by_party = eel.expose(contract_controller.get_contract_file_path_by_party)





eel.start("index.html", mode="default")