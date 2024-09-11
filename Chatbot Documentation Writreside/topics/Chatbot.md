# Chatbot
This chatbot is designed to assist you with financial inquiries based on the data provided in the final_data.csv and final_summary.csv.

## Executing the Code
1. Ensure you have Jupyter Python libraries like Pandas installed.
2. Open and execute the "**Task 1 - Data Extraction and Analysis.ipynb**" file.
3. Press `F5` and click on "_**Python File** Debug the currently active Python file_" in the dropdown menu to start the chatbot

## Chatbot Syntax
The chatbot can understand queries in a flexible format, such as "`[Metric]` `[Company]` `[Year]`" or any variation of this order.

###### Mandatory Information:

- Metric: The financial metric you're interested in (revenue, income, assets, liabilities, cash flow).
- Company or Year: At least one of these must be specified.

###### Example queries:

Display the total income for Tesla across all available years:
```text
income tesla
```
Display the total assets for all companies in the year 2022:
```text
asset 2022
```
Display the total revenue for Microsoft in the year 2023:
```text
revenue microsoft 2023
```  