---------
-- #1
---------
-- Find the month-over-month percentage change for monthly active users (MAU). 
-- 
-- logins:
-- | user_id | date       |
-- |---------|------------|
-- | 1       | 2018-07-01 |
-- | 234     | 2018-07-02 |
-- | 3       | 2018-07-02 |
-- | 1       | 2018-07-02 |
-- | ...     | ...        |
-- | 234     | 2018-10-04 |

WITH mau AS
(
    SELECT MONTH(date) AS m, YEAR(date) AS y, COUNT(DISTINCT user_id) AS nau
    FROM logins
    GROUP BY MONTH(date), YEAR(date)
)
SELECT m, y, nau
    100 * nau / LAG(1, nau) OVER(ORDER BY y,m) - 100 AS pctchange
FROM mau
ORDERY BY y, m

---------
-- #2
---------
-- Write SQL such that we label each node as a “leaf”, “inner” or “Root” node
--
-- tree:
-- node   parent
-- 1       2
-- 2       5
-- 3       5
-- 4       3
-- 5       NULL 

SELECT node,
   CASE WHEN parent IS NULL THEN 'Root'
        WHEN node IN (SELECT parent FROM tree) THEN 'Inner'
        ELSE 'Leaf' END AS label
FROM tree
