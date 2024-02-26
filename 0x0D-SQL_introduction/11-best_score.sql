-- file: 11-best_score.sql
-- Description: listing all records if a table in a certain order

-- script that lists all records with specifications
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
