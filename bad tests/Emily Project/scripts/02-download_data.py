#### Preamble ####
# Purpose: Downloads and saves the data from Open Data Toronto
# Author: Emily Su
# Date: 7 May 2025
# Contact: em.su@mail.utoronto.ca
# License: MIT
# Pre-requisites: Have the required packages installed by following the instructions in README.md under "Setup".


#### Workspace setup ####
import requests
import csv
from io import StringIO

#### Download data ####
# REFERENCE: From the Open Data Toronto website
url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/package_show"
params = { "id": "catalogue-quality-scores"} # Contains the dataset we want to retrieve 
package = requests.get(url, params = params).json()
 
# Get resource data 
for idx, resource in enumerate(package["result"]["resources"]):
    # for datastore_active resources:
    if resource["datastore_active"]:
        # To get all records in CSV format:
        url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/datastore/dump/" + resource["id"]
        
        # Referenced: https://stackoverflow.com/questions/42834861/csv-file-from-string-output
        #### Save data as a CSV ####
        reader = csv.reader(StringIO(requests.get(url).text), skipinitialspace=True)
        with open('data/01-raw_data/raw_data.csv', 'w') as output_file:
            writer = csv.writer(output_file)
            writer.writerows(reader) # Write in rows into the new file