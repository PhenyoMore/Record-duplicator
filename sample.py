import pandas as pd
import numpy as np

# Use a raw string for the file path or replace backslashes with double backslashes
df = pd.read_excel(r"C:\xampp\htdocs\Newcastle_MDUs_AeX_template.xlsx")

# Initialize an empty DataFrame to store the result
df_result = pd.DataFrame()

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Fetch the number in 'mdu_unit' and handle NaN values
    mdu_unit_value = int(row['mdu_unit']) if not np.isnan(row['mdu_unit']) else 1

    # Duplicate the entire row based on the fetched number
    df_duplicates = pd.concat([row.to_frame().T] * mdu_unit_value, ignore_index=True)

    # Append the duplicates to the result DataFrame
    df_result = pd.concat([df_result, df_duplicates], ignore_index=True)

# Save the result to a new Excel file
df_result.to_excel('p3.xlsx', index=False)

print("Duplicates created successfully.")
