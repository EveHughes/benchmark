# Annual Analysis of Delays in TTC Streetcars for the year 2023

## Overview

This project aims to study the causes of delays in Toronto Transit Commissions (TTC) streetcar service, the variation in delays by the hours in working shifts and whether there are any seasonal relationships to the observed delays for the year 2023. The findings from the paper can help in better designing policies to improve the commuting experience for the residents of Toronto.

## File Structure

The repo is structured as follows:

- `data` contains all the data necessary provided by OpenData Toronto.
  - `data/raw_data` contains the raw data taken from OpenData Toronto. A link to the dataset can be found [here](https://open.toronto.ca/dataset/ttc-streetcar-delay-data/)
  - `data/analysis_data` contains the cleaned dataset that is used for analysis purposes.
  - `data/simulated_data` contains a sample simulated dataset for exploring the delays in TTC Streetcars.
- `other` contains relevant sketches and LLM usage documentation.
  - `other/llm` contains a usage.txt file outlining the prompts used by ChatGPT to assist in the programming aspect of the project.
  - `other/sketches` contains a _dataset.png_ and _graphs.png_ outlining how we expect our dataset and graphs to look in this project.
- `paper` contains the files used to generate the paper.
  - `paper/paper.qmd` contains a Quarto document used to write up the report and include R components to generate graphs.
  - `paper/paper.pdf` contains the compiled pdf document as per the Quarto document content.
  - `paper/references.bib` contains a bibliography document outlining all the relevant literature and R package references used in this project.
- `scripts` contains the R scripts used in this project.
  - `scripts/00-simulate_data.R` contains the R script used to simulate how our dataset could look like before downloading it from OpenData Toronto.
  - `scripts/01-download_data.R` contains the R script used to download the dataset from OpenData Toronto and save a CSV version of it.
  - `scripts/02-data_cleaning.R` contains the R script used to perform various data cleaning methods to create the final CSV data used for analysis.
  - `scripts/03-test_data.R` contains the R script used to test our simulated data generated.


## How to run this project?

Please open the __ttc_streetcar_delay.Rproj__ file to run the project. It is recommended you have R and RStudio v4.4 installed on your machine. To compile the Quarto document, simply navigate to the document and click __Render__.


## Statement on LLM usage

Aspects of the code were written with the help of ChatGPT 3.5 and ChatGPT-4o daily free limit. The entire chat history with the LLM is available in other/llm/usage.txt.
