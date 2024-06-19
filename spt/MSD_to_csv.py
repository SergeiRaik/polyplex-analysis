import pandas as pd
import os

def convert_excel_to_csv(folder_path):
    # Iterate over all files in the provided folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".xlsx") or filename.endswith(".xls"):
            # Construct the full file path
            file_path = os.path.join(folder_path, filename)
            
            # Read the Excel file
            df = pd.read_excel(file_path, usecols="A:C", skiprows=10, nrows=301)
            
            # Save to CSV with the same name
            csv_filename = os.path.splitext(filename)[0] + '.csv'
            csv_path = os.path.join(folder_path, csv_filename)
            df.to_csv(csv_path, index=False)
            print(f"Converted {filename} to {csv_filename}")

folder_path = 'positions/2p5_Mar22'
convert_excel_to_csv(folder_path)