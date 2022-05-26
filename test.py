import requests
from decouple import config

update_password = config("UPDATE_PASSWORD")

def main():
	url = 'https://jojj97ftph.execute-api.us-east-2.amazonaws.com/dev/update-table'
	headers = {
		'password': update_password
	}
	response = requests.get(
		url,
		headers=headers
	)

	print(response.json())

if __name__ == "__main__":
	main()