from config import airtable_variables_loader
import pyairtable as pa


def get_subjects_table():
	"""
		Description: Function to get the complete table from airtable
		Return: A table from airtable
		Return Type: <class 'pyairtable.api.table.Table'>
	"""
	# Get airtable environmental variables
	airtable_env_vars = airtable_variables_loader()
	# Use pyairtable for get the table
	table = pa.Table(
		airtable_env_vars['api_key'],
		airtable_env_vars['base_id'], 
		airtable_env_vars['table_name']
	)
	return table # Return the table



def get_subject_name_list():
	"""
		Description: Function to get only the subject names in a sorted list.
		Return: A sorted list with the subject names.
		Return Type: <class 'list'>
	"""
	# Get all the table
	table = get_subjects_table().all()
	# Map the name field into a variable
	names = set(map(lambda record: record['fields']['NAME'], table))
	# Return the sorted list
	return sorted(list(names))

def get_professor_name_list():
	# Get all the table
	table = get_subjects_table().all()
	# Map the name field into a variable
	names_field = list(map(lambda record: record['fields']['PROFESSORS'], table))
	# Filter all the professors
	professor_names = set()
	for field in names_field:
		names = field.split('/')
		for name in names:
			professor_names.add(name.strip())

	return sorted(list(professor_names))