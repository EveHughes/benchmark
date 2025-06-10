import unittest
import pandas as pd
import numpy as np

class TestCleanedTTCStreetcarDelayData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = pd.read_csv("data/analysis_data/cleaned_ttc_streetcar_delay_2023.csv")

    def test_no_missing_values(self):
        self.assertFalse(self.data.isna().any().any(), "Dataset contains missing values")

    def test_column_types(self):
        self.assertTrue(self.data['season'].dtype == 'object', "Column 'season' should be of type object (string)")
        self.assertTrue(np.issubdtype(self.data['line'].dtype, np.number), "Column 'line' should be numeric")
        self.assertTrue(np.issubdtype(self.data['min_delay'].dtype, np.number), "Column 'min_delay' should be numeric")
        self.assertTrue(np.issubdtype(self.data['year'].dtype, np.number), "Column 'year' should be numeric")
        self.assertTrue(np.issubdtype(self.data['month'].dtype, np.number), "Column 'month' should be numeric")
        self.assertTrue(np.issubdtype(self.data['hour'].dtype, np.number), "Column 'hour' should be numeric")
        self.assertTrue(self.data['incident'].dtype == 'object', "Column 'incident' should be of type object (string)")

    def test_month_range(self):
        self.assertTrue(self.data['month'].between(1, 12).all(), "All months must be between 1 and 12")

    def test_year_is_2023(self):
        self.assertTrue((self.data['year'] == 2023).all(), "All year values must be 2023")

    def test_hour_range(self):
        self.assertTrue(self.data['hour'].between(0, 23).all(), "All hour values must be between 0 and 23")

    def test_min_delay_non_negative(self):
        self.assertTrue((self.data['min_delay'] >= 0).all(), "All delays must be non-negative")

    def test_min_delay_max(self):
        self.assertTrue((self.data['min_delay'] <= 120).all(), "All delays must be less than or equal to 120 minutes")

    def test_valid_seasons(self):
        valid_seasons = {"Winter", "Spring", "Summer", "Fall"}
        self.assertTrue(self.data['season'].isin(valid_seasons).all(), "Invalid season values detected")

    def test_non_empty_incident(self):
        self.assertTrue((self.data['incident'].str.len() > 0).all(), "All incident descriptions must be non-empty")


if __name__ == "__main__":
    unittest.main()