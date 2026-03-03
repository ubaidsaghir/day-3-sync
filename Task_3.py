# Challenge 3: The "Difficult" One – String & Data Cleaning
# Goal: Handling real-world "dirty" data in Pandas.

# The Setup: Give them this messy DataFrame:
    

# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     'Date': ['2023-01-01', '2023-01-02', 'Missing', '2023-01-04'],
#     'Revenue': ['$1,200', '$2,500', 'ERROR', '$1,800'],
#     'Active_Users': [150, np.nan, 200, 175]
# })    


# The Mission: Write a script to "sanitize" this data:

# The Date Trap: Convert the Date column to datetime objects. (They will need to handle the "Missing" string—hint: errors='coerce').

# The Currency Trap: Convert Revenue into a clean float. They must remove the $ and the , and handle the "ERROR" string.

# The Null Trap: Fill the missing Active_Users with the mean value of that column.

# The Final Output: Print df.info() and the final cleaned DataFrame.



import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-02', 'Missing', '2023-01-04'],
    'Revenue': ['$1,200', '$2,500', 'ERROR', '$1,800'],
    'Active_Users': [150, np.nan, 200, 175]
})

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")    

df["Revenue"] = df["Revenue"].str.replace("$","",regex=False)
df["Revenue"] = df["Revenue"].str.replace(",","",regex=False)

df["Revenue"] = pd.to_numeric(df["Revenue"], errors="coerce")

mean_users = df["Active_Users"].mean()
df["Active_Users"] = df["Active_Users"].fillna(mean_users)

print(df.info())
print("Cleaned DataFrame:\n")
print(df)