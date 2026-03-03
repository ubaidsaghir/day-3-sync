# Challenge 1: The "Manual to Vectorized" Shift
# Goal: Prove they can stop using for loops.

# Task: Provide the intern with this dictionary and ask them to:

# Convert it to a DataFrame.

# Create a new column Total_Cost by multiplying Price and Quantity.

# Constraint: They are forbidden from using for, while, or iterrows().

import pandas as pd

data = {
    'Item': ['Widget A', 'Widget B', 'Widget C'],
    'Price': [25.50, 40.00, 15.75],
    'Quantity': [10, 5, 20]
}

df = pd.DataFrame(data)

df["Total_Cost"] = df["Price"] * df["Quantity"]

grand_total = df["Total_Cost"].sum()
print("Final DataFrame:")
print(df)

print("Grand Total of All Items:", grand_total)
