'''
Recent Refinance Submissions, Credit Karma: 
https://platform.stratascratch.com/coding/2003-recent-refinance-submissions

Write a query that joins this submissions table to the loans table and returns the total loan balanceon each user’s most recent ‘Refinance’ submission. 
Return all users and the balance for each of them.
'''

WITH cte AS (
    SELECT l.user_id, l.created_at, s.balance, 
    row_number() OVER (PARTITION BY l.user_id 
    ORDER BY l.created_at ASC) AS rn
    FROM loans l
    INNER JOIN submissions s
    ON l.id = s.loan_id  
    WHERE s.rate_type = 'Refinance'
)
SELECT cte.user_id, cte.balance
FROM cte;


