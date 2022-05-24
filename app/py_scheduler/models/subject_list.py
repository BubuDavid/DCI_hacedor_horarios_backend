from typing import List
from pydantic import BaseModel

class SubjectList(BaseModel):
    subjects: List[str]