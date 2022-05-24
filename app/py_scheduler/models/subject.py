from textwrap import indent
from typing import List
from .day import Day
import json

class Subject:
	param_list = [
	'_id',
	'name',
	'group',
	'time_zones',
	'professor1',
	'professor_email1',
	'professor2',
	'professor_email2',
	'day1',
	'day2',
	'day3'
	]
	def __init__(
		self,
		_id             : int,
		name            : str,
		time_zones      : List[Day],
		group           : str = None,
		professor1      : str = None,
		professor_email1: str = None,
		professor2      : str = None,
		professor_email2: str = None,
		day1            : str = None,
		day2            : str = None,
		day3            : str = None,
		**kwargs
	) -> None:
		self._id              = _id
		self.name             = name
		self.group            = group
		self.time_zones       = time_zones
		self.professor1       = professor1
		self.professor_email1 = professor_email1
		self.professor2       = professor2
		self.professor_email2 = professor_email2
		self.day1             = day1
		self.day2             = day2
		self.day3             = day3


	def __str__(self) -> str:
		params = ''
		for d in dir(self):
			if '__' not in d:
				if "time_zones" not in d:
					params += f"{d}: {getattr(self, d)}\n"
				else:
					for index, day in enumerate(getattr(self, d)):
						params += f"Day{index+1}: {str(day)}\n"

		return params

	def for_jsonify(self):
		sub_json = {}
		for param in self.param_list:
			if "time_zones" not in param:
				sub_json[param] = getattr(self, param)
			else:
				for index, day in enumerate(getattr(self, param)):
					sub_json[f"day{index + 1}"] = day.for_jsonify()

		return sub_json
		