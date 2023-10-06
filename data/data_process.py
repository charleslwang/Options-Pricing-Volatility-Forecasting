import pandas as pd
import os


# loading raw data

raw_data_file = os.path.join("data", "raw_data", "stock_data.csv")

raw_data = pd.read_csv(raw_data_file)

# cleaning data

missing_values = raw_data.isnull().sum()
print("Missing values:\n", missing_values)

raw_data.dropna(inplace=True)

duplicate_rows = raw_data.duplicated()
print("Duplicate Rows:\n", raw_data[duplicate_rows])

raw_data.drop_duplicates(inplace=True)

# transform data

raw_data['Date'] = pd.to_datetime(raw_data['Date'])
raw_data.sort_values(by='Date', inplace=True)
raw_data.reset_index(drop=True, inplace=True)

# save data

cleaned_data_file = os.path.join("data", "clean_data.csv")
raw_data.to_csv(cleaned_data_file, index=False)

print("Cleaned data saved to ", cleaned_data_file)
