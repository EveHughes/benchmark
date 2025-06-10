import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(20136)

# Clean data
raw_data = pd.read_csv("data/raw_data/unedited_ttc_streetcar_delay_2023.csv")

cleaned_data = (
    raw_data
    .rename(columns=lambda x: x.strip().lower().replace(" ", "_"))  # Clean column names
)

# Split 'date' and 'time' columns
cleaned_data['date'] = pd.to_datetime(cleaned_data['date'], errors='coerce')
cleaned_data['year'] = cleaned_data['date'].dt.year
cleaned_data['month'] = cleaned_data['date'].dt.month

cleaned_data['hour'] = cleaned_data['time'].str.split(':').str[0]

# Map months to seasons
season_map = {
    '03': 'Spring', '04': 'Spring', '05': 'Spring',
    '06': 'Summer', '07': 'Summer', '08': 'Summer',
    '09': 'Fall', '10': 'Fall', '11': 'Fall',
    '12': 'Winter', '01': 'Winter', '02': 'Winter'
}
cleaned_data['season'] = cleaned_data['month'].map(season_map)

# Drop missing values and filter
cleaned_data = cleaned_data.dropna()
cleaned_data = cleaned_data[cleaned_data['min_delay'] != 0]
cleaned_data = cleaned_data[['year', 'month', 'hour', 'incident', 'min_delay', 'line', 'season']]

# Convert columns to numeric
cleaned_data['hour'] = pd.to_numeric(cleaned_data['hour'])
cleaned_data['month'] = pd.to_numeric(cleaned_data['month'])
cleaned_data['year'] = pd.to_numeric(cleaned_data['year'])
cleaned_data['min_delay'] = pd.to_numeric(cleaned_data['min_delay'])
cleaned_data['line'] = pd.to_numeric(cleaned_data['line'])

# Filter for delays less than 121 minutes
cleaned_data = cleaned_data[cleaned_data['min_delay'] < 121]

# Save data
cleaned_data.to_csv("data/analysis_data/cleaned_ttc_streetcar_delay_2023.csv", index=False)