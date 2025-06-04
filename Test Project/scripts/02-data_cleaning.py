#### Preamble ####
# Purpose: Cleans the raw data into appropriate formats and removes missing values
# Author: Aakash Vaithyanathan (translated by ChatGPT)
# Date: September 24, 2024
# Contact: aakash.vaithyanathan@mail.utoronto.ca
# License: MIT
# Pre-requisites: pandas, numpy
# Any other information needed? None

#### Workspace setup ####
import pandas as pd
import numpy as np
from pathlib import Path

#### Clean data ####
raw_data = pd.read_csv("data/raw_data/unedited_ttc_streetcar_delay_2023.csv")

# Standardize column names (snake_case)
raw_data.columns = (
    raw_data.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

# Split 'date' into 'year' and 'month'
date_split = raw_data["date"].str.split("-", expand=True)
raw_data["year"] = date_split[0]
raw_data["month"] = date_split[1]

# Extract hour from 'time'
raw_data["hour"] = raw_data["time"].str.split(":", expand=True)[0]

# Assign season based on month
raw_data["season"] = raw_data["month"].map({
    "03": "Spring", "04": "Spring", "05": "Spring",
    "06": "Summer", "07": "Summer", "08": "Summer",
    "09": "Fall",   "10": "Fall",   "11": "Fall",
    "12": "Winter", "01": "Winter", "02": "Winter"
})

# Drop rows with missing values
cleaned_data = raw_data.dropna()

# Convert relevant columns to numeric
cols_to_convert = ["year", "month", "hour", "min_delay", "line"]
for col in cols_to_convert:
    cleaned_data[col] = pd.to_numeric(cleaned_data[col], errors="coerce")

# Filter out rows with min_delay = 0 or >= 121
cleaned_data = cleaned_data[
    (cleaned_data["min_delay"] != 0) & (cleaned_data["min_delay"] < 121)
]

# Select relevant columns
cleaned_data = cleaned_data[["year", "month", "hour", "incident", "min_delay", "line", "season"]]

#### Save data ####
output_path = Path("data/analysis_data")
output_path.mkdir(parents=True, exist_ok=True)
cleaned_data.to_csv(output_path / "cleaned_ttc_streetcar_delay_2023.csv", index=False)