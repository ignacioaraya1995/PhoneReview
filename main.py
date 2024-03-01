import os
import pandas as pd
from prettytable import PrettyTable

def client_file_analysis():
    folder_path = 'data'
    data_frames = []

    for file in os.listdir(folder_path):
        if file.endswith('.xlsx'):
            file_path = os.path.join(folder_path, file)
            df = pd.read_excel(file_path)
            data_frames.append(df)

    combined_df = pd.concat(data_frames, ignore_index=True)
    phone_columns = [col for col in combined_df.columns if col.startswith('PHONE NUMBER')]
    phone_numbers = combined_df[phone_columns].values.flatten()

    # Attempt to convert phone numbers into integers, ignoring errors
    cleaned_phone_numbers = pd.Series(phone_numbers).apply(lambda x: pd.to_numeric(x, errors='coerce')).dropna()

    counts = cleaned_phone_numbers.value_counts()

    # Creating a pretty table
    table = PrettyTable()
    table.field_names = ["Phone Number", "Count"]
    table.title = "Top 25 Most Repeated Phone Numbers"

    for phone, count in counts.head(25).items():
        table.add_row([int(phone), "{:,}".format(count)])

    print(table)

    # Alert for excessive repetitions
    if any(counts > 50):
        print("\nALERT: There are phone numbers repeated more than 50 times!")

    print("\nNote: Phone numbers should ideally be unique or repeated no more than 3 or 4 times to ensure data integrity and privacy.")

# Call the function to perform analysis
client_file_analysis()
