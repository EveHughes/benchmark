#### Preamble ####
# Purpose: Simulates sample data for delay in TTC streetcars
# Author: Aakash Vaithyanathan (translated by ChatGPT)
# Date: September 24, 2024
# Contact: aakash.vaithyanathan@mail.utoronto.ca
# License: MIT
# Pre-requisites: pandas, numpy
# Any other information needed? None

#### Workspace setup ####
import pandas as pd
import numpy as np
import random
from pathlib import Path

random.seed(20136)
np.random.seed(20136)

#### Simulate data ####
num_rows = 100

data = pd.DataFrame({
    "year": 2023,
    "month": np.random.randint(1, 13, size=num_rows),
    "hour": np.random.randint(0, 24, size=num_rows),
    "delay_mins": np.random.randint(1, 121, size=num_rows),
    "streetcar_line": random.choices([504, 505, 506, 511, 304, 305, 311, 9000], k=num_rows),
    "reason": random.choices(["Traffic", "Emergency", "Weather", "Route Change"], k=num_rows)
})

#### Write CSV ####
output_path = Path("data/simulated_data")
output_path.mkdir(parents=True, exist_ok=True)
data.to_csv(output_path / "simulated_streetcar_delay.csv", index=False)