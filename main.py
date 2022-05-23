from fastapi import FastAPI, Header, BackgroundTasks
from decouple import config
from fastapi.middleware.cors import CORSMiddleware
from numpy import sort
from py_scheduler.manage_exceptions import manage_empty_rows

from tools.airtable_tools import *
from py_scheduler import *


# ====== AIRTABLE ENV VARIABLES ====== #
air_api_key = config("AIRTABLE_API_KEY")
air_base_id = config("AIRTABLE_BASE_ID")
air_table_name = config("AIRTABLE_TABLE_NAME")
air_names_table_name = config("AIRTABLE_NAMES_TABLE_NAME")
# ====== OTHER ENV VARIABLES ====== #
try:
	update_password = config("UPDATE_PASSWORD")
except:
	update_password = None

app = FastAPI()

# CORS POLICY CORRECTION
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ["GET", "POST"],
)

@app.get("/")
def hello_endpoint():
	return {"Hola": "World"}

@app.post("/get-schedule")
async def get_schedule_endpoint(body: SubjectList):
	my_subjects = body.subjects
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

@app.post('/update-table')
async def update_table_endpoint(background_tasks: BackgroundTasks, password: str = Header('')):
	if password != update_password:
		return "You need the password"

	column_names = [
		"_id",
		"name",
		"group",
		"day/hour/room1",
		"day/hour/room2",
		"day/hour/room3",
		"professor1",
		"professor_email1",
		"professor2",
		"professor_email2",
	]
	url = "http://www.dci.ugto.mx/estudiantes/index.php/mcursos/horarios-licenciatura"
	new_subjects = scrap(url, column_names)
	new_subjects = manage_empty_rows(new_subjects)

	new_subject_names = [subject['NAME'] for subject in new_subjects]
	new_subject_names = sort(list(set(new_subject_names)))
	new_subject_names = [
		{
			"NAME": subject,
			"_ID": index
		}
		for index, subject in enumerate(new_subject_names)
	]
	
	background_tasks.add_task(
		update_airtable_table,
		air_api_key,
		air_base_id,
		air_table_name,
		new_subjects
	)

	background_tasks.add_task(
		update_airtable_table,
		air_api_key,
		air_base_id,
		air_names_table_name,
		new_subject_names
	)

	background_tasks.add_task(
		update_date,
		air_api_key,
		air_base_id,
	)

	return {
		"Status": "Everything is fine! ❤️‍🔥, the updating is running in the background"
	}


@app.get('/update-table')
def update_table_method_get():
	table = get_airtable_table(air_api_key, air_base_id, "updated_date")
	last = table.all()[-1]
	return {
		"last_update": last
	}