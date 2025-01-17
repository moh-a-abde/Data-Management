# -*- coding: utf-8 -*-
"""label_Dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DDSHUpF6v7xoWR3kR18OvcqhmsVYezy_
"""

import pandas as pd

# Load the CSV file
file_path = '/content/zeek_live_data_6172024a-2.csv'  # Adjust the path as necessary
data = pd.read_csv(file_path)

# Define the port-label mapping
port_label_mapping = {
    53: 'DNS',
    22: 'SSH',
    80: 'HTTP',
    443: 'HTTPS',
    21: 'FTP'
}

# Create a new 'label' column and initialize with None
data['label'] = None

# Function to map port to label
def get_label(port):
    return port_label_mapping.get(port, None)

# Apply the mapping to the 'id.resp_p' column
data['label'] = data['id.resp_p'].apply(lambda x: get_label(int(x)) if not pd.isna(x) else None)

# Save the updated DataFrame to a new CSV file
output_file_path = 'zeek_live_data_labeled.csv'  # Adjust the path as necessary
data.to_csv(output_file_path, index=False)

print(f"Labeled data saved to {output_file_path}")

# Print the first few rows of the labeled data
print(data.head())