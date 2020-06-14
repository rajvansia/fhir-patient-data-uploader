import json
import os
import requests

URL = "http://localhost:8080/hapi-fhir-jpaserver/fhir/"

headers = {"Content-Type": "application/fhir+json;charset=utf-8"}

bundle = "/Users/rajvansia/Documents/GitHub/synthea/output/fhir/Abdul218_Keeling57_c754e34b-b690-424d-bf48-23418380b906.json"

with open(bundle, "r") as bundle_file:
        data = bundle_file.read()

r = requests.post(url = URL, data = data, headers = headers)

resource = r.json()
print(json.dumps(resource, indent=2))
