import pandas as pd
import numpy as np
import random
from datetime import timedelta, datetime

# Define the time range
start_date = datetime(2016, 1, 1)
end_date = datetime(2023, 12, 31)

# Generate a sequential date range
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# Define product and category lists
products = ['Laptop', 'Smartphone', 'Tablet', 'Smartwatch', 'Camera', 'Headphones', 'Keyboard', 'Monitor', 'Router', 'Drone']
categories = ['Computers', 'Mobile Devices', 'Accessories', 'Networking', 'Audio & Video']

# Randomly generate data
data = {
    'Date': date_range[:1000],  # Randomly choose dates
    'Product': np.random.choice(products, size=1000),
    'Category': np.random.choice(categories, size=1000),
    'Price': np.random.randint(20, 1001, size=1000),  # Random price between 20 and 1000 USD
    'Quantity': np.random.randint(1, 51, size=1000),  # Random quantity between 1 and 50
    'Rating': np.round(np.random.uniform(1, 5, size=1000), 1),  # Random rating between 1.0 and 5.0
    'Revenue': np.random.randint(2000, 10000, size=1000)  # Random revenue between 10000 and 30000
}

# Create the DataFrame
df = pd.DataFrame(data)

# Define the file path
file_path = "data/sales_data_2016_2023.csv"

# Save the DataFrame to a CSV file
df.to_csv(file_path, index=False)

# Provide the file path for download
print(file_path)
