from tools.functions import normalize_text

def validate_body_request(subjects):
	# ===== Validate Types ===== # 
	assert type(subjects) == list, "Your subject list is not correct list"

	normalized_subjects = []
	for subject in subjects:
		assert type(subject) == str, f"One of your subject items in the subject list is not a string {subject}"
		# Normalize data
		normalized_subjects.append(normalize_text(subject))

	return subjects
	
