import sqlite3
import pandas as pd

# Read the CSV
df = pd.read_csv("data/loan_portfolio.csv")

# Connect to SQLite database
conn = sqlite3.connect("loan_portfolio.db")

# Import data into SQL table
df.to_sql(
    "loan_portfolio",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Data imported successfully!")