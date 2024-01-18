


import pandas as pd

# Use a raw string for the file path
df = pd.read_excel("C:\\xampp\\htdocs\\Welkom_premise data.xlsx")

# Find the maximum value in the 'mdu_block' column
max_value = df['mdu_block'].max()

# Check if max_value is not null
if pd.notna(max_value):
    # Assuming 'mdu_block' is the column you want to check for null/empty values
    df_filtered = df[pd.notnull(df['mdu_block'])]

    # Create duplicate records only for rows with 'mdu_block' values
    df_duplicates = pd.concat([df_filtered] * int(max_value), ignore_index=True)

    # Append rows with null 'mdu_block' values to the duplicates
    df_null_values = df[pd.isnull(df['mdu_block'])]
    df_result = pd.concat([df_duplicates, df_null_values], ignore_index=True)

    # Save the result to a new Excel file
    df_result.to_excel('duplicates_only_win.xlsx', index=False)
else:
    print("No valid number extracted from 'mdu_block' column.")

import pandas as pd

# Use a raw string for the file path
df = pd.read_excel("C:\\xampp\\htdocs\\Welkom_premise data.xlsx")

# Find the unique values in the 'mdu_block' column
unique_values = df['mdu_block'].unique()

# Check if there are any unique values
if len(unique_values) > 0:
    # Initialize an empty DataFrame to store the result
    df_result = pd.DataFrame()

    # Loop through unique values in 'mdu_block' column
    for mdu_block_value in unique_values:
        # Filter rows for the current 'mdu_block' value
        df_filtered = df[df['mdu_block'] == mdu_block_value]

        # Duplicate records for the current 'mdu_block' value
        df_duplicates = pd.concat([df_filtered] * len(df_filtered), ignore_index=True)

        # Append the duplicates to the result DataFrame
        df_result = pd.concat([df_result, df_duplicates], ignore_index=True)

    # Save the result to a new Excel file
    df_result.to_excel('duplicates_only_letsGO.xlsx', index=False)

    print("Duplicates created successfully.")
else:
    print("No unique values found in 'mdu_block' column.")