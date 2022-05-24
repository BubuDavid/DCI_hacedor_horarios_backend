# When the data base is horrible I will fix it by hand
def manage_row_exceptions(row):
	if (row["_ID"] == 43):
		print("File _ID 43 fixed")
		row["DAY/HOUR/ROOM1"] = "MARTES/15-17/F2"

	return row

def manage_empty_rows(rows):
	rows = list(filter(
		lambda x: True if x.get('NAME', '') else False,
		rows
	))

	return rows