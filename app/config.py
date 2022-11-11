from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

def airtable_variables_loader():
	airtable_env_variables = {}
	airtable_env_variables["api_key"]    = config("AIRTABLE_API_KEY")
	airtable_env_variables["base_id"]    = config("AIRTABLE_BASE_ID")
	airtable_env_variables["table_name"] = config("AIRTABLE_TABLE_NAME")

	return airtable_env_variables


def config_app():
	# INITAL APP
	app = FastAPI()
	# CORS POLICY CORRECTION 
	app.add_middleware(
		CORSMiddleware,
		allow_origins = ["*"],
		allow_credentials = True,
		allow_methods = ["*"],
		allow_headers = ["*"],
	)

	return app