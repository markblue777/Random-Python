import os
import pandas as pd

def merge_csv_files(input_folder, output_file):
    # Get a list of all CSV files in the input folder
    csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

    # Check if there are any CSV files in the folder
    if not csv_files:
        print("No CSV files found in the specified folder.")
        return

    # Initialize an empty DataFrame to store the merged data
    merged_data = pd.DataFrame()

    # Loop through each CSV file and append its data to the merged DataFrame
    for csv_file in csv_files:
        file_path = os.path.join(input_folder, csv_file)
        df = pd.read_csv(file_path)
        merged_data = merged_data.append(df, ignore_index=True)

    # Write the merged data to a new CSV file
    merged_data.to_csv(output_file, index=False)
    print(f"Merged data successfully written to {output_file}")

# Example usage
input_folder = 'C:\\folder'
output_file = 'merged_data.csv'
merge_csv_files(input_folder, output_file)