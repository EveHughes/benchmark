#### Preamble ####
# Purpose: Tests whether simulated data contain valid entries or not
# Author: Aakash Vaithyanathan (translated by ChatGPT)
# Date: September 24, 2024
# Contact: aakash.vaithyanathan@mail.utoronto.ca
# License: MIT
# Pre-requisites: pandas
# Any other information needed? None

#### Workspace setup ####
import pandas as pd

#### Load cleaned dataset ####
data = pd.read_csv("data/analysis_data/cleaned_ttc_streetcar_delay_2023.csv")

#### Run tests ####

# Check for missing values
assert not data.isna().any().any(), "There are missing values in the dataset"

# Check data types
assert data["season"].dtype == object, "Season should be of type string/object"
assert pd.api.types.is_numeric_dtype(data["line"]), "Line should be numeric"
assert pd.api.types.is_numeric_dtype(data["min_delay"]), "min_delay should be numeric"
assert pd.api.types.is_numeric_dtype(data["year"]), "year should be numeric"
assert pd.api.types.is_numeric_dtype(data["month"]), "month should be numeric"
assert pd.api.types.is_numeric_dtype(data["hour"]), "hour should be numeric"
assert data["incident"].dtype == object, "Incident should be of type string/object"

# Check ranges and values
assert data["month"].between(1, 12).all(), "Month values must be between 1 and 12"
assert (data["year"] == 2023).all(), "Year should be 2023"
assert data["hour"].between(0, 23).all(), "Hour values must be between 0 and 23"
assert (data["min_delay"] >= 0).all(), "Delays must be non-negative"
assert (data["min_delay"] <= 120).all(), "Delays must be less than or equal to 120 minutes"

# Check valid seasons
valid_seasons = {"Winter", "Spring", "Summer", "Fall"}
assert data["season"].isin(valid_seasons).all(), "Invalid season values detected"

# Check incident descriptions are non-empty
assert (data["incident"].str.strip().str.len() > 0).all(), "Incident descriptions must be non-empty"

print("All tests passed.")