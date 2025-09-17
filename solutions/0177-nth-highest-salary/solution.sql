CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET n=N;
      # Write your MySQL query statement below.
      RETURN (WITH ranked AS (
  SELECT distinct salary,
         DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
  FROM Employee
)
SELECT salary
FROM ranked
WHERE rnk = N) ;
       
END
