#### Preamble ####
# Purpose: Cleans the raw data from Open Data Toronto
# Author: Emily Su
# Date: 9 May 2025
# Contact: em.su@mail.utoronto.ca
# License: MIT
# Pre-requisites: Have ran 02-download_data.py and have installed the required packages mentioned in 
# Workspace setup by running requirements.txt.

#### Workspace setup ####
import polars as pl

#### Clean data ####
# Read in CSV file
the_raw_data = pl.read_csv("data/01-raw_data/raw_data.csv")

# Select specific columns
selected_columns = ["accessibility", "completeness", "freshness", "metadata", "usability", "grade"]

selected_df = the_raw_data.select(selected_columns)

# Filter to only rows that have no NONE data
filtered_df = selected_df.filter(the_raw_data["accessibility"].is_not_null() & 
                                 the_raw_data["completeness"].is_not_null() & 
                                 the_raw_data["freshness"].is_not_null() & 
                                 the_raw_data["metadata"].is_not_null() & 
                                 the_raw_data["usability"].is_not_null() & 
                                 the_raw_data["grade"].is_not_null())

#### Save data ####
filtered_df.write_csv("data/02-analysis_data/analysis_data.csv")