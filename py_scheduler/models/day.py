import json
from typing import List

class TimeRange:
	def __init__(
		self, 
		low: float = None,
		high: float = None
	) -> None:
		self.low = low
		self.high = high
		self.time_range = [low, high]

	def __str__(self):
		return f"{self.low} - {self.high}"

	def is_overlapping(self, time_range):
		if not self.low or not time_range.low:
			return False
		if self.low < time_range.low and self.high <= time_range.low:
			return False
		if time_range.low < self.low and time_range.high <= self.low:
			return False

		return True

	def for_jsonify(self):
		return self.time_range
		

class Day:
	def __init__(self,
	day       : str,
	time_range: TimeRange, 
	room      : str
	) -> None:
		self.day        = day
		self.time_range = time_range
		self.room       = room

	def __str__(self):
		return f"{self.day}/{str(self.time_range)}/{self.room}"

	def for_jsonify(self):
		day_json = []
		day_json.append(self.day)
		day_json.append(self.time_range.for_jsonify())
		day_json.append(self.room)

		return day_json
