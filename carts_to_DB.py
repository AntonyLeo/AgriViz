import pandas as pd
import os
from sqlalchemy import create_engine

folder_path = "C:\Users\maste\Desktop\Project\Carts"

csv_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]

all_data = pd.DataFrame()
for file in csv_files:
    df = pd.read_csv(file)
    df.insert(1, 'Date', os.path.basename(file))  # Insert 'Date' as the second column
    all_data = all_data.append(df, ignore_index=True)

# MySQL connection details
db_endpoint = 'yielddatabase.coz72rpcgefb.us-east-1.rds.amazonaws.com'
db_username = 'admin'
db_password = 'stavros1332'
db_name = 'harvest'

# Create a connection to the database
connection_string = f"mysql+mysqlconnector://{db_username}:{db_password}@{db_endpoint}/{db_name}"
engine = create_engine(connection_string)

all_data.to_sql('carrito', engine, if_exists='replace', index=False)
