--File: 15-groups.sql
--Description: script that lists the number of records with the same score in the table

-- script that lists the number of records with the same score in the table 
SELECT score, COUNT(*) AS number GROUP BY score ORDER BY number DESC, score DESC;
