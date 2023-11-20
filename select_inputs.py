import pandas as pd
from sqlalchemy import create_engine

# MySQL connection details
db_endpoint = 'yielddatabase.coz72rpcgefb.us-east-1.rds.amazonaws.com'
db_username = 'admin'
db_password = 'stavros1332'
db_name = 'harvest'

# Create a connection to the database
connection_string = f"mysql+mysqlconnector://{db_username}:{db_password}@{db_endpoint}/{db_name}"
engine = create_engine(connection_string)

# SQL query to select specific columns
query = """
SELECT universal_time, GPS_TOW, LAT, LON, HEIGHT, ax, ay, az, filtered_mass, raw_mass
FROM raw_data
"""

# Execute the query and store the result in a DataFrame
df = pd.read_sql(query, engine)

# Specify the path for the CSV file
csv_file_path = 'C:\Users\maste\Desktop\Raw Data 2022\selected_data.csv'

# Save the DataFrame as a CSV file
df.to_csv(csv_file_path, index=False)
