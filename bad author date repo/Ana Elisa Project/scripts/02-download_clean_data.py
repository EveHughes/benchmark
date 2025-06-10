#### Preamble ####
# Purpose: Downloads and saves the data from Toronto Open Data
# Author: Ana Elisa Lopez-Miranda
# Date: 22 May 2025
# Contact: a.lopez.miranda@mail.utoronto.ca
# License: MIT



#### Download data ####
import polars as pl

# URL of the CSV file
url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/hate-crimes-open-data/resource/5e89f848-1573-4306-b011-de35e18b50d8/download/Hate%20Crimes%20Open%20Data.csv"

# Read the CSV file into a Polars DataFrame
df = pl.read_csv(url)

# Save the raw data
df.write_csv("hate_crimes.csv")

import polars as pl

df = pl.read_csv("hate_crimes.csv")

# Select specific columns
selected_columns = ["OCCURRENCE_DATE", "OCCURRENCE_TIME", "REPORTED_DATE", "DIVISION", "LOCATION_TYPE", "AGE_BIAS", "MENTAL_OR_PHYSICAL_DISABILITY", "RACE_BIAS", "ETHNICITY_BIAS", "LANGUAGE_BIAS", "RELIGION_BIAS", "SEXUAL_ORIENTATION_BIAS", "GENDER_BIAS", "MULTIPLE_BIAS", "PRIMARY_OFFENCE", "NEIGHBOURHOOD_158", "ARREST_MADE"]


selected_df = df.select(selected_columns)

# Filter to only rows that have data
filtered_df = selected_df.filter(df["OCCURRENCE_DATE"].is_not_null())

print(filtered_df.head())


renamed_df = filtered_df.rename({"OCCURRENCE_DATE": "occurrence_date",
                                 "OCCURRENCE_TIME": "time",
                                 "REPORTED_DATE": "reported_date",
                                 "DIVISION": "division",
                                 "LOCATION_TYPE": "location_type",
                                 "AGE_BIAS": "age",
                                 "MENTAL_OR_PHYSICAL_DISABILITY": "mental or physical disability",
                                 "RACE_BIAS": "race",
                                 "ETHNICITY_BIAS": "ethnicity",
                                 "LANGUAGE_BIAS": "language",
                                 "RELIGION_BIAS": "religion",
                                 "SEXUAL_ORIENTATION_BIAS": "sexual orientation",
                                 "GENDER_BIAS": "gender",
                                 "MULTIPLE_BIAS": "multiple",
                                 "PRIMARY_OFFENCE": "primary_offence",
                                 "NEIGHBOURHOOD_158": "neighbourhood",
                                 "ARREST_MADE": "arrest"
                                 })
clean = renamed_df.filter(
    (renamed_df["location_type"] != "NA") &
    (renamed_df["neighbourhood"] != "NSA") &
    (renamed_df["primary_offence"] != "NA") &
    (renamed_df["primary_offence"] != "This should be removed")
)

print(renamed_df.head())

clean.write_csv("cleaned_hate_crimes.csv")


