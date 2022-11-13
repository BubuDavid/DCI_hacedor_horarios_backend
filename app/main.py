# FastAPI imports
from fastapi import HTTPException
from typing import Optional

# My imports
from config import config_app
from tools.airtable_tools import get_subject_name_list, get_professor_name_list, get_all_schedules
from models.Models import SubjectList
from py_scheduler.validations import validate_body_request
from py_scheduler.py_scheduler import generate_my_schedules

# ====== FASTAPI CONFIGURATION ====== #
app = config_app()
# =================================== #


# ====== FASTAPI ENDPOINTS ====== #

# Endpoint for testing
@app.get("/")
def hello_endpoint():
	return {"Bubulu": "Buenos días"}

# Endpoint for getting the subject names in a list
@app.get("/subject-names")
def subject_names():
	subject_names_list = get_subject_name_list()
	return subject_names_list

# Endpoint for getting all the professors
@app.get("/professor-names")
def professor_names():
	professor_names_list = get_professor_name_list()
	return professor_names_list

# Endpoint for getting all the combinations given a list of subjects
@app.post("/get-schedules")
async def get_schedules(subject_list: SubjectList):
	subjects = subject_list.subjects
	all_schedules = get_all_schedules()
	# Validation of Data
	try:
		norm_subjects = validate_body_request(subjects)
	except AssertionError as error:
		raise HTTPException(
			status_code=422,
			detail=str(error))

	# Generate schedules with validated data
	at_least_one, result = generate_my_schedules(all_schedules, norm_subjects)
	
	# Return in case there are combinations or not
	return {
		'at_least_one': at_least_one,
		'result': result
	}