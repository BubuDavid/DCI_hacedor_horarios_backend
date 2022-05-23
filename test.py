import requests
from decouple import config

update_password = config("UPDATE_PASSWORD")

def main():
	url = 'http://3.19.209.231:8000/update-table'
	headers = {
		'password': update_password
	}
	response = requests.post(
		url,
		headers=headers
	)

	print(response.json())

if __name__ == "__main__":
	main()