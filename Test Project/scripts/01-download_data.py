#### Preamble ####
# Purpose: Downloads and saves the data from OpenToronto
# Author: Aakash Vaithyanathan (translated by ChatGPT)
# Date: September 24, 2024
# Contact: aakash.vaithyanathan@mail.utoronto.ca
# License: MIT
# Pre-requisites: pandas, requests, openpyxl
# Any other information needed? None

#### Workspace setup ####
import pandas as pd
import requests
from pathlib import Path

#### Download data ####
# Define the Open Data Toronto API endpoint for the package
package_id = "b68cb71b-44a7-4394-97e2-5d2f41462a5d"
package_url = f"https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/package_show?id={package_id}"

# Get package metadata
response = requests.get(package_url)
response.raise_for_status()
resources = response.json()["result"]["resources"]

# Find the 2023 TTC delay Excel resource
xlsx_resource = next(r for r in resources 
                     if r["format"].lower() == "xlsx" and 
                        r["name"] == "ttc-streetcar-delay-data-2023")

# Download and read the Excel file
df = pd.read_excel(xlsx_resource["url"], engine="openpyxl")

#### Save data ####
output_path = Path("data/raw_data")
output_path.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path / "unedited_ttc_streetcar_delay_2023.csv", index=False)