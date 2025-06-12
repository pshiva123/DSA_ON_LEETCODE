SELECT
  score,
  DENSE_RANK() OVER (ORDER BY score DESc) AS `rank`
FROM Scores
ORDER BY score DESC;

