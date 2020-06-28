
---------------------------------------------
-- SENATE COSPONSORSHIP DATASET
---------------------------------------------

-- PROBLEM 1

 WITH pairs AS
(
SELECT DISTINCT sponsor_name, cosponsor_name
FROM cosponsors
)
SELECT t1.sponsor_name, COUNT(*) AS num
FROM pairs AS t1
INNER JOIN pairs AS t2
ON t1.sponsor_name=t2.cosponsor_name
  AND t1.cosponsor_name=t2.sponsor_name
GROUP BY t1.sponsor_name
ORDER BY num DESC
LIMIT 1

-- PROBLEM 2
 
WITH pairs AS
(
SELECT DISTINCT sponsor_name, cosponsor_name, sponsor_state
FROM cosponsors
), 
counts AS
(
SELECT t1.sponsor_state, t1.sponsor_name, COUNT(*) AS num
FROM pairs AS t1
INNER JOIN pairs AS t2
ON t1.sponsor_name=t2.cosponsor_name
  AND t1.cosponsor_name=t2.sponsor_name
GROUP BY t1.sponsor_name, t1.sponsor_state
ORDER BY num DESC
), 
states AS
(
SELECT sponsor_state, MAX(num) AS statemax
FROM counts
GROUP BY sponsor_state
)
SELECT c.sponsor_state, c.sponsor_name,
       c.num
FROM counts AS c
JOIN states AS s
     ON c.sponsor_state=s.sponsor_state
WHERE c.num=s.statemax
ORDER BY c.num DESC
 
-- PROBLEM 3

SELECT DISTINCT cosponsor_name FROM cosponsors
WHERE cosponsor_name NOT IN
(SELECT DISTINCT sponsor_name FROM cosponsors)

