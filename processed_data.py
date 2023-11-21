import pandas as pd
import os
from sqlalchemy import create_engine

folder_path = 'C:\Users\maste\Desktop\Raw Data 2022\Yield_2022\yield data'

all_data = []
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        all_data.append(df)

combined_df = pd.concat(all_data, ignore_index=True)

# MySQL connection details
db_endpoint = 'yielddatabase.coz72rpcgefb.us-east-1.rds.amazonaws.com'
db_username = 'admin'
db_password = 'stavros1332'
db_name = 'processed'

# Create a connection to the database
connection_string = f"mysql+mysqlconnector://{db_username}:{db_password}@{db_endpoint}/{db_name}"
engine = create_engine(connection_string)

combined_df.to_sql('proce', engine, if_exists='replace', index=False)

local_csv_path = 'C:\Users\maste\Desktop\Raw Data 2022\Yield_2022\yield plot\combined_data.csv'
combined_df.to_csv(local_csv_path, index=False)
