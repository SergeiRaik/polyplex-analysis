import os
import pandas as pd

# Function to convert Excel files to CSV
def convert_excel_to_csv(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Loop through all files
    for file in files:
        # Check if the file is an Excel file
        if file.endswith('.xlsx') or file.endswith('.xls'):
            # Create full file path
            file_path = os.path.join(folder_path, file)
            
            # Read the Excel file
            excel_data = pd.read_excel(file_path)
            
            # Remove the file extension and add '.csv' to create the new file name
            csv_file = os.path.splitext(file)[0] + '.csv'
            
            # Create full path for the new CSV file
            csv_file_path = os.path.join(folder_path, csv_file)
            
            # Save the data to a CSV file
            excel_data.to_csv(csv_file_path, index=False)
            
            print(f'Converted {file} to {csv_file}')

# Specify the folder path
folder_path = 'positions/2p5_HA_Mar6'

# Convert all Excel files in the specified folder to CSV
convert_excel_to_csv(folder_path)