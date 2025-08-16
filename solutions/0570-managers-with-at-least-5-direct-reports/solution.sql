# Write your MySQL query statement below
select a.name from employee a inner join employee b on a.id=b.managerId
 group by b.managerId having 
count(b.managerId)>=5;
