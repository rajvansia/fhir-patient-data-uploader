import json
import os
import requests


#fhir server endpoint
URL = "http://localhost:8080/hapi-fhir-jpaserver/fhir/"

#fhir server json header content
headers = {"Content-Type": "application/fhir+json;charset=utf-8"}

#loop over all files in the output folder in order to upload each json file for each patient.
for dirpath, dirnames, files in os.walk('/Users/rajvansia/Documents/GitHub/synthea/output/fhir'):

    for file_name in files:
        with open('/Users/rajvansia/Documents/GitHub/synthea/output/fhir/'+file_name, "r") as bundle_file:
                data = bundle_file.read()

        r = requests.post(url = URL, data = data, headers = headers)

        #output file name that was processed
        print(file_name)
