from tools.functions import normalize_text

def validate_body_request(subjects, professors_dict = None):
	# ===== Validate Types ===== # 
	assert type(subjects) == list, "Your subject list is not correct list"

	normalized_subjects = []
	for subject in subjects:
		assert type(subject) == str, f"One of your subject items in the subject list is not a string {subject}"
		# Normalize data
		normalized_subjects.append(normalize_text(subject))
		
	if not professors_dict:
		return normalized_subjects, ''
	# ===== Now for professors ===== #
	assert type(professors_dict) == dict, "Your professor list is not a correct list format"

	normalized_professors = {}
	for subject, professors in professors_dict.items():
		assert type(subject) == str, f"One of your subject keys in the professors list is not a string {subject}"
		assert type(professors) == list, f"One of your professor in the professors list is not a list {professors}"
		# Normalize data
		normalized_professors[normalize_text(subject)] = [normalize_text(professor) for professor in professors]

	return normalized_subjects, normalized_professors
	
