# Data Cleaning & Standardization Project

## Project Objective

This project is a practical demonstration of the data cleaning, preparation, and automation skills required for a data-focused role. The goal was to take a raw, messy dataset sourced from the web, and transform it into a clean, well-structured, and analysis-ready format using both manual inspection and an automated Python script.

## Project Methodology

This project was approached in two distinct phases to showcase a full-circle understanding of a data cleaning task:

1.  **Manual Analysis & Cleaning (in Excel):** The initial dataset was first loaded into Excel to perform a hands-on inspection. This foundational step allowed for the identification of various data quality issues, from simple formatting problems to subtle, "invisible" character encoding errors. A detailed **"Summary"** was created to document every identified issue and the proposed solution.

2.  **Automated Cleaning (with Python):** The steps and rules defined in the manual log were then translated into a robust, repeatable Python script using the **pandas** library. This script programmatically performs all the cleaning steps, taking the raw CSV as input and producing a perfectly clean Excel file as output.

## Files in this Repository

*   `dirty data.csv`: The original, unprocessed dataset with numerous data quality issues.
*   `manual cleaning.xlsx`: An Excel workbook containing:
    *   The original raw data.
    *   A detailed **"Summary"** tab that documents all identified issues and the actions required to fix them.
*   `python_cleaning.py`: The final, well-commented Python script that automates the entire cleaning workflow.
*   `python_cleaned.xlsx`: The final, analysis-ready dataset produced by the Python script.

## Summary of Cleaning Steps Performed

The Python script automates the following cleaning actions:

*   **Column Name Standardization:**
    *   Corrected invisible non-breaking spaces (`\xa0`) in column headers.
    *   Removed leading/trailing whitespace.
    *   Updated column names for clarity (e.g., `(in 2022 dollars)` to `(in 2024 dollars)`).

*   **Data Type Correction:**
    *   Stripped non-numeric characters (e.g., `$`, `,`) from financial columns.
    *   Converted numeric-like columns to their proper `int64` data type.

*   **Text & String Cleaning:**
    *   Used regular expressions to remove unwanted patterns and symbols (e.g., `[...]`, `†`, `*`) from text fields.
    *   Normalized whitespace to ensure all text was clean and consistent.

*   **Structural Cleaning:**
    *   Removed irrelevant columns (`Peak`, `All Time Peak`, `Ref.`) that contained significant missing data.

## Key Skills Demonstrated

This project showcases the following skills:

*   **Detail-Oriented & Thorough:** Identified and corrected subtle data issues like non-breaking spaces, en dashes, and mixed data types that are often missed.
*   **Spreadsheet Competence (Excel):** Used Excel for initial data inspection and to create a structured summary and action log.
*   **Python for Automation (Pandas):** Developed a complete, well-commented Python script using the pandas library to create a robust and repeatable cleaning workflow.
*   **Data Operations & Regular Expressions:** Handled data type conversions, complex string manipulation, and pattern matching using regex.
*   **Problem-Solving & Action-Oriented Mindset:** Independently managed an end-to-end project from a raw file to a clean, usable dataset.

## How to Run the Project

1.  Ensure you have Python and the pandas library installed (`pip install pandas`).
2.  Place the `data_cleaner.py` script and the `raw_data.csv` file in the same directory.
3.  Run the Python script from your terminal: `python data_cleaner.py`
4.  The script will generate the `cleaned_output.xlsx` file in the same directory.
