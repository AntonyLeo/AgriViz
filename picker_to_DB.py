import pandas as pd
from sqlalchemy import create_engine

csv_file_path = 'path/to/your/csvfile.csv'

df = pd.read_csv(csv_file_path)

# MySQL connection details
db_endpoint = 'yielddatabase.coz72rpcgefb.us-east-1.rds.amazonaws.com'
db_username = 'admin'
db_password = 'stavros1332'
db_name = 'harvest'

# Create a connection to the database
connection_string = f"mysql+mysqlconnector://{db_username}:{db_password}@{db_endpoint}/{db_name}"
engine = create_engine(connection_string)

df.to_sql('picker', engine, if_exists='replace', index=False)

