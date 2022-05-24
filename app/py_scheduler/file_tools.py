import pandas as pd

def check_for_table_file(check, name):
	# We not always want to check for the file
	if not check:
		return check

	try:
		f = open(f"{name}.csv", "r")
		return True
	except:
		return False

def create_file(file_name, data, columns, index=False):
	df = pd.DataFrame(data, columns=columns)
	df.to_csv(f"{file_name}.csv", index=index)
	print("File created!")
	return df
	

def read_table_file(file_name):
	try:
		df = pd.read_csv(f"{file_name}.csv", header=0)
		return df
	except:
		raise Exception("El archivo no existe!")

def get_my_subjects(file_name):
	lines = []
	try:
		with open(file_name, 'r') as f:
			for line in f:
				lines.append(line)
	except:
		raise Exception("El archivo no existe!")

	return lines