# Import Python Package
import pandas as pd

# Load DataFrames
df = pd.read_csv("mimic-iii-sample.csv")


# Information of dataframe
print(df.info())


# If you have a column that has only on unique values -> drop the column
# 1 get the list of all columns
column_name_list = df.columns

# 2 to go over each column and check if the unique value is one
for col in column_name_list:
    number_of_unique_values = len(df[col].unique())
    if number_of_unique_values == 1:
        # 3 Drop the column
        df = df.drop(columns=[col])

# If you have a column that has missing values greater than a threshold (70 - 80% ) -> drop the column
# 1 Find the number of missing values per each column
df_missing_values = (df.isnull().sum() / len(df)) * 100
print(df_missing_values)
