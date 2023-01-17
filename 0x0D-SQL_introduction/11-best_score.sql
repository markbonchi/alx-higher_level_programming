-- Script that lists all records with a score >= 10 in second_table
-- Database name passed as argument
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;