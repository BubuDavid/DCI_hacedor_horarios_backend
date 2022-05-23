import json
import pyairtable as pa
from py_scheduler import *

def get_airtable_table(api_key, base_id, table_name):
	table = pa.Table(api_key, base_id, table_name)
	
	return table

def update_airtable_table(api_key, base_id, table_name, new_subjects):
	table = get_airtable_table(api_key, base_id, table_name)
	json_all_subjects = table.all()
	ids = []
	for subject in json_all_subjects:
		ids.append(subject["id"])

	table.batch_delete(ids)
	print("Deleted!")
	table.batch_create(new_subjects)
	print("Created!")

	return True

def update_date(api_key, base_id, table_name="update_date"):
	table = get_airtable_table(api_key, base_id, table_name)
	last_update = -1
	try:
		last_update = table.all()[-1]
	except: 
		pass

	# Get the date
	date = str(datetime.date(datetime.now()))
	table.create({'updated_date': date})
	
	print("Last update: ", last_update)
	print("Updated!")
	return last_update