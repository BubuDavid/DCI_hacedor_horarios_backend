# FastAPI imports
from fastapi import HTTPException
from fastapi.responses import RedirectResponse

# My imports
from config import config_app
from tools.airtable_tools import get_subject_name_list, get_professor_name_list, get_all_schedules
from models.Models import SubjectList, SubjectListWithProfessors
from py_scheduler.validations import validate_body_request
from py_scheduler.py_scheduler import generate_my_schedules, filter_by_professor

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
@app.post("/professor-names")
def professor_names(subject_list: SubjectList):

	try:
		subjects = subject_list.subjects
	except:
		if not subject_list:
			error = 'You need to pass a subjects list'
		else:
			error = f'There is something wrong with your subject_list: {subject_list}'
		raise HTTPException(
				status_code=422,
				detail=error)
		

	subjects_professor_dict = get_professor_name_list(subjects)
	return subjects_professor_dict

# Endpoint for getting all the combinations given a list of subjects
@app.post("/get-schedules")
async def get_schedules(subject_list: SubjectList):
	subjects = subject_list.subjects
	all_schedules = get_all_schedules()
	# Validation of Data
	try:
		norm_subjects, _ = validate_body_request(subjects)
	except AssertionError as error:
		raise HTTPException(
			status_code=422,
			detail=str(error))

	# Generate schedules with validated data
	there_are_combs, result = generate_my_schedules(all_schedules, norm_subjects)
	
	# Return in case there are combinations or not
	return {
		'there_are_combs': there_are_combs,
		'length_of_result': len(result),
		'result': result
	}


# Endpoint for getting all the combinations given a list of subjects and forbidden professors
@app.post("/get-schedules-with-professors")
async def get_schedules_with_professors(subjects_professors: SubjectListWithProfessors):
	subjects = subjects_professors.subjects
	professors = subjects_professors.professors

	all_schedules = get_all_schedules()
	# Validation of Data
	try:
		norm_subjects, norm_professors = validate_body_request(subjects, professors)
	except AssertionError as error:
		raise HTTPException(
			status_code=422,
			detail=str(error))

	# Generate schedules with validated data
	there_are_combs, result = generate_my_schedules(all_schedules, norm_subjects)
	empty = False
	if professors:
		if there_are_combs:
			there_are_combs, result = filter_by_professor(result, norm_professors)
			if not there_are_combs:
				empty = 'PROFESSORS'
		else:
			empty = 'COMBINATIONS'
	elif not there_are_combs:
		empty = 'COMBINATIONS'	

	
	# Return in case there are combinations or not
	return {
		'there_are_combs': there_are_combs,
		'length_of_result': len(result),
		'result': result,
		'why_empty': empty
	}