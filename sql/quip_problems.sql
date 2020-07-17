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


---------
-- #3
---------
-- Find the number of retained users per month (i.e. number who logged in in current month that also logged in in past month)
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

WITH monthly_logins AS
(
    SELECT DISTINCT 
       user_id, MONTH(date) AS curmonth, YEAR(date) AS curyear,
       CASE WHEN MONTH(date)==1 THEN 12 ELSE MONTH(date)-1 END AS prevmonth,
       CASE WHEN MONTH(date)==1 THEN YEAR(date)-1 ELSE YEAR(date) END AS prevyear
    FROM logins
)
SELECT ml1.curmonth AS m, ml1.curyear AS y, COUNT(*) AS retained_users
FROM monthly_logins ml1
JOIN montly_logins ml2
     ON ml1.user_id=ml2.user_id AND ml1.prevmonth=ml2.curmonth AND ml1.prevyear=ml2.curyear
GROUP BY ml1.curmonth, ml1.curyear

-- Now find the number of *churned* users (i.e. those that did not return in a given month)

WITH monthly_logins AS
(
    SELECT DISTINCT 
       user_id, MONTH(date) AS curmonth, YEAR(date) AS curyear,
       CASE WHEN MONTH(date)==1 THEN 12 ELSE MONTH(date)-1 END AS prevmonth,
       CASE WHEN MONTH(date)==1 THEN YEAR(date)-1 ELSE YEAR(date) END AS prevyear
    FROM logins
)
SELECT ml1.curmonth AS m, ml1.curyear AS y, COUNT(*) AS churned_users
FROM monthly_logins ml1
RIGHT JOIN montly_logins ml2
     ON ml1.user_id=ml2.user_id AND ml1.prevmonth=ml2.curmonth AND ml1.prevyear=ml2.curyear
WHERE ml1.user_id is NULL
GROUP BY ml1.curmonth, ml1.curyear
