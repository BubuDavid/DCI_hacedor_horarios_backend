from pyairtable import Table

def get_airtable_table(api_key, base_id, table_name):
	table = Table(api_key, base_id, table_name)
	
	return table