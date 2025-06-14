#### Preamble ####
# Purpose: Tests Cleaned Disease Count Data & Yearly Disease Count Data
# Author: Evelyn Hughes
# Date: 13 May 2025
# Contact: evelyn.hughes@mail.utoronto.ca
# License: MIT
# Pre-requisites: 
  # - `polars` must be installed (pip install polars)
  # - 'unittest' must be installed
  # -  02-download_data.py must have been run
  # -  03-clean_data.py must have been run


#### Workspace setup ####
import polars as pl
import unittest

class TestAll(unittest.TestCase):
  def setUp(self):
    self.disease_count = pl.read_csv("data/02-analysis_data/disease_count.csv")
    self.yearly_disease_count = pl.read_csv("data/02-analysis_data/yearly_disease_count.csv")

  def test_diseaseCount(self):

    #### Test disease_count data ####

    #Test counts add to total
    for row in self.disease_count.rows(named = True):
      self.assertEquals(row["Coronavirus"] + row["Other"] + row["Unknown"], row["Total Agents"])

  def test_yearlyCount(self):
      #### Test yearly_disease_count data ####
      # Test that the dataset has 10 rows - one for each year between 2016-2025 inclusive
      self.assertEquals (self.yearly_disease_count.shape[0], 6)

      # Test that the dataset has 6 columns
      self.assertEquals(self.yearly_disease_count.shape[1], 9)

if __name__ == "__main__":
  unittest.main()