#### Preamble ####
# Purpose: Tests the cleaned dataset from Open Data Toronto 
# Author: Emily Su
# Date: 9 May 2025
# Contact: em.su@mail.utoronto.ca
# License: MIT
# Pre-requisites: Have ran 02-download_data.py and 03-clean_data.py and have installed the required packages mentioned in 
# Workspace setup by running requirements.txt.


#### Workspace setup ####
import polars as pl
import pointblank as pb

# Reference https://posit.co/blog/introducing-pointblank-for-python/
# Read in CSV file
cleaned_data = pl.read_csv("data/02-analysis_data/analysis_data.csv")

#### Test data ####
# Check columns type
schema = pb.Schema(
    columns=[
        ("accessibility", "Int64"),
        ("completeness", "Float64"),
        ("freshness", "Float64"),
        ("metadata", "Float64"),
        ("usability", "Float64"),
        ("grade", "String"),
    ]
)

# None of the columns in string type columns are ""
check_for_empty_strings_test = (
    pb.Validate(
        data=cleaned_data,
        tbl_name="cleaned_data",
        label="Check for empty strings test"
    )
    .col_vals_regex(
        columns=["grade"],# check that all string columns are non-empty strings
        pattern=r"(.|\s)*\S(.|\s)*" # Referenced: https://posit-dev.github.io/pointblank/demos/column-selector-functions/index.html
    )
    .interrogate()
)

# Check if grade's value is only grade is Bronze, Silver, and Gold 
check_grade_value_test = (
    pb.Validate(
        data=cleaned_data,
        tbl_name="cleaned_data",
        label="Check Grade Value Test"
    )
    .col_vals_in_set(columns="grade", set=["Bronze", "Silver", "Gold"])
    .interrogate()
)

# RUN TESTS 
check_for_empty_strings_test.get_tabular_report().show("browser")
check_grade_value_test.get_tabular_report().show("browser")