import sqlite3
import pandas as pd
import os


def create_output_folder():
    """Create output/reports folder if it doesn't exist"""

    os.makedirs("output/reports", exist_ok=True)


def get_portfolio_summary(conn):

    query = """
    SELECT
        COUNT(*) AS Total_Loans,
        SUM(Outstanding_Balance) AS Total_Outstanding,
        ROUND(AVG(Outstanding_Balance), 2) AS Average_Outstanding
    FROM loan_portfolio
    """

    return pd.read_sql(query, conn)


def get_risk_summary(conn):

    query = """
    SELECT
        Risk_Segment,
        COUNT(*) AS Borrowers,
        SUM(Outstanding_Balance) AS Outstanding
    FROM loan_portfolio
    GROUP BY Risk_Segment
    """

    return pd.read_sql(query, conn)


def get_loan_type_analysis(conn):

    query = """
    SELECT
        Loan_Type,
        COUNT(*) AS Loans,
        SUM(Outstanding_Balance) AS Outstanding
    FROM loan_portfolio
    GROUP BY Loan_Type
    ORDER BY Outstanding DESC
    """

    return pd.read_sql(query, conn)


def save_reports(portfolio_summary, risk_summary, loan_type):

    portfolio_summary.to_csv(
        "output/reports/portfolio_summary.csv",
        index=False
    )

    risk_summary.to_csv(
        "output/reports/risk_summary.csv",
        index=False
    )

    loan_type.to_csv(
        "output/reports/loan_type_analysis.csv",
        index=False
    )


def main():

    create_output_folder()

    conn = sqlite3.connect("loan_portfolio.db")

    portfolio_summary = get_portfolio_summary(conn)

    risk_summary = get_risk_summary(conn)

    loan_type = get_loan_type_analysis(conn)

    print("\n===== Portfolio Summary =====")
    print(portfolio_summary)

    print("\n===== Risk Segment Distribution =====")
    print(risk_summary)

    print("\n===== Loan Type Analysis =====")
    print(loan_type)

    save_reports(
        portfolio_summary,
        risk_summary,
        loan_type
    )

    conn.close()

    print("\nReports generated successfully!")


if __name__ == "__main__":
    main()