# Challenge 2: The Titanic Data Audit
# Goal: Practical data cleaning and filtering.

# Task: Ask the intern to download the Titanic CSV and write a script that outputs a "Report" containing:

# The count of missing values in every column.

# A new DataFrame called young_passengers containing only people aged 18 or younger.

# The average Fare paid by people in young_passengers.

# Replace all missing values in the Embarked column with the string "Unknown".

import pandas as pd 

df = pd.read_csv("Titanic-Dataset.csv")

print("Missing Values Per Column:\n")
missing_values = df.isnull().sum()   
print(missing_values)

young_passengers = df[df["Age"] <= 18]

print("\nTotal Young Passengers:")
print(len(young_passengers))

average_fare_young = young_passengers["Fare"].mean()
print("\nAverage Fare Paid by Young Passengers:")
print(round(average_fare_young, 2))

df["Embarked"] = df["Embarked"].fillna("Unknown")

print("\nMissing values in Embarked after replacement:")
print(df["Embarked"].isnull().sum())