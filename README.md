# Loan Portfolio Monitoring & Risk Analysis System

## Overview

This project is an end-to-end loan portfolio analytics solution built using **Python, SQL (SQLite), and Pandas**.

It analyzes a synthetic portfolio of 5,000 loan accounts to monitor repayment behavior, portfolio exposure, and borrower risk. The project demonstrates how SQL and Python can be used together to generate analytical reports and support decision-making in banking and financial services.

---

## Features

- Generated a synthetic loan portfolio dataset (5,000 records)
- Imported loan data into SQLite database
- Performed SQL-based portfolio analysis
- Classified borrowers using Days Past Due (DPD)
- Generated portfolio reports using Python
- Created dashboard visualizations using Matplotlib

---

## Tech Stack

- Python
- SQLite
- Pandas
- Matplotlib
- Git & GitHub

---

## Project Structure

```
Loan-Portfolio-Monitoring-System/

├── data/
│   └── loan_portfolio.csv
│
├── python/
│   ├── generate_dataset.py
│   ├── import_data.py
│   ├── analysis.py
│   └── dashboard.py
│
├── sql/
│   ├── schema.sql
│   └── analysis_queries.sql
│
├── output/
│   ├── reports/
│   └── charts/
│
├── README.md
├── requirements.txt
└── loan_portfolio.db
```

---

## Key SQL Analysis

- Total Portfolio Exposure
- Outstanding Balance
- Risk Segment Distribution
- Loan Type Analysis
- State-wise Portfolio Analysis
- High-Risk Borrowers
- DPD Classification

---

## Sample Output

### Portfolio Summary

| Metric | Value |
|---------|------:|
| Total Loans | 5000 |
| Total Outstanding | ₹6.91 Billion |
| Average Outstanding | ₹1.38 Million |

---

## Future Enhancements

- Interactive Power BI Dashboard
- Predictive Default Risk Model
- Loan Recovery Trend Analysis
- Branch Performance Dashboard
- Monthly Portfolio Monitoring

---

## Author

**Karthik Prabhu**