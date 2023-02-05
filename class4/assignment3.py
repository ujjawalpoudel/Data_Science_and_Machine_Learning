"""
This content is based on our course assignment
Full Name: Ujjawal Poudel
Student ID: *****
Faculty: *****
"""

# Import Python Package
import pandas as pd

# read data from csv
# Only read particular columns

df = pd.read_csv(
    "COVID-19.csv",
    usecols=[
        "hospital_onset_covid_coverage",
        "critical_staffing_shortage_today_not_reported",
        "total_staffed_pediatric_icu_beds",
    ],
)


# "hospital_onset_covid_coverage"
# check minimum, maximum, mean and mode values
print(
    "mean of hospital_onset_covid_coverage", df["hospital_onset_covid_coverage"].mean()
)
print(
    "minimum of hospital_onset_covid_coverage",
    df["hospital_onset_covid_coverage"].min(),
)
print(
    "maximum of hospital_onset_covid_coverage",
    df["hospital_onset_covid_coverage"].max(),
)
print(
    "mode of hospital_onset_covid_coverage",
    df["hospital_onset_covid_coverage"].mode()[0],
)

# "critical_staffing_shortage_today_not_reported"
# check minimum, maximum, mean and mode values
print(
    "mean of critical_staffing_shortage_today_not_reported",
    df["critical_staffing_shortage_today_not_reported"].mean(),
)
print(
    "minimum of critical_staffing_shortage_today_not_reported",
    df["critical_staffing_shortage_today_not_reported"].min(),
)
print(
    "maximum of critical_staffing_shortage_today_not_reported",
    df["critical_staffing_shortage_today_not_reported"].max(),
)
print(
    "mode of critical_staffing_shortage_today_not_reported",
    df["critical_staffing_shortage_today_not_reported"].mode()[0],
)

# "total_staffed_pediatric_icu_beds"
# check minimum, maximum, mean and mode values
print(
    "mean of total_staffed_pediatric_icu_beds",
    df["total_staffed_pediatric_icu_beds"].mean(),
)
print(
    "minimum of total_staffed_pediatric_icu_beds",
    df["total_staffed_pediatric_icu_beds"].min(),
)
print(
    "maximum of total_staffed_pediatric_icu_beds",
    df["total_staffed_pediatric_icu_beds"].max(),
)
print(
    "mode of total_staffed_pediatric_icu_beds",
    df["total_staffed_pediatric_icu_beds"].mode()[0],
)
