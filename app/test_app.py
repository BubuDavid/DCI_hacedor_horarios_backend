import requests as req
from decouple import config

backend_url = config("URL_API")

data = {
  "subjects": [
    "ALEMAN I",
    "ALGEBRA LINEAL",
    "ANALISIS DE CIRCUITOS",
    "ANALISIS DE LA CULTURA MEXICANA",
    "ANALISIS TENSORIAL",
    "ANALISIS VECTORIAL"
  ],
  "professors": {
    "analisis de circuitos": [
      "carlos villaseñor mora"
    ]
  }
}

res = req.post(
    url=backend_url,
    json=data
)

print(res.json())