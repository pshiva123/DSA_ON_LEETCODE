# Write your MySQL query statement below
select r.contest_id,
round((count(r.contest_id)/(select count(*) from users))*100,2) as 
percentage from users u 
right join register r on u.user_id=r.user_id group by
r.contest_id order by  round((count(r.contest_id)/(select count(*) from users))*100,2) desc , r.contest_id 
