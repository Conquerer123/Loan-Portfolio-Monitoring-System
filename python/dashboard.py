import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Create output folder
Path("output/charts").mkdir(parents=True, exist_ok=True)

# Connect to SQLite database
conn = sqlite3.connect("loan_portfolio.db")

# -----------------------------
# Outstanding by Loan Type
# -----------------------------
loan_type = pd.read_sql("""
SELECT Loan_Type,
       SUM(Outstanding_Balance) AS Outstanding
FROM loan_portfolio
GROUP BY Loan_Type
ORDER BY Outstanding DESC
""", conn)

plt.figure(figsize=(8,5))
plt.bar(loan_type["Loan_Type"], loan_type["Outstanding"])
plt.title("Outstanding Balance by Loan Type")
plt.xlabel("Loan Type")
plt.ylabel("Outstanding Balance")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("output/charts/loan_type_outstanding.png")
plt.close()

# -----------------------------
# Risk Segment Distribution
# -----------------------------
risk = pd.read_sql("""
SELECT Risk_Segment,
       COUNT(*) AS Borrowers
FROM loan_portfolio
GROUP BY Risk_Segment
""", conn)

plt.figure(figsize=(6,4))
plt.bar(risk["Risk_Segment"], risk["Borrowers"])
plt.title("Risk Segment Distribution")
plt.xlabel("Risk Segment")
plt.ylabel("Borrowers")
plt.tight_layout()
plt.savefig("output/charts/risk_segment_distribution.png")
plt.close()

# -----------------------------
# State-wise Outstanding
# -----------------------------
state = pd.read_sql("""
SELECT State,
       SUM(Outstanding_Balance) AS Outstanding
FROM loan_portfolio
GROUP BY State
ORDER BY Outstanding DESC
""", conn)

plt.figure(figsize=(8,5))
plt.bar(state["State"], state["Outstanding"])
plt.title("Outstanding Balance by State")
plt.xlabel("State")
plt.ylabel("Outstanding Balance")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("output/charts/state_outstanding.png")
plt.close()

conn.close()

print("Dashboard charts generated successfully!")