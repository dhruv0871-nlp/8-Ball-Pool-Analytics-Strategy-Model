"""
CSV to SQLite Database Loader
Author: Dhruv
Description: Reads the raw pool match CSV and loads it into a structured SQLite database.
"""

import sqlite3
import pandas as pd

# 1. Read the CSV file we just generated
csv_file = 'pool_match_data.csv'
print(f"Reading {csv_file}...")
df = pd.read_csv(csv_file)

# 2. Create a connection to a new SQLite database (this creates the file if it doesn't exist)
db_name = 'pool_analytics.db'
conn = sqlite3.connect(db_name)
print(f"Connected to database: {db_name}")

# 3. Load the data into a SQL table named 'match_history'
# if_exists='replace' ensures we can run this script multiple times without duplicating data
table_name = 'match_history'
df.to_sql(table_name, conn, if_exists='replace', index=False)

# 4. Verify the data was loaded by running a quick SQL query via Python
cursor = conn.cursor()
cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
row_count = cursor.fetchone()[0]

print(f"Success! {row_count} rows inserted into the '{table_name}' table.")

# Close the connection
conn.close()