from pydantic import BaseModel, Field, conlist

# Class for receiving the Body in the Endpoints of request schedules
class SubjectList(BaseModel):
	# Receives a constrained list (constrained to string objects and between 0 and 10 elements)
	subjects : conlist(
		str,
		min_items = 0,
		max_items = 10
	) = Field(
		...,
		example = [
			'ALEMAN I',
			'ALGEBRA LINEAL',
			'ANALISIS DE CIRCUITOS',
			'ANALISIS DE LA CULTURA MEXICANA',
			'ANALISIS TENSORIAL',
			'ANALISIS VECTORIAL'
		]
	)

# Class for receiving the constraints for professors
class SubjectListWithProfessors(BaseModel):
	# Receives a constrained list (constrained to string objects and between 0 and 10 elements)
	subjects : conlist(
		str,
		min_items = 0,
		max_items = 10
	) = Field(
		...,
		example = [
			'ALEMAN I',
			'ALGEBRA LINEAL',
			'ANALISIS DE CIRCUITOS',
			'ANALISIS DE LA CULTURA MEXICANA',
			'ANALISIS TENSORIAL',
			'ANALISIS VECTORIAL'
		]
	)
	# Receives a constrained list (constrained to string objects)
	professors : dict[str, list[str]] = Field(
		default=None,
		example = {
			'analisis de circuitos': ['carlos villaseñor mora'],
		}
	)

