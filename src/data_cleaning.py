"""
        Purpose : cleans data/raw/sales_data_raw.csv by 
                  removing invalid rows with negative values, 
                  trimming whitespace and column names, and 
                  handling missing values.
"""
import pandas as pd

# method to read in sales_data_raw.csv from data/raw/.
# Why : doing it to "clean" the .csv.
def load_data(file_path:str):
        ...

# method to make the column names lowercased and underscores in the .csv.
# Why : To make the column names have the same style and look professional.
def clean_column_names(df):
        ...

# method to deal with empty cells in the csv
# Why : we either remove the cell or fill it in with an empty value. For proper data collection.
def handle_missing_values(df):
        ...

# method to remove invalid rows in the csv.
# Why : invalid rows spoil the data. rows that have negative quantity or price.
def remove_invalid_rows(df):
        ...



if __name__ == "__main__":
        raw_path = "data/raw/sales_data_raw.csv"
        cleaned_path = "data/processed/sales_data_clean.csv"

        df_raw = load_data(raw_path)
        df_clean = clean_column_names(df_raw)
        df_clean = handle_missing_values(df_clean)
        df_clean = remove_invalid_rows(df_clean)
        df_clean.to_csv(cleaned_path, index=False)
        print("Cleaning complete. First few rows:")
        print(df_clean.head())
