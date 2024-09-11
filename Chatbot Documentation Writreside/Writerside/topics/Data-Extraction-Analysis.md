# Data Extraction & Analysis with Jupyter
This Python code analyzes the financial performance of **Microsoft, Tesla, and Apple** using data manually extracted from the [**SEC's EDGAR database**](https://www.sec.gov/edgar/search/#).\
The data is entered into **Microsoft Excel** and exported as a CSV file.\
The analysis covers a period of **three years** (2021, 2022 & 2023, subject to data availability).

## Executing the Code
1. Ensure that the **Jupyter Notebook** Extension and the **pandas library** are installed.
2. Open and execute the "**Task 1 - Data Extraction and Analysis.ipynb**" file.
3. Click on the `Run All` button.

## What the Code Does
1. Extracts data from the `extracted_data.csv` file.
2. Year-over-Year Growth Rates:
   - Calculates the percentage change in key financial metrics (revenue, income, assets, liabilities, cash flow).
   - Rounds growth rates to two decimal places.
3. Groups data by company and calculates average growth rates for each metric over the period.
4. Exports processed data and summary statistics to CSV files.
   - The **Year-by-Year Growth Rate** data is extracted to`final_data.csv`
   - The **Average Growth Rate** data is extracted to `final_summary.csv`
