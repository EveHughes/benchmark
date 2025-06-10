from pydantic import BaseModel, Field, ValidationError, field_validator
from datetime import date

# Define the Pydantic model
class HateCrimes(BaseModel):
    occurrence_date: date #must be of the form yyyy-mm-dd
    reported_date: date #must be of the form yyyy-mm-dd
    division: str #must be a string
    location_type: str #must be a string
    primary_offence: str #must be a string
    neighbourhood: str #must be a string
    arrest: str # should be yes or no

    @field_validator("division")
    def reject_na_division(cls,v):
        not_allowed = {"NA"}
        if v in not_allowed:
            raise ValueError(f'"{v}" is not an allowed value for divison')
        return v
    @field_validator("location_type")
    def reject_na_location_type(cls,v):
        not_allowed = {"NA"}
        if v in not_allowed:
            raise ValueError(f'"{v}" is not an allowed value for location_type')
        return v
    @field_validator("primary_offence")
    def reject_na_primary_offence(cls,v):
        not_allowed = {"NA", "This should be removed"}
        if v in not_allowed:
            raise ValueError(f'"{v}" is not an allowed value for primary_offence')
        return v
    @field_validator("neighbourhood")
    def reject_na_neighbourhood(cls,v):
        not_allowed = {"NSA"}
        if v in not_allowed:
            raise ValueError(f'"{v}" is not an allowed value for neighbourhood')
        return v
    

import polars as pl

df = pl.read_csv("cleaned_hate_crimes.csv")

# Convert Polars DataFrame to a list of dictionaries for validation
data_dicts = df.to_dicts()

# Validate the dataset in batches
validated_data = []
errors = []

# Batch validation
for i, row in enumerate(data_dicts):
    try:
        validated_row = HateCrimes(**row)  # Validate each row
        validated_data.append(validated_row)
    except ValidationError as e:
        errors.append((i, e))

# Convert validated data back to a Polars DataFrame
validated_df = pl.DataFrame([row.dict() for row in validated_data])

# Display results
print("Validated Rows:")
print(validated_df)

if errors:
    print("\nErrors:")
    for i, error in errors:
        print(f"Row {i}: {error}")