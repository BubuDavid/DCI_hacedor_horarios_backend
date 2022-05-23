import unicodedata

def super_normalize(s):
	return ''.join(c for c in unicodedata.normalize('NFD', s) 
					if unicodedata.category(c) != 'Mn').upper()


def extract_id_matrix(subjects):
	matrix = []

	for _, s_list in subjects.items():
		ids = []
		for subject in s_list:
			ids.append(subject._id)
		matrix.append(ids)

	return matrix