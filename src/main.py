from typing import List
from fastapi import FastAPI
from decouple import config


from tools.airtable_tools import *
from py_scheduler import *


# ====== AIRTABLE ENV VARIABLES ====== #
air_api_key = config("AIRTABLE_API_KEY")
air_base_id = config("AIRTABLE_BASE_ID")
air_table_name = config("AIRTABLE_TABLE_NAME")

app = FastAPI()

@app.get("/")
def hello_endpoint():
	return "Hello"

@app.post("/get-schedule")
def get_schedule_endpoint(my_subjects: List[str]):
	json_all_subjects = get_airtable_table(
		air_api_key,
		air_base_id,
		air_table_name
	).all()
	# ============ Transform the JSON to a list of Subject objects ============ #
	all_subjects = from_json_to_subjects(json_all_subjects)
	# ============ Normalize my subs and filter all subjects ============ #
	all_my_subjects = filter_my_subjects(my_subjects, all_subjects)
	# ============ Make every possible permutation of this subjects ============ #
	all_permutations = make_permutations(all_my_subjects)
	# ============ Filter the validate permutations (no overlap) ============ #
	validated_permutations = list(filter(filter_permutations, all_permutations))
	# ============ Transform the Subject List into a python dicctionary ============ #
	my_subjects_json = from_subjects_to_json(validated_permutations, False)

	return my_subjects_json
