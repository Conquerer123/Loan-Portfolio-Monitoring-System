import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Create output folder
Path("output/charts").mkdir(parents=True, exist_ok=True)

# Connect to database
conn = sqlite3.connect("loan_portfolio.db")

# Read data
loan_type = pd.read_sql("""
SELECT
    Loan_Type,
    SUM(Outstanding_Balance) AS Outstanding
FROM loan_portfolio
GROUP BY Loan_Type
ORDER BY Outstanding DESC
""", conn)

# Create chart
plt.figure(figsize=(8, 5))

plt.bar(
    loan_type["Loan_Type"],
    loan_type["Outstanding"]
)

plt.title("Outstanding Balance by Loan Type")
plt.xlabel("Loan Type")
plt.ylabel("Outstanding Balance")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig("output/charts/loan_type_outstanding.png")

plt.show()

conn.close()

print("Dashboard chart generated successfully!")