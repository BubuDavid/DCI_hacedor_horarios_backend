# 👇 THIS CODE IS READ FROM BOTTOM TO TOP 👆
# 🔚 This is the end 🔚 #

def create_index_matrix(all_schedules, subjects):
	"""
	Description: Create an indices matrix, each row is a subject and each column is an index in all_subjects.
	Input:
		- all_schedules: A dictionary of all the schedules in the page
		- subjects: A list of subject names. (The ones you want to combine)
	Returns: [
		['4'],
		['17','18'],
		['125', '126', '127', '128'],
		['240'],
	]
	Return Type: List[List[str]]
	Note: That 👆 "str" inside of the lists, is the _ID, but is string because of the API formatting
		  I will work with _ID as string so there is no problem
	"""

	# There are not in order, so I need to store them in a dictionary and then translate them into a matrix
	subject_indices = {subject:[] for subject in subjects}
	for id, schedule in all_schedules.items():
		if schedule['NAME'] in subjects:
			subject_indices[schedule['NAME']].append(id)

	# Matrix translation
	index_matrix = []
	for index_list in subject_indices.values():
		index_matrix.append(index_list)

	# Filter subjects that not exists in the database
	index_matrix_filtered = list(filter(
		lambda sub_list: bool(len(sub_list)),
		index_matrix
	))
	
	return index_matrix_filtered

# All combinations generator
def create_all_combinations(schedule_index_matrix):
	"""
	Description: Create a list with all the possible combinations for a indices_matrix
	Input: 
		- schedule_index_matrix: The matrix of indices which is needed to create the combinations from
	Returns: A list of list with the combinations for every index, each element of this list 
				has the length N, where N = len(schedule_index_matrix)
	Return Type: List[List[str]]
	Note: That 👆 "str" inside of the lists, is the _ID, but is string because of the API formatting
		I will work with _ID as string so there is no problem
	"""
	all_combinations = []
	indices = [0 for schedule in schedule_index_matrix] # A list of index
	while True:
		all_combinations.append([schedule_index_matrix[i][index] for i, index in enumerate(indices)]) # Guardamos la combinación actual
		next = len(schedule_index_matrix) - 1 # Empezamos a cambiar de izquierda a derecha
		# Checamos si ya nos salimos por completa de la matriz o si nos pasamos de tamaño de cada fila
		while next >= 0 and indices[next] == len(schedule_index_matrix[next]) - 1:
			next -= 1
		if next < 0 :
			break
		indices[next] += 1
		for index in range(next + 1, len(indices)):
			indices[index] = 0 

	return all_combinations

def check_spliced_time(s1, s2, i1, i2):
	# Get the correct column time for comparison
	s1_time_column = f'TIME{i1}'
	s2_time_column = f'TIME{i2}'

	# Separate in parts, start and end for each schedule
	# The simplest way to do this is to compare with numbers if the ranges are not splicing.
	# That is why I am mapping to float, also, it is probable that some times have an ":" that's why I replace it.
	start1, end1 = map(lambda t: float(t.replace(':', '.')), s1[s1_time_column].split('-'))
	start2, end2 = map(lambda t: float(t.replace(':', '.')), s2[s2_time_column].split('-'))

	# Comparing time!
	if start1 >= end2 or start2 >= end1:
		return False
	else:
		return True




# Check if two schedules are overlapping
def are_spliced(sid1, sid2, all_schedules):
	"""
	Description: Check if two schedules are spliced or not
	Input: 
		- sid1: The schedule id (in all_schedules) to compare with schedule_id2
		- sid2: The schedule id (in all_schedules) to compare with schedule_id1
	Returns: True or false depending on the situation of schedule_id1 and schedule_id2
	Return Type: Bool
	"""
	# Getting all the important info from every schedule
	schedule1 = all_schedules[sid1]
	schedule2 = all_schedules[sid2]
	# Get the day columns for each schedule (because some of then doesn't have the same columns as others)
	s1_day_columns = [day for day in schedule1.keys() if 'DAY' in day and 'TIME' not in day]
	s2_day_columns = [day for day in schedule2.keys() if 'DAY' in day and 'TIME' not in day]


	# Its time to compare
	for day1 in s1_day_columns:
		for day2 in s2_day_columns:
			if schedule1[day1] == schedule2[day2]:
				if check_spliced_time(schedule1, schedule2, day1[-1], day2[-1]): 
					return True, [schedule1, schedule2]

	return False, []

def schedule_validator(all_schedules, combination_indices):
	"""
	Description: This is a assistant function for filter() object created in the "Main function" below.
				 Remove all the combinations that has spliced schedules
	Input: 
		- all_schedules: A dictionary of all the schedules in the page
		- combination_index: combination list ['4', '123', '140']
	Returns: True or False depending on the combination_index list, if the schedules are valid or not
	Return Type: Bool
	"""
	# We need to validate for every pair in the schedules
	for index1, schedule_id1 in enumerate(combination_indices):
		for schedule_id2 in combination_indices[index1 + 1:]:
			are_spliced_checker, spliced_subjects = are_spliced(schedule_id1, schedule_id2, all_schedules)
			if are_spliced_checker:
				spliced_names = list(map(
					lambda subject: {
						'NAME': subject['NAME'], 
						'GROUP': subject['GROUP'],
						'_ID': subject['_ID']
					},
					spliced_subjects
				))
				return False, spliced_names

	return True, []

def filter_by_professor(schedules, professors):
	new_schedules = []
	professor_detector = False
	for schedule in schedules:
		for subject in schedule:
			professor_detector = False
			if subject['NAME'] in professors:
				for professor in professors[subject['NAME']]:
					if professor in subject['PROFESSORS']:
						professor_detector = True
						break
			if professor_detector:
				break
		if not professor_detector:
			new_schedules.append(schedule)

	return len(new_schedules) > 0, new_schedules
			


# 👇👇👇👇 THIS IS THE "MAIN" FUNCTION 👇👇👇👇
def generate_my_schedules(all_schedules, subjects):
	# Create the index matrix, see 👆 to understand what it does:
	index_matrix = create_index_matrix(all_schedules, subjects)
	if not index_matrix:
		return False, []
	# Generate combinations
	all_combinations_index = create_all_combinations(index_matrix)
	# Validate those combinations
	valid_combinations = []
	for combination in all_combinations_index:
		is_valid, spliced_subjects = schedule_validator(all_schedules, combination)
		if is_valid:
			valid_combinations.append(combination)
	# If there are not valid combinations then we need to notify the user
	if not valid_combinations:
		return False, spliced_subjects
	
	# Translate the valid schedule ids to actual schedule objects
	valid_schedules = []
	for combination in valid_combinations:
		new_schedule = []
		for index in combination:
			new_schedule.append(all_schedules[index])

		valid_schedules.append(new_schedule)

	return True, valid_schedules


# 🔝 This is the start 🔝 #