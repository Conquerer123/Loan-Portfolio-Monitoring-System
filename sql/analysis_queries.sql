-- Total number of loans
SELECT COUNT(*) AS Total_Loans
FROM loan_portfolio;

-- Total outstanding exposure
SELECT
    SUM(Outstanding_Balance) AS Total_Outstanding
FROM loan_portfolio;

SELECT
    ROUND(AVG(Outstanding_Balance),2) AS Average_Outstanding
FROM loan_portfolio;

SELECT
    Risk_Segment,
    COUNT(*) AS Total_Borrowers
FROM loan_portfolio
GROUP BY Risk_Segment
ORDER BY Total_Borrowers DESC;

SELECT

CASE

WHEN DPD = 0 THEN 'Current'

WHEN DPD BETWEEN 1 AND 30 THEN '1-30'

WHEN DPD BETWEEN 31 AND 60 THEN '31-60'

WHEN DPD BETWEEN 61 AND 90 THEN '61-90'

ELSE '90+'

END AS DPD_Bucket,

COUNT(*) AS Loans

FROM loan_portfolio

GROUP BY DPD_Bucket;


SELECT

Loan_Type,

SUM(Outstanding_Balance) AS Outstanding

FROM loan_portfolio

GROUP BY Loan_Type

ORDER BY Outstanding DESC;

SELECT

State,

SUM(Outstanding_Balance) AS Outstanding

FROM loan_portfolio

GROUP BY State

ORDER BY Outstanding DESC;

SELECT

Loan_ID,

Customer_ID,

Outstanding_Balance,

DPD

FROM loan_portfolio

WHERE DPD > 90

ORDER BY Outstanding_Balance DESC;

