CREATE TABLE loan_portfolio (

    Loan_ID TEXT PRIMARY KEY,

    Customer_ID TEXT,

    Loan_Type TEXT,

    Loan_Amount INTEGER,

    Outstanding_Balance INTEGER,

    DPD INTEGER,

    Risk_Segment TEXT,

    State TEXT,

    Sanction_Date DATE

);