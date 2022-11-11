# My imports
from config import config_app
from tools.airtable_tools import get_subject_name_list, get_professor_name_list
from models.SubjectList import SubjectList

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
def get_schedules(subject_list: SubjectList):
	subjects = subject_list.subjects
	constraints = subject_list.constraints

	return {'subjects': subjects, 'constraints': constraints}