import requests
from bs4 import BeautifulSoup
from .tools import super_normalize

def fetch_page(url):
	page = requests.get(url)
	return BeautifulSoup(page.content, 'html.parser')

def get_rows(page):
	table = page.find_all('tbody')[1]
	rows = table.find_all("tr")
	return rows

def get_column_names(column_names):
	table_column_names = []
	for data in column_names: # Ignoring the index
		table_column_names.append(super_normalize(data.strip()))

	return table_column_names

def get_content_rows(rows):
	pd_rows = []
	for index, row in enumerate(rows):
		pd_row = [index] # Note is different from pd_rows
		for data in row.find_all('td')[1:]:
			text = data.text.strip()
			normalized_text = super_normalize(text)
			pd_row.append(normalized_text) # Save the rows
		pd_rows.append(pd_row)

	return pd_rows

def scrap(url, column_names):
	# Request the page
	print("Fetching the page...")
	html_page = fetch_page(url)
	# Get all the rows
	rows = get_rows(html_page)
	# Get the column names
	table_column_names = get_column_names(column_names)
	# Get the rows in a python matrix (list of lists)
	list_rows = get_content_rows(rows[1:])
	# Create a new subject list
	new_subjects_list = []

	for row in list_rows:
		new_subject = {}
		for name, info in zip(table_column_names, row):
			new_subject[name] = info
		new_subjects_list.append(new_subject)

	return new_subjects_list