# Write your MySQL query statement below
select d.name as Department , e.name as Employee ,e.salary as Salary 
from Employee e inner join Department d on e.departmentId = d.id
WHERE (
    SELECT COUNT(DISTINCT salary)
    FROM Employee
    WHERE departmentId = e.departmentId
    AND salary > e.salary
) < 3

