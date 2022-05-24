from py_scheduler.subject_tools import print_subject_list
from .tools import extract_id_matrix
from itertools import product

def select_subjects_from_id(subjects, id_permutation):
	s_set = []
	for _, s_list in subjects.items():
		for subject in s_list:
			if subject._id in id_permutation:
				s_set.append(subject)
				break

	return s_set

def make_permutations(subjects):
	all_permutations = []
	# We need a matrix of id's to make the permutations
	# ID column will be used to do this, ID permutations = Subject permutations
	id_matrix = extract_id_matrix(subjects)
	all_id_permutations = list(product(*id_matrix))
	for id_permutation in all_id_permutations:
		all_permutations.append(select_subjects_from_id(subjects, id_permutation))

	return all_permutations


def filter_permutations(permutation):
	days = {}
	for subject in permutation:
		for time_zone in subject.time_zones:
			if time_zone.day not in days:
				days[time_zone.day] = []
			current_time_range = time_zone.time_range

			for time_range in days[time_zone.day]:
				if current_time_range.is_overlapping(time_range):
					return False

			days[time_zone.day].append(current_time_range)
	
	return True