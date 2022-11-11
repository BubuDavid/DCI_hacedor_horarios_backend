from typing import Dict
from pydantic import BaseModel, Field, conlist

# Class for receiving the Body in the Endpoints of request schedules
class SubjectList(BaseModel):
	# Receives a constrained list (constrained to string objects and between 0 and 10 elements)
	subjects : conlist(
		str,
		min_items = 0,
		max_items = 10
	)

	# And a dictionary of constrains
	constraints: Dict[str, str] = Field(
		default=None
	)