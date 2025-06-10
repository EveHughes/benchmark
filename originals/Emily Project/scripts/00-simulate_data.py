#### Preamble ####
# Purpose: Simulates a dataset of the data quality of datasets on Open Data Toronto
# Author: Emily Su
# Date: 13 May 2025
# Contact: em.su@mail.utoronto.ca
# License: MIT
# Pre-requisites: 
  # - `polars` must be installed (pip install polars)
  # - `numpy` must be installed (pip install numpy)


#### Workspace setup ####
import polars as pl
import numpy as np
np.random.seed(646)


#### Simulate data ####
# Grade
grade = [
  "Bronze", "Silver", "Gold"
]

# Generate the data using numpy and polars
accessibility = np.random.randint(low=0, high=1, size=151, dtype=int)
completeness = np.random.random()
freshness = np.random.random()
metadata = np.random.random()
usability = np.random.random()
grade = np.random.choice(grade, size=151, replace=True, p=[0.5, 0.25, 0.25])


# Create a polars DataFrame
analysis_data = pl.DataFrame({
    "accessibility": accessibility,
    "completeness": completeness,
    "freshness": freshness,
    "metadata": metadata,
    "usability": usability,
    "grade": grade
})

#### Save data ####
analysis_data.write_csv("data/00-simulated_data/simulated_data.csv")
