"""
This content is based on our course assignment
Full Name: Ujjawal Poudel
Student ID: ******
Faculty: ******
"""

# * Install Python Packages
import pandas as pd

# * Read the CSV file
df = pd.read_csv(
    "COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries.csv"
)

# * Print the first five rows
print(df.head())

# * Check total number of NAN values in dataframe
print("Check how many NAN value is in our dataset", df.isnull().sum().sum())

# * For assignment 2
# * We need to find the maximum, minimum, and mode of critical_staffing_shortage_today_no

# * Maximum Value of critical_staffing_shortage_today_no
max_val = df["critical_staffing_shortage_today_no"].max()

# * Minimum Value of critical_staffing_shortage_today_no
min_val = df["critical_staffing_shortage_today_no"].min()

# * Mode of critical_staffing_shortage_today_no
# * dropna=true; After applying this, while calculation NAN/NaT value is not consider
mode_val = df["critical_staffing_shortage_today_no"].mode(dropna=True)[0]


# * To cross check the mode value, I calculate counts of unique values of particular series
# print(df["critical_staffing_shortage_today_no"].value_counts())


# * Print the maximum, minimum, and mode of critical_staffing_shortage_today_no
print(f"The maximum value for critical_staffing_shortage_today_no is: {max_val}")
print(f"The minimum value for critical_staffing_shortage_today_no is: {min_val}")
print(f"The mode value for critical_staffing_shortage_today_no is: {mode_val}")
