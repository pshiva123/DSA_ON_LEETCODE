CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET n=N-1;
      # Write your MySQL query statement below.
      RETURN (select distinct(salary) 
      from Employee 
      order by salary desc 
      limit 1 
      OFFSET n) ;
       
END
