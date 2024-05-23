-- Lists the number of records with the same score in the table second_table.
-- Records are ordered by descending count.
SELECT COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

