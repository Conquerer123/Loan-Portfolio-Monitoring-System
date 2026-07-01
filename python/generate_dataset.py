import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

loan_types = [
    "Home Loan",
    "Personal Loan",
    "Auto Loan",
    "Education Loan",
    "Business Loan"
]

states = [
    "Karnataka",
    "Maharashtra",
    "Tamil Nadu",
    "Delhi",
    "Telangana"
]

records = []

for i in range(1, 5001):

    loan_id = f"LN{i:05d}"
    customer_id = f"CUST{i:05d}"

    loan_type = random.choice(loan_types)

    loan_amount = random.randint(50000, 5000000)

    outstanding_balance = random.randint(
        int(loan_amount * 0.1),
        loan_amount
    )

    dpd = random.randint(0, 180)

    if dpd == 0:
        risk_segment = "Low"
    elif dpd <= 60:
        risk_segment = "Medium"
    else:
        risk_segment = "High"

    state = random.choice(states)

    sanction_date = datetime(2020, 1, 1) + timedelta(
        days=random.randint(0, 2000)
    )

    records.append([
        loan_id,
        customer_id,
        loan_type,
        loan_amount,
        outstanding_balance,
        dpd,
        risk_segment,
        state,
        sanction_date.date()
    ])

df = pd.DataFrame(
    records,
    columns=[
        "Loan_ID",
        "Customer_ID",
        "Loan_Type",
        "Loan_Amount",
        "Outstanding_Balance",
        "DPD",
        "Risk_Segment",
        "State",
        "Sanction_Date"
    ]
)

df.to_csv("data/loan_portfolio.csv", index=False)

print("Dataset created successfully!")
print("Total records:", len(df))