import os
import pandas as pd
from sqlalchemy import create_engine

folder_path = r'C:\Users\maste\Desktop\Raw Data 2022\Harvest 2022 new set data'

all_data = []

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        df = pd.read_csv(os.path.join(folder_path, filename))

        df.rename(columns={'utc_time': 'universal_time', ' GPS_TOW': 'GPS_TOW'}, inplace=True)

        df.insert(0, 'field_id', 101)

        date_from_file = filename.split('.')[0]  # Assuming the date is the file name without extension
        df.insert(1, 'date', date_from_file)

        cart_id = filename.replace('Cart', '').replace('.csv', '')
        df.insert(2, 'cart_id', cart_id)

        # Append the DataFrame to the list
        all_data.append(df)

# Combine all DataFrames into a single DataFrame
combined_df = pd.concat(all_data, ignore_index=True)

# MySQL connection details
db_endpoint = 'yielddatabase.coz72rpcgefb.us-east-1.rds.amazonaws.com'
db_username = 'admin'
db_password = 'stavros1332'
db_name = 'harvest'

# Create a connection to the database
connection_string = f"mysql+mysqlconnector://{db_username}:{db_password}@{db_endpoint}/{db_name}"
engine = create_engine(connection_string)

combined_df.to_sql('raw_data', engine, if_exists='replace', index=False)
