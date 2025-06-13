SELECT IF(
    (SELECT COUNT(*) 
     FROM (
         SELECT num 
         FROM MyNumbers 
         GROUP BY num 
         HAVING COUNT(num) = 1
     ) AS temp) > 0,
     
    (SELECT num 
     FROM MyNumbers 
     GROUP BY num 
     HAVING COUNT(num) = 1 
     ORDER BY num DESC 
     LIMIT 1),
     
    null
) AS num;

