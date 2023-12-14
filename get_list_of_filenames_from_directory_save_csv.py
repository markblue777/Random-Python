import os
import csv

def save_filenames_to_csv(directory_path, output_csv):
    with open(output_csv, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Filename'])  # Write a header row if needed
        for filename in os.listdir(directory_path):
            csv_writer.writerow([filename])

# Replace 'directory_path' with the path of the directory you want to scan
directory_path = 'C:\\Folder'

# Replace 'output.csv' with the desired name of the output CSV file
output_csv = 'output.csv'

save_filenames_to_csv(directory_path, output_csv)