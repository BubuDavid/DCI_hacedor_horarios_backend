import json
import pyairtable as pa
from py_scheduler import *

def get_airtable_table(api_key, base_id, table_name):
	table = pa.Table(api_key, base_id, table_name)
	
	return table

def update_airtable_table(api_key, base_id, table_name, new_subjects):
	table = get_airtable_table(api_key, base_id, table_name)
	json_all_subjects = table.all()
	for subject in json_all_subjects:
		table.delete(subject["id"])

	print("Deleted them!")

	table.batch_create(new_subjects)

	print("Created!")

	return True
